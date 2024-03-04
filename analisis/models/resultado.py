from analisis import db
import datetime

class Resultado(db.Model):
    __tablename__ = 'resultados'
    resul_id = db.Column(db.Integer, primary_key=True)
    resul_ana_id_fk = db.Column(db.Integer)
    resul_mues_id_fk = db.Column(db.Integer)
    resul_fecha = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    resul_componente = db.Column(db.String(50))
    resul_unidad = db.Column(db.String(50))
    resul_resultado = db.Column(db.String(50))
    resul_rango = db.Column(db.String(50))
    resul_fuera_de_rango = db.Column(db.Boolean)
    resul_sta = db.Column(db.String(50))

    def __init__(self, resul_ana_id_fk,resul_mues_id_fk,resul_fecha, resul_componente, resul_unidad, resul_resultado, resul_rango, resul_fuera_de_rango,resul_sta):
        super(Resultado, self).__init__()
        self.resul_fecha = resul_fecha
        self.resul_componente = resul_componente
        self.resul_unidad = resul_unidad
        self.resul_resultado = resul_resultado
        self.resul_rango = resul_rango
        self.resul_fuera_de_rango = resul_fuera_de_rango
        self.resul_ana_id_fk = resul_ana_id_fk
        self.resul_mues_id_fk = resul_mues_id_fk
        self.resul_sta = resul_sta
