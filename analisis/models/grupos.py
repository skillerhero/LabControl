from analisis import db
class Grupo(db.Model):
    __tablename__ = 'grupos'

    grupo_id = db.Column(db.Integer, primary_key=True)
    grupo_nombre = db.Column(db.String(80))
    grupo_sta = db.Column(db.String(1))
    grupo_costo = db.Column(db.Numeric(20, 2))

    def __init__(self, grupo_nombre, grupo_costo):
        self.grupo_nombre = grupo_nombre
        self.grupo_costo = grupo_costo

    def __repr__(self):
        return f'Grupo: {self.grupo_nombre}'
