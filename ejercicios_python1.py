
# Ejercicio 1: Conversor de Temperatura - Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
#variables
grados_c = 10

#operaciones
grados_f = (grados_c * (9 / 5)) + 32

#resultado
print(grados_f)


# Ejercicio 2: Calculadora de Propina - Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
#variables
cuenta = 120
propina = cuenta * (15 / 100)

#operaciones
cuenta_total = cuenta + propina

#resultado
print(cuenta_total)


# Ejercicio 3: Verificación de Edad - Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
#variables
edad = 21
mayor_edad = 18

#operaciones
if edad < mayor_edad:
  print("El usuario es menor de edad")
else:
  print("El usuario es mayor de edad")


# Ejercicio 4: Contador de Vocales - Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
# Definimos una función que cuenta las vocales
def contar_vocales(palabra):
    # Definimos las vocales en minúsculas y mayúsculas
    vocales = "aeiouAEIOU"
    # Variable contador que se inicia en 0 y cuenta la vocales
    contador = 0
    # Bucle for que recorre cada letra de la variable palabra
    for letra in palabra:
        # Verificamos si cada letra que recorre está en la lista de vocales
        if letra in vocales:
            # Si la letra es una vocal, esta línea incrementa el valor de contador en 1
            contador += 1
    # Se recorren todas las letras de la palabra, el bucle for se completa y devuelve el valor del contador
    return contador

# Solicitamos al usuario que ingrese la palabra
palabra = input("Ingrese una palabra: ")

# Contamos las vocales en la palabra ingresada llamando a la funcion contar_vocales
numero_de_vocales = contar_vocales(palabra)

# Mostramos el resultado
# f"" (f-string/cadena formateada) - permite insertar variables directamente dentro de la cadena de texto
# Incluir valores de variables en una cadena sin necesidad de usar (+) para unir texto y variables
print(f"El número de vocales en '{palabra}' es: {numero_de_vocales}")


# Ejercicio 5: Suma de Números Pares - Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
# Definimos grupo de numeros del 1 al 100
uno_cien = range(1,101)
print(uno_cien)

# Identificamos dentro de uno_cien cuáles son números pares
num_pares = list(num for num in uno_cien if num % 2 == 0)
print(num_pares)

# Hacemos la suma de la lista de números pares obtenida
suma_pares = (sum(num_pares))
print(suma_pares)

print(f"La suma de todos los números pares dentro del 1 al 100 es: {suma_pares}" )



# Ejercicio 6: Verificación de Palíndromo - Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas y eliminamos espacios en blanco
    # Cuando incluimos (" ", "") quiere decir que busque lo primero y nos devuelva lo segundo + .lower que convierta en minúsculas
    palabra = palabra.replace(" ", "").lower()
    # Verificamos si la palabra es igual a su versión invertida
    # Cuando incluimos [::-1] quiere decir que nos devuelva nuestra variable al revés
    return palabra == palabra[::-1]

# Solicitamos al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra: ")

# Verificamos si la palabra es un palíndromo
if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' no es un palíndromo.")


# Ejercicio 7: Calculadora Simple - Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
# Variables
a = 6
b = 2

# Solicitamos al usuario que seleccione una operación aritmética
operacion_aritmetica = str(input("Seleccione una operación aritmética: "))

if operacion_aritmetica == "suma":
  print(a + b)

elif operacion_aritmetica == "resta":
  print(a - b)

elif operacion_aritmetica == "multiplicacion":
  print(a * b)

elif operacion_aritmetica == "division":
  print(a / b)

else:
  print("Error")

print(operacion_aritmetica)


# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC) - Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
# Solicitamos la usuario que indique su peso y altura
peso = float(input("Indique su peso (kg): "))
altura = float(input("Indique su altura (m): "))

# Calculamos el IMC con los datos que ha introducido el usuario. IMC = peso / altura
indice_masa_corporal = (peso / (altura ** 2))

print(indice_masa_corporal)


# Ejercicio 9: Conversor de Divisas - Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
#variables
dolar = 1
euro = dolar / 0.85

cantidad = int(input("Indique la cantidad ($) a convertir (€): "))

print(cantidad / 0.85)


# Ejercicio 10: Determinar el Día de la Semana - Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
numero = int(input("Indique el dia de las semana: "))

if numero == 1:
  print("El día correspondiente al número es: lunes")

elif numero == 2:
  print("El día correspondiente al número es: martes")

elif numero == 3:
  print("El día correspondiente al número es: miércoles")

elif numero == 4:
  print("El día correspondiente al número es: jueves")

