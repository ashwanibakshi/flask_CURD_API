from flask import request,jsonify
from model import User,UserSchema
from app import db,app

@app.route('/addUser',methods=['POST'])
def addUser():
    dataa = request.get_json()
    namee = dataa.get('name')
    userData = User(name=namee)
    db.session.add(userData)
    db.session.commit()
    return 'data inserted'

user_schema = UserSchema(many=True)

@app.route('/showallUser',methods=['GET'])
def showall():
    userData = db.session.query(User).all()
    result = user_schema.dump(userData)
    return jsonify(result)

@app.route('/updateUser',methods=['PUT'])
def update():
    upData = request.get_json()
    dataa = db.session.query(User).get(upData.get('id'))
    dataa.name = upData.get('name')
    db.session.add(dataa)
    db.session.commit()
    return 'updated record'

@app.route('/deleteUser/<id>',methods=['DELETE'])
def delete(id):
  db.session.query(User).filter(User.id==id).delete()
  db.session.commit()
  return 'deleted record id '+id