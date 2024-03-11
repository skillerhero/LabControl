from analisis import db
class GruposAnalisisRel(db.Model):
    __tablename__='grupos_analisis_rel'
    gana_grupo_id_fk =db.Column(db.Integer,primary_key=True)
    gana_ana_id_fk =db.Column(db.Integer,primary_key=True)


    def __init__(self,gana_grupo_id_fk, gana_ana_id_fk )->None:
        self.gana_grupo_id_fk=gana_grupo_id_fk
        self.gana_ana_id_fk=gana_ana_id_fk

    def __repr__(self) -> str:
        return f'gana_grupo_id_fk:{self.gana_grupo_id_fk}, gana_ana_id_fk:{self.gana_ana_id_fk}'
