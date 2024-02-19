from analisis import db
class Area(db.Model):
    __tablename__='areas'
    area_id=db.Column(db.Integer,primary_key=True)
    area_nombre=db.Column(db.String(80))
    area_sta=db.Column(db.String(1))

    def __init__(self, area_nombre, area_sta):
        super().__init__()
        self.area_nombre = area_nombre
        self.area_sta = area_sta

    def __repr__(self) -> str:
        return f'User:{self.area_nombre}'