from myapp import db

class tbl_user(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100), unique=True, nullable=True)
   password = db.Column(db.String(50), unique=True,nullable=True)

class tbl_house(db.Model):
   id=db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), unique=True, nullable=True)
   size = db.Column(db.String(100), unique=True, nullable=True)
   price=db.Column(db.Float,unique=False,nullable=True)
   status=db.Column(db.Integer,unique=False,nullable=True)

class tbl_menu(db.Model):
   id=db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), unique=True, nullable=True)
   location = db.Column(db.String(100), unique=True, nullable=True)
   outlet=db.Column(db.Integer,unique=False,nullable=True)
   available=db.Column(db.Integer,unique=False,nullable=True)
