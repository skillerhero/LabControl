from analisis import app
from flask import redirect, url_for
from flask import session
from analisis.views.auth import auth

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    print('user_id: ', session)
    return redirect(url_for('home.index'))

if __name__ == '__main__':
    app.run( )