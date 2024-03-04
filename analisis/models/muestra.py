from analisis import db
import datetime
class Muestra(db.Model):
    __tablename__='muestras'
    mues_id =db.Column(db.Integer,primary_key=True)
    mues_sta=db.Column(db.String(1),default='A')
    mues_alta_fec=db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    mues_folio=db.Column(db.String(20))
    mues_nombre=db.Column(db.String(80))
    mues_apellido_paterno=db.Column(db.String(80))
    mues_apellido_materno=db.Column(db.String(80))
    mues_calle=db.Column(db.String(80))
    mues_num_ext=db.Column(db.String(8))
    mues_num_int=db.Column(db.String(8))
    mues_colonia=db.Column(db.String(80))
    mues_tel=db.Column(db.String(15))
    mues_email=db.Column(db.String(80))
    mues_horas_ayuno=db.Column(db.Integer)
    mues_alimentos=db.Column(db.String(1024))
    mues_enfermedades=db.Column(db.String(1024))
    mues_medicamentos=db.Column(db.String(1024))
    mues_rubrica=db.Column(db.String(80))
    mues_des_id_fk=db.Column(db.Integer)
    mues_edad = db.Column(db.Integer)
    mues_fec_nac = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    def __init__(self,mues_folio, mues_nombre, mues_apellido_paterno, mues_apellido_materno, mues_calle, mues_num_ext, mues_num_int, mues_colonia, mues_tel, mues_email, mues_horas_ayuno, mues_alimentos, mues_enfermedades, mues_medicamentos, mues_rubrica,mues_des_id_fk)->None:
        self.mues_folio=mues_folio
        self.mues_nombre=mues_nombre
        self.mues_apellido_paterno=mues_apellido_paterno
        self.mues_apellido_materno=mues_apellido_materno
        self.mues_calle=mues_calle
        self.mues_num_ext=mues_num_ext
        self.mues_num_int=mues_num_int
        self.mues_colonia=mues_colonia
        self.mues_tel=mues_tel
        self.mues_email=mues_email
        self.mues_horas_ayuno=mues_horas_ayuno
        self.mues_alimentos=mues_alimentos
        self.mues_enfermedades=mues_enfermedades
        self.mues_medicamentos=mues_medicamentos
        self.mues_rubrica=mues_rubrica
        self.mues_des_id_fk=mues_des_id_fk

    def __repr__(self) -> str:
        return f'mues_id:{self.mues_id}, mues_folio:{self.mues_folio}'
