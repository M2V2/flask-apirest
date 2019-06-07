import datetime
from functools import wraps
import json
from cassandra.cqlengine import connection
from flask_cors import CORS
from flask import Blueprint, Response, request, make_response, jsonify
import flask
# from models.user import Person
from models.usuarios import Usuarios
from models.medico import Medico
from models.especialidad import Especialidad
from models.turnos import Turnos
import util

__author__ = 'hangvirus'

api = Blueprint("api", __name__)

CORS(api)

connection.setup(['192.168.0.120'], "cqlengine", protocol_version=3)


def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)  # Call Function
        json_result = util.to_json(result)
        return Response(response=json_result,
                        status=200,
                        mimetype="application/json")

    return decorated_function


@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World hehe"


#Esto es para registrar, no deberia de estar validado para crearse un usuario
@api.route("/agregar_usuario", methods=["POST"])
@json_api
def add_usuario():
    #data = flask.request.data #este da error

    user = Usuarios.create(user=request.form["user"], password=request.form["password"], estado=request.form["estado"], token_auth=request.form["token_auth"])
    user.save()
    return 'ok'




#DESDE AQUI HAY QUE VALIDAR AL USUARIO PARA ENTRAR A ESTOS PATHS
@api.route("/ver_usuario")
@json_api
def get_all_usuario():
    users = Usuarios.objects().all()
    return [user.get_data() for user in users]
#
# #
@api.route("/agregar_medico", methods=["POST"])
@json_api
def add_medico():
    # data = json.loads(flask.request.data)
    medico = Medico.create(cin=request.form["cin"], nombre_doc=request.form["nombre_doc"], horario=request.form['horario'],
                          estado=request.form['estado'], especialidad=request.form['especialidad'])
    medico.save()
    return medico.get_data()

    # print(datetime.datetime.strptime(request.form['horario'], '%H:%M').time())


@api.route("/ver_medico")
@json_api
def get_all_medico():
    medicos = Medico.objects().all()
    return [medico.get_data() for medico in medicos]
# #

@api.route("/agregar_especialidad", methods=["POST"])
@json_api
def add_especialidad():
    # data = json.loads(flask.request.data)
    especialidad = Especialidad.create(especialidad=request.form["especialidad"])
    especialidad.save()
    return especialidad.get_data()

@api.route("/ver_especialidad")
@json_api
def get_all_especialidad():
    especialidades = Especialidad.objects().all()
    return [especialidad.get_data() for especialidad in especialidades]

# #
@api.route("/agregar_turnos", methods=["POST"])
@json_api
def add_turnos():
    # data = json.loads(flask.request.data)
    turno = Turnos.create(nro_turno=request.form["nro_turno"], fecha=request.form["fecha"], hora=request.form['hora'],
                           medico=request.form['medico'], persona=request.form['persona'], estado_turnos=request.form['estado_turnos'])
    turno.save()
    return turno.get_data()

@api.route("/ver_turnos")
@json_api
def get_all_persona():
    turnos = Turnos.objects().all()
    return [turno.get_data() for turno in turnos]



######################################################################################################

# @api.route("/add", methods=["POST"])
# @json_api
# def add_person():
#     data = json.loads(flask.request.data)
#     person = Person.create(first_name=data["first_name"], last_name=data["last_name"])
#     person.save()
#     return person.get_data()
#
#
#
# @api.route("/get-all")
# @json_api
# def get_all():
#     persons = Person.objects().all()
#     return [person.get_data() for person in persons]

