from analisis import app
from flask import redirect, url_for, render_template
from flask import session

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    segment = 'index'  # Define el valor de segment
    return render_template('recepcion/home.html', segment=segment)

if __name__ == '__main__':
    app.run()
