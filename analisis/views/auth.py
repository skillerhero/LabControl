import functools
from flask import render_template,Blueprint,flash,g,redirect,request,session,url_for
from analisis.models.user import User
from analisis.models.area import Area
from analisis.models.resultado import Resultado
from analisis.models.analisis import Analisis
from analisis.models.muestra import Muestra
from werkzeug.security import check_password_hash,generate_password_hash
from analisis import db
from flask import jsonify
auth=Blueprint('auth',__name__,url_prefix='/auth')
from sqlalchemy import func

#registra usuario
@auth.route('/register', methods=['GET', 'POST'])
def register():
    areas = Area.query.order_by('area_nombre').all()
    msg = None
    msg_class = ""

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        area = request.form.get('area')

        if not username:
            msg = "Se requiere nombre de usuario."
            msg_class = "alert-danger"
        elif not password:
            msg = "Se requiere contraseña."
            msg_class = "alert-danger"
        elif not area:
            msg = "Se requiere área."
            msg_class = "alert-danger"
        else:
            user_name = User.query.filter_by(user_username=username).first()
            if user_name is None:
                user = User(username, generate_password_hash(password), area)
                db.session.add(user)
                db.session.commit()
                msg = "Usuario creado exitosamente."
                msg_class = "alert-success"
            else:
                msg = f"El usuario {username} ya existe."
                msg_class = "alert-danger"

    return render_template('auth/register.html', areas=areas, msg=msg, msg_class=msg_class)

#Iniciar sesion
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = ""
        user = User.query.filter_by(user_username=username).first()

        if user is None:
            error += "Nombre de usuario incorrecto."
        elif not check_password_hash(user.user_password, password):
            error += "Contraseña incorrecta."

        if error != '':
            flash(error)
            return render_template('auth/login.html', msg=error)  # Pasar el mensaje de error a la plantilla HTML

        session.clear()
        session['user_id'] = user.user_id
        session['user_area_id_fk'] = user.user_area_id_fk

        if user.user_area_id_fk == 6 or user.user_area_id_fk == 7:
            return redirect(url_for("home.indexRecepcion")) 
        else:
            return redirect(url_for("home.index"))

    return render_template('auth/login.html', msg=None)  # Pasar el mensaje como None si no hay error


@auth.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    user_area_id = session.get("user_area_id_fk")
    if user_id is None:
        g.user = None
        g.area_nombre = None
    else:
        user = User.query.get_or_404(user_id)
        g.user = user
        if user_area_id:
            area = Area.query.filter_by(area_id=user_area_id).first()
            if area:
                g.area_nombre = area.area_nombre
            else:
                g.area_nombre = None
        else:
            g.area_nombre = None


@auth.route("logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view

def get_user_results():
    if session.get('user_area_id_fk') == 6 or session.get('user_area_id_fk') == 7:
        resultados = db.session.query(Muestra.mues_folio, Muestra.mues_fec_nac,Muestra.mues_nombre + ' ' + Muestra.mues_apellido_paterno + ' ' + Muestra.mues_apellido_materno)\
            .join(Resultado, Resultado.resul_mues_id_fk == Muestra.mues_id)\
            .join(Analisis, Resultado.resul_ana_id_fk == Analisis.ana_id)\
            .filter(Muestra.mues_sta == 'F')\
            .group_by(Muestra.mues_nombre)\
            .all()
    else:
        resultados = db.session.query(Analisis.ana_nombre, Muestra.mues_nombre)\
        .join(Resultado, Resultado.resul_ana_id_fk == Analisis.ana_id)\
        .join(Muestra, Resultado.resul_mues_id_fk == Muestra.mues_id)\
        .filter(Analisis.ana_area_id_fk == g.user.user_area_id_fk)\
        .filter(Resultado.resul_sta == 'O')\
        .add_columns(Muestra.mues_apellido_paterno, Muestra.mues_folio, Muestra.mues_alta_fec)\
        .group_by(Resultado.resul_ana_id_fk, Resultado.resul_mues_id_fk)\
        .all()
    return resultados

@auth.route('/get_user_results_ajax',methods=['GET','POST'])
def get_user_results_ajax():
    user_results = get_user_results()
    html_content = render_template('notification_modal_ajax.html', results=user_results)
    return jsonify({'html_content': html_content, 'count': len(user_results)})