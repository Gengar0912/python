from flask import Blueprint, request, jsonify
login = Blueprint('/login',__name__)

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    global user,password

    user =request.json['user']
    password =request.json['password']
    inicializarVariables(user,password)


    salida = {'codRes': codRes, 'menRes': menRes, 'usuario':user, 'accion': accion}
    return jsonify(salida)


def inicializarVariables(user,password):
    global codRes, menRes,accion
    userLocal= "marcos"
    passLocal="123"
    codRes ='SIN_ERROR'
    menRes='OK'
    try:     
        print("verificar login")
        if(str(password)==str(passLocal) and str(user)==str(userLocal)):
            print("Usuario y contraseña OK")
            accion="succes"
        else:
            print("Usuario o contraseña incorrecta")
            accion="Usuario o contraseña incorrecta"

    except Exception as e:
        print("Error",str(e))
        codRes='Error'
        menRes='Msg'+ str (e)