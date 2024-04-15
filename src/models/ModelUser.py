from .entities.User import User
from werkzeug.security import generate_password_hash


class ModelUser():

    

    @classmethod
    def create(self, db, user):
        try:
            cursor = db.connection.cursor()
            hashed_password = generate_password_hash(user.password)
            # Insertar el nuevo usuario en la base de datos
            sql = """INSERT INTO user (correo, password, fullname, fechaN, telefono, direccion) 
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.correo, hashed_password, user.fullname, user.fechaN, user.telefono, user.direccion))
            db.connection.commit()
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)



    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            
            sql = """SELECT id, correo, password, fullname FROM user 
                    WHERE correo = '{}'""".format(user.correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, correo, fullname FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None, row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
