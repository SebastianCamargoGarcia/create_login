from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, correo, password, fullname = None, fechaN = None, telefono= None, direccion= None) -> None:
        self.id = id
        self.correo = correo
        self.password = password
        self.fullname = fullname
        self.fechaN = fechaN
        self.telefono = telefono
        self.direccion = direccion
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    print(generate_password_hash("123456"))