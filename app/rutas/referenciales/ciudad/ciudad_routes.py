from flask import Blueprint, render_template, jsonify
from app.dao.referenciales.ciudad.CiudadDao import CiudadDao

ciumod = Blueprint('ciudad', __name__, template_folder='templates')

@ciumod.route('/ciudad-index')
def ciudadIndex():
    ciudao = CiudadDao()
    return render_template('ciudad-index.html', lista_ciudades=ciudao.getCiudades())

@ciumod.route('/ciudad-agregar')
def ciudadAgregar():
    return render_template('ciudad-agregar.html')

# REST
@ciumod.route('/get-ciudades')
def getCiudades():
    ciudao = CiudadDao()
    return jsonify(ciudao.getCiudades())