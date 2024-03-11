from analisis import db
class Descuento(db.Model):
    __tablename__='descuentos'
    des_id=db.Column(db.Integer,primary_key=True)
    des_nombre=db.Column(db.String(80))
    des_dsc=db.Column(db.String(255))
    des_sta=db.Column(db.String(1))
    des_descuento=db.Column(db.Numeric(5,0))

    def __init__(self,des_nombre, des_dsc, des_sta, des_descuento)->None:
        self.des_nombre =des_nombre
        self.des_dsc=des_dsc
        self.des_sta =des_sta
        self.des_descuento=des_descuento

    def __repr__(self) -> str:
        return f'Descuento:{self.des_nombre}'