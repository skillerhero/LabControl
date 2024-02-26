from analisis import db
import datetime

class Resultado(db.Model):
    __tablename__ = 'resultados'
    resul_id = db.Column(db.Integer, primary_key=True)
    resul_ana_id = db.Column(db.Integer)
    resul_mues_id = db.Column(db.Integer)
    resul_fecha = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    resul_componente = db.Column(db.String(255))
    resul_unidad = db.Column(db.String(255))
    resul_resultado = db.Column(db.String(255))
    resul_rango = db.Column(db.String(255))
    resul_fuera_de_rango = db.Column(db.Boolean)

    def __init__(self, resul_fecha, resul_componente, resul_unidad, resul_resultado, resul_rango, resul_fuera_de_rango,resul_ana_id,resul_mues_id):
        super(Resultado, self).__init__()
        self.resul_fecha = resul_fecha
        self.resul_componente = resul_componente
        self.resul_unidad = resul_unidad
        self.resul_resultado = resul_resultado
        self.resul_rango = resul_rango
        self.resul_fuera_de_rango = resul_fuera_de_rango
        self.resul_ana_id = resul_ana_id
        self.resul_mues_id = resul_mues_id
