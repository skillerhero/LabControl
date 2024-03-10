from analisis import db
class Analisis(db.Model):
    __tablename__='analisis'
    ana_id=db.Column(db.Integer,primary_key=True)
    ana_nombre=db.Column(db.String(80))
    ana_costo=db.Column(db.Numeric(20,2))
    ana_area_id_fk=db.Column(db.Integer)
    ana_sta=db.Column(db.String(1))

    def __init__(self,ana_nombre, ana_costo, ana_area_id_fk, ana_sta=ana_sta)->None:
        self.ana_nombre =ana_nombre
        self.ana_costo=ana_costo
        self.ana_area_id=ana_area_id_fk
        self.ana_sta = ana_sta

    def __repr__(self) -> str:
        return f' Analisis:{self.ana_nombre}'