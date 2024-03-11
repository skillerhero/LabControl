from analisis import db
class MedicionesAnalisis(db.Model):
    __tablename__='mediciones_analisis'
    mediciones_analisis_id=db.Column(db.Integer,primary_key=True)
    mediciones_analisis_ana_id_fk=db.Column(db.Integer)
    mediciones_analisis_componente = db.Column(db.String(50))
    mediciones_analisis_unidad = db.Column(db.String(50))
    mediciones_analisis_rango = db.Column(db.String(50))

    def __init__(self,mediciones_analisis_ana_id_fk,mediciones_analisis_componente=None,mediciones_analisis_unidad=None,mediciones_analisis_rango=None)->None:
        self.mediciones_analisis_ana_id_fk=mediciones_analisis_ana_id_fk
        self.mediciones_analisis_componente=mediciones_analisis_componente
        self.mediciones_analisis_unidad=mediciones_analisis_unidad
        self.mediciones_analisis_rango=mediciones_analisis_rango

    def __repr__(self) -> str:
        return f'Medicion:{self.mediciones_analisis_id}'
    
    @property
    def serialize(self):
        return {
            'mediciones_analisis_id': self.mediciones_analisis_id,
            'mediciones_analisis_ana_id_fk': self.mediciones_analisis_ana_id_fk,
            'mediciones_analisis_componente': self.mediciones_analisis_componente,
            'mediciones_analisis_unidad': self.mediciones_analisis_unidad,
            'mediciones_analisis_rango': self.mediciones_analisis_rango
        }