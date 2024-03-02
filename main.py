# Este código servirá para generar contraseñas aleatorias 
# El usuario podrá elegir la longitud de la contraseña
# El usuario podrá elegir si la contraseña tendrá letras mayúsculas, minúsculas, números y/o símbolos

import random
import string
import datetime

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    try:
        # Conjuntos de caracteres disponibles
        caracteres = ''
        if incluir_mayusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_simbolos:
            caracteres += string.punctuation

        # Verificar que haya al menos un conjunto de caracteres seleccionado
        if not caracteres:
            raise ValueError("Debe seleccionar al menos un conjunto de caracteres.")

        # Verificar que la longitud sea mayor a cero
        if longitud <= 0:
            raise ValueError("La longitud de la contraseña debe ser mayor a cero.")

        # Generar la contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        return contraseña

    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

def guardar_contraseña(contraseña):
    try:
        ahora = datetime.datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        with open("contraseñas_guardadas.txt", "a") as archivo:
            archivo.write(f"{fecha_hora} - {contraseña}\n")
        print("Contraseña guardada con éxito. Viva! Viva! Viva!")
    except Exception as e:
        print(f"Error al guardar la contraseña: {str(e)}")

def main():
    print("""#############################
# Yeyo's Password Generator #
#############################""")
    while True:
        try:
            longitud = input('Longitud de la contraseña: ')
            while not longitud.isdigit() or int(longitud) <= 0 or int(longitud) > 100:
                print("La longitud de la contraseña debe ser un número mayor a cero y menor o igual a 100.")
                longitud = input('Longitud de la contraseña: ')
            longitud = int(longitud) 
            incluir_mayusculas = input('¿Incluir mayúsculas? (s/n): ').lower() == 's'
            incluir_minusculas = input('¿Incluir minúsculas? (s/n): ').lower() == 's'
            incluir_numeros = input('¿Incluir números? (s/n): ').lower() == 's'
            incluir_simbolos = input('¿Incluir símbolos? (s/n): ').lower() == 's'


            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
            print(f'Contraseña generada: {contraseña}')

            guardar = input("¿Deseas guardar la contraseña generada? (s/n): ").lower() == 's'

            if guardar:
                guardar_contraseña(contraseña)
                
            continuar = input("¿Deseas generar otra contraseña? (s/n): ").lower() == 's'
            if not continuar:
                print("Bye bye!")
                break

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

    
if __name__ == '__main__':
    main()
    