import random
from werkzeug.security import generate_password_hash

minus = "qwertyuiopasdfghjklñzxcvbnm"
mayus = minus.upper()
numeros = "1234567890"
simbolos = "@_:;][*¨¡?=)(/&%$#!-,.}{+´¿'|°}"

base = minus+mayus+numeros+simbolos
longitud = 8
for _ in range(1):
    muestra = random.sample(base, longitud)
    password ="".join(muestra) 
    password_encriptado = generate_password_hash(password)
    print("contraseña: {} → {}".format(password, password_encriptado))