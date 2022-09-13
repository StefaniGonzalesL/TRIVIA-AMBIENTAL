import time
import random  # Importamos la librería random

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
iniciar_trivia = True 
intentos = 0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("\033[32m Bienvenido a mi trivia sobre medio ambiente \033[39m")

print ("\033[33m Pondremos a prueba tus conocimientos \033[39m ")
print ("\033[35m Cargando...nos vemos en 5 segundos!!\033[39m")
time.sleep(5) # Espera 5 segundos antes de continuar.


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = random.randint(0, 10)
    print ("Tienes", puntaje, "puntos")
    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")
  
    # Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

    nombre = input ("Ingresa tu nombre: ")

    # Es importante dar instrucciones sobre cómo jugar:
    # Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
    print ("\033[34m \n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n \033[39m")

    # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
    print ("\033[35m Cargando...nos vemos en 5 segundos!!\033[39m")
    time.sleep(5) # Espera 5 segundos antes de continuar.
    # Pregunta 1
    print ("\033[32m1)¿Cuánto tarda en degradarse una botella de plástico? \033[39m")
    print ("a) 10-40 años")
    print ("b) 60-100 años")
    print ("c) Más de 500 años")
    print ("d) 300 años")

    # Almacenamos la respuesta del usuario en la variable "respuesta_1"
    respuesta_1 = input("\nTu respuesta: ")

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_1 == "c":
        puntaje += 10
        print ("Muy bien", nombre, "!")
    else:
        print ("Incorrecto", nombre, "!")


    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 2
    print("\033[32m2)¿Qué color de contenedor usarías para desechar unas cáscaras de frutas? \033[39m ")
    print("a) Rojo")
    print("b) Verde")
    print("c) Negro")
    print("d) Marrón")

    # Almacenamos la respuesta del usuario en la variable "respuesta_2"
    respuesta_2 = input("\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "a":
        print ("Incorrecto!", nombre, "El color rojo es para pilas, lámparas y luminarias, medicinas vencidas, empaques de plaguicidas y otros.")
    elif respuesta_2 == "b":
        print ("Incorrecto!", nombre, "El color verde es para papel, cartón, vidrio, plástico, textiles, madera, cuero, empaques compuestos, metales (latas y afines).")
    elif respuesta_2 == "c":
        print ("Incorrecto!", nombre, "El color negro es para papel encerado, cerámicos, colillas de cigarro, residuos sanitarios")
    else:
        puntaje += 10
        print ("Muy bien", nombre, "!")

    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 3
    print("\033[32m3)¿Qué cantidad de agua esta disponible para el consumo humano? \033[39m")
    print("a) 35%")
    print("b) 70%")
    print("c) 15%")
    print("d) 1%")

    # Almacenamos la respuesta del usuario en la variable "respuesta_3"
    respuesta_3 = input("\nTu respuesta: ")

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "a":
        print ("Incorrecto!", nombre, "Sigue pensando jeje")
        puntaje = puntaje / 2
    elif respuesta_3 == "b":
        print ("Incorrecto!", nombre, "Sigue intentando")
        puntaje = puntaje / 6
    elif respuesta_3 == "c":
        print ("Cerquita, pero no es")
        puntaje = puntaje + 5
    else:
        print ("Correcto, tienes una bonificación extra!")
        puntaje = puntaje * 2

    print("\033[36m ¡Ruleta de puntaje final!\033[39m")
    print("\033[36m ¿Desea un sorteo aleatorio de puntajes?\033[39m")


    for i in range (5,0,-1):
        print(i)
        time.sleep (3)
    puntaje2 = random.randint(0, 10)

    print("Tu puntaje en la ruleta final es: " , puntaje2 )
    print ("\033[33m Gracias", nombre, "por jugar mi trivia, Pero.. el puntaje real que alcanzaste es", puntaje, "puntos")
    print("\n \033[32m ¿Deseas intentar la trivia nuevamente?\033[39m")
    repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

    if repetir_trivia != "si":  # != significa "distinto"
     print("\nEspero que lo hayas pasado bien, hasta pronto!")
     iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.