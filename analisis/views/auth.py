import functools
from flask import render_template,Blueprint,flash,g,redirect,request,session,url_for
from analisis.models.user import User
from analisis.models.area import Area
from analisis.models.resultado import Resultado
from analisis.models.analisis import Analisis
from werkzeug.security import check_password_hash,generate_password_hash
from analisis import db

auth=Blueprint('auth',__name__,url_prefix='/auth')

#registra usuario
@auth.route('/register',methods=['GET','POST'])
def register():
    areas=Area.query.order_by('area_nombre').all()
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        area=request.form.get('area')
        user=User(username,generate_password_hash(password),area)
        error=""
        if not username:
            error+="Se requiere nombre de usuario"
        elif not password:
            error+="Se requiere password"
        elif not area:
            error+="Se requiere area"
        user_name=User.query.filter_by(user_username=username).first()
        if user_name==None:
            db.session.add(user)
            db.session.commit()
        else:
            error+=f"El usuario {username} ya existe"
        if error=='':
            flash("Usuario creado")
        flash(error)
    return render_template('auth/register.html',areas=areas)

@auth.route('/login',methods=['GET','POST'])
def login():
    print("inicio")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("username: ", username)
        print("password: ", password)

        error = ""
        user = User.query.filter_by(user_username=username).first()
        
        print("user: ", user)
        print("area: ", user.user_area_id_fk)
        if user is None:
            error += "nombre de usuario incorrecto"
        elif not check_password_hash(user.user_password, password):
            error += "contraseña incorrecta"
        if error != '':
            print(error)
            flash(error)
        else:
            session.clear()
            session['user_id'] = user.user_id
            session['user_area_id_fk'] = user.user_area_id_fk
            print("No hay errores, redirigiendo...")

            if user.user_area_id_fk == 6 or user.user_area_id_fk == 7:
                return redirect(url_for("home.indexRecepcion")) 
            else:
                return redirect(url_for("home.index"))
    print("fin")
    return render_template('auth/login.html')

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
    results = Resultado.query.join(Analisis, Resultado.resul_ana_id_fk == Analisis.ana_id)\
                              .filter(Analisis.ana_area_id_fk == g.user.user_area_id_fk).all()
    return results

@auth.route('/get_user_results_ajax',methods=['GET','POST'])
def get_user_results_ajax():
    user_results = get_user_results()
    html_content = render_template('notification_modal_ajax.html', results=user_results)
    return html_content