elif numero == 5:
  print("El día correspondiente al número es: viernes")

elif numero == 6:
  print("El día correspondiente al número es: sábado")

elif numero == 7:
  print("El día correspondiente al número es: domingo")

else:
  print("Error")


# Ejercicio 11: Calculadora de Edad - Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
año_actual = 2024

año_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad_actual = int(año_actual - año_nacimiento)

print(edad_actual)


# Ejercicio 12: Calculadora de Área de un Rectángulo - Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
# Área = Largo * Ancho

largo = float(input("Introduzca la longitud del rectángulo: "))
ancho = float(input("Introduzca la anchura del rectángulo: "))

area = largo * ancho

print(area)


# Ejercicio 13: Verificación de Número Primo - Escribe un programa que determine si un número ingresado por el usuario es primo o no.
 Un número es primo cuando sólo se puede dividir entre 1 y entre él mismo + números < 2 no son primos.

def es_primo(numero):
  if numero < 2:
    return False
  for i in range(2, numero):
    if numero % i == 0:
      return False
  else:
    return True

numero = int(input("Introduzca un número: "))

if es_primo(numero):
  print(f"El número {numero} es primo")

else:
  print(f"El número {numero} no es primo")


# Ejercicio 14: Calculadora de Descuento - Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
precio_total = float(input("Introduzca el precio total de la compra sin descuento aplicado: "))
porcentaje_descuento = int(input("Introduzca el descuento a aplicar: "))

euros_descuento = float(precio_total) * (porcentaje_descuento / 100)

precio_descuento = precio_total - euros_descuento

print(precio_descuento)


# Ejercicio 15: Conversor de Tiempo - Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.
min_iniciales = int(input("Introduzca los minutos: "))

h_desglose = int(min_iniciales // 60)
min_desglose = int(min_iniciales % 60)

print("El desglose en horas y minutos de", min_iniciales, "es:", h_desglose, "horas y", min_desglose, "minutos")


# Ejercicio 16: Contador de Números Pares e Impares - Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
# Definimos listado de numeros
numeros = input("Introduzca un listado de 5 números (sin separarlos por comas ni espacios): ")
print(numeros)

listado_num = [int(c) for c in numeros]

print(list(listado_num))

# Identificamos dentro de numeros cuáles son números pares
num_pares = [par for par in listado_num if par % 2 == 0]
print(num_pares)

# Identificamos dentro de numeros cuáles son números impar
num_impares = [impar for impar in listado_num if impar % 2 != 0]
print(num_impares)

# Calculamos la cantidad de números que hay de cada
cantidad_pares = len(num_pares)
cantidad_impares = len(num_impares)

print("Hay un total de", cantidad_pares, "números pares:", list(num_pares))
print("Hay un total de", cantidad_impares, "números impares:", list(num_impares))


# Ejercicio 17: Conversor de Millas a Kilómetros - Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
millas = float(input("Introduzca el número de millas: "))

km = float(millas * 1.60934)

print(km)


# Ejercicio 18: Contador de Palabras - Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
frase = input("Introduzca una frase: ")

def contar_palabras(frase): # Creamos una función para contar las palabras de la frase introducida por el usuario
  i = 0 # Establecemos un contador a 0
  en_palabra = False # Establecemos un punto de partida en el que el contador no se ha encontrado ninguna palabra = 0

  for caracter in frase: # Para todos los caracteres dentro de la frase
    if caracter != " ": # Si dicho caracter es distinto de espacio
      if not en_palabra: # y si el contador se ha encontrado una palabra
        i += 1 # sumamos 1 al contador
        en_palabra = True # y establecemos como verdadero en_palabra

    else:
      en_palabra = False # De lo contrario no se ha encontrado con ninguna palabra, seguimos en el estado inicial
  
  return i

cantidad_palabras = contar_palabras(frase)  # Llamamos a la función

print(f"La frase introducida tiene {cantidad_palabras} palabras")


# Ejercicio 19: Verificación de Año Bisiesto - Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
# Un año es bisiesto cuando el año / 4 da de resultado un número entero

year = int(input("Introduzca un año: "))

if year % 4 == 0:
  print("El año", year, "es bisiesto")

else:
  print("El año", year, "no es bisiesto")


# Ejercicio 20: Suma de Números en una Lista - Crea un programa que sume todos los números en una lista ingresada por el usuario.
numeros = input("Introduzca un listado de números (sin separarlos por comas ni espacios): ")
print(numeros)

numeros = [int(c) for c in numeros]

listado = list(numeros)
print(listado)

print(sum(listado))

