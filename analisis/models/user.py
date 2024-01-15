from analisis import db
class User(db.Model):
    __tablename__='users'
    user_id=db.Column(db.Integer,primary_key=True)
    user_username=db.Column(db.String(50))
    user_password=db.Column(db.Text)
    user_area_id_fk=db.Column(db.Integer)

    def __init__(self,username,password,area_id)->None:
        self.user_username=username
        self.user_password=password
        self.user_area_id_fk=area_id

    def __repr__(self) -> str:
        return f'User:{self.user_username}'
