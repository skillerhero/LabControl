import functools
from flask import render_template,Blueprint,flash,g,redirect,request,session,url_for
from analisis.models.user import User
from analisis.models.area import Area
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
            print("No hay errores, redirigiendo...")

            if user.user_area_id_fk == 6 or user.user_area_id_fk == 7:
                return redirect(url_for("home.indexRecepcion")) 
            else:
                return redirect(url_for("home.index"))
    print("fin")
    return render_template('auth/login.html')

@auth.before_app_request
def load_logged_in_user():
    user_id=session.get("user_id")
    if user_id==None:
        g.user=None
    else:
        g.user=User.query.get_or_404(user_id)

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


