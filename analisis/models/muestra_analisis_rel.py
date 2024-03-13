from analisis import db
import datetime
class MuestraAnalisisRel(db.Model):
    __tablename__='muestra_analisis_rel'
    muan_mues_id_fk=db.Column(db.Integer,primary_key=True)
    muan_ana_id_fk=db.Column(db.Integer,primary_key=True)
    muan_alta_fec=db.Column(db.DateTime(timezone=True),server_default=("CURRENT_TIMESTAMP"))
    muan_sta=db.Column(db.String(1),default='A')
    muan_resultado=db.Column(db.Float)

    def __init__(self,muan_mues_id_fk, muan_ana_id_fk, muan_alta_fec=None, muan_sta=None, muan_resultado=None)->None:
        self.muan_mues_id_fk=muan_mues_id_fk
        self.muan_ana_id_fk=muan_ana_id_fk
        self.muan_alta_fec=muan_alta_fec
        self.muan_sta=muan_sta
        self.muan_resultado=muan_resultado

    def __repr__(self) -> str:
        return f'Resultado:{self.muan_resultado}'