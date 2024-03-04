from analisis import db
import datetime
class GruposAnalisisRel(db.Model):
    __tablename__='grupos_analisis_rel'
    gana_grupo_id_fk =db.Column(db.Integer(10))
    gana_ana_id_fk =db.Column(db.Integer(10))


    def __init__(self,gana_grupo_id_fk, gana_ana_id_fk )->None:
        self.gana_grupo_id_fk=gana_grupo_id_fk
        self.gana_ana_id_fk=gana_ana_id_fk

    def __repr__(self) -> str:
        return f'gana_grupo_id_fk:{self.gana_grupo_id_fk}, gana_ana_id_fk:{self.gana_ana_id_fk}'
