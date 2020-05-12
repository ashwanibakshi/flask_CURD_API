from app import db,ma

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)

def __init__(self,name):
    self.name = name

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name')