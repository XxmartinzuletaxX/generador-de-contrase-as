import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("de cuantos caracteres sera tu contraseña?"))

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print(contraseña)
