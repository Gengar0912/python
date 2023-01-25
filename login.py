from flask import Blueprint, request, jsonify
login = Blueprint('/login',__name__)

@login.route('/login', methods=['POST'])
def llamarServicios():
    global usar,passw

    user =request.json['user']
    passw =request.json['passw']

    print("username",user)
    print("password",passw)