from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from myapp.model import tbl_user, tbl_house, tbl_menu
from myapp import app, db

@app.route('/data/<username>')
def index(username):
    user = tbl_user.query.filter_by(name=username).first()
    res = {'id': user.id, 'name': user.name, 'password': user.password}
    return jsonify(res)

@app.route('/outlet')
def getOutlet():
    houses=tbl_house.query.all()
    data=[];
    for house in houses:
        res={'id':house.id,'name':house.name,'price':house.price,'status':house.status,'size':house.size}
        data.append(res);
    return jsonify(data)

@app.route('/menu')
def getMenu():
    menus=tbl_menu.query.all()
    data=[];
    for menu in menus:
        res={'id':menu.id,'name':menu.name,'location':menu.location,'outlet':menu.outlet,'available':menu.available}
        data.append(res);
    return jsonify(data)


@app.errorhandler(Exception)
def exception_error(err):
    app.logger.exception(err)
    return jsonify({'message': f'{err}'}), 400


@app.errorhandler(SQLAlchemyError)
def sql_error(err):
    app.logger.exception(err)
    message = str(err.__dict__['orig'])
    return jsonify({'message': f'{message}'}), 402


@app.errorhandler(KeyError)
def key_error(err):
    app.logger.exception(err)
    return jsonify({'message': f'Invalid key {err}'}), 401
