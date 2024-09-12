from flask import Flask

app=Flask(__name__)

app.secret_key = '19790523'

#importar referenciales
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix='/ciudad')



