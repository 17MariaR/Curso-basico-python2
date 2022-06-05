# Se declara una variable

Calificacion = input("introduce tu calificacion de AZ-900:")
Calificacion = int(Calificacion)

# Se pregunta si la calificacion es < 700

if Calificacion < 700 :
    print("No estudiaste haha") # Si es <700 se muestra este mensaje
elif Calificacion > 1000 :
    print("MIENTEEEES!, no hay puntuacion >1000")
else : # Si no se cumple el if anterior pasa a esta linea
    print("Felicidades, crack") #Se ejecuta si niguno de los if se cumple

# Verificador de edades
edad = input("Introduce tu edad")
edad = int(edad)
if edad >=18 and edad <=100 :
    print("Bienvenido al after")
elif edad > 100 :
    print("Solo se fia a noventeros acompa;ados de sus abuelos")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes consumir alcohol")