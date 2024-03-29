from analisis import db
import datetime

class Resultado(db.Model):
    __tablename__ = 'resultados'
    resul_id = db.Column(db.Integer, primary_key=True)
    resul_medicion_analisis_id_fk = db.Column(db.Integer)
    resul_ana_id_fk = db.Column(db.Integer)
    resul_mues_id_fk = db.Column(db.Integer)
    resul_fecha = db.Column(db.DateTime(timezone=True), server_default=("CURRENT_TIMESTAMP"))
    resul_resultado = db.Column(db.String(50))
    resul_fuera_de_rango = db.Column(db.Boolean)
    resul_sta = db.Column(db.String(50))

    def __init__(self, resul_medicion_analisis_id_fk, resul_ana_id_fk,resul_mues_id_fk,
                 resul_fecha, resul_resultado, resul_fuera_de_rango,resul_sta):
        super(Resultado, self).__init__()
        self.resul_medicion_analisis_id_fk = resul_medicion_analisis_id_fk
        self.resul_ana_id_fk = resul_ana_id_fk
        self.resul_mues_id_fk = resul_mues_id_fk
        self.resul_fecha = resul_fecha
        self.resul_resultado = resul_resultado
        self.resul_fuera_de_rango = resul_fuera_de_rango
        self.resul_sta = resul_sta

    def __repr__(self):
        return f"Resultado(resul_id={self.resul_id}, " \
        f"resul_medicion_analisis_id_fk={self.resul_medicion_analisis_id_fk}, " \
        f"resul_ana_id_fk={self.resul_ana_id_fk}, " \
        f"resul_mues_id_fk={self.resul_mues_id_fk}, " \
        f"resul_fecha={self.resul_fecha}, " \
        f"resul_resultado={self.resul_resultado}, " \
        f"resul_fuera_de_rango={self.resul_fuera_de_rango}, " \
        f"resul_sta={self.resul_sta})"