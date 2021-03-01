# ejercicio 1
print('Bienvenidos a su frutera de confianza')
print('donde le ofrecemos los mejores descuentos')
print('segun la cantidad de kilos de manzanas que lleve ')
print('1. Un kilo de manzanas = $6.500')
kiloManzana = 6500
cantidad = float(input('Ingrese la cantidad de manzanas que desea llevar: '))
subtotal = kiloManzana * cantidad
if cantidad < 2:
    descuento = 0
elif cantidad >= 2 and cantidad < 5:
    descuento = subtotal * 0.1
elif cantidad >= 5 and cantidad < 10:
    descuento = subtotal * 0.15
else:
    descuento = subtotal * 0.2
total = subtotal - descuento
print(f'Su descuento fue de: ${descuento:,}')
print(f'El total a pagar es: ${total:,}')

# Hacer algoritmo que de el valor final por la compra de abanicos. El
# descuento lo hace basado a la clave, si la clave es 010 el descuento
# es del 20% y si la clave es 020 el descuento es del 40%, si ela clave
# es 030 el descuento es 55% y si es 040 el 75%.
print('¡Bienvenidos!')
print('Aqui encontraras todo tipo de abanicos')
print('con descuentos de locura')
clave = input('Ingrese la clave: ')
precio = float(input('Ingrese el valor del abanico: '))
cantidad = float(input('Ingrese la cantidad: '))
subtotal = precio * cantidad
descuento = 0
if clave == '010':
    descuento = subtotal * 0.2
elif clave == '020':
    descuento = subtotal * 0.4
elif clave == '030':
    descuento = subtotal * 0.55
elif clave == '040':
    descuento = subtotal * 0.75
else:
    print('No tiene descuento')
total = subtotal - descuento
print(f'Su descuento fue de: ${descuento:,}')
print(f'El total a pagar es: ${total:,}')
# Un proveedor de estéreos ofrece un descuento del 20% sobre el
# precio sin IVA, de algún aparato si este cuesta $4000 o más.
# Además, independientemente de esto, ofrece un 10% de descuento
# si la marca es NOSY. Determinar cuanto pagará, con IVA incluido, un
# cliente cualquiera por la compra de su aparato. IVA es del 30%.
print('Bienvenidos')
articulo = float(input('Ingrese el valor del articulo (sin IVA): '))
print('¿La marca del producto es Nosy?')
print('Elija el numero que tenga su respuesta')
print('0. no')
print('1. si')
nosy = int(input(''))
descuento = 0
descuentoNosy = 0
if articulo >= 4000:
    descuento = articulo * 0.2
if nosy == 1:
    descuentoNosy = articulo * 0.1
iva = articulo * 0.3
total = articulo - descuento - descuentoNosy + iva
print(f'El valor total es: ${total}')

# El gobierno Colombiano desea reforestar un bosque que mide un
# determinado número de hectáreas. Si la superficie del terreno excede
# a 5 hectáreas se sembrarán 80% Pino, 15% Oyamel y 5% Cedro. Si
# es menor o igual a 5 hectáreas se sembrarán 45% Pino, 25% Oyamel
# y 30% Cedro. Que cantidad de hectáreas le corresponde sembrar al
# Gobierno de Pino, Oyamel y Cedro.
print('Plan de reforestación')
terreno = float(input('Ingrese el numero de hectareas: '))
if terreno > 5:
    Pino = terreno * 0.8
    Oyamel = terreno * 0.15
    Cedro = terreno * 0.05
else:
    Pino = terreno * 0.45
    Oyamel = terreno * 0.25
    Cedro = terreno * 0.3
print(f'El bosque tiene un total de {terreno} hectareas')
print('El gobierno debera sembrar:')
print(f'{Pino} hectareas de Pinos')
print(f'{Oyamel} hectareas de Oyamel')
print(f'{Cedro} de hectareas de Cedro')

# ejercicio 5

numUno = int(input('Ingrese un numero: '))
numDos = int(input('Ingrese un numero: '))
numTres = int(input('Ingrese un numero: '))
if numUno > numDos and numUno > numTres:
    print(f'El numero mayor es: {numUno}')
elif numDos > numUno and numDos > numTres:
    print(f'El numero mayor es: {numDos}')
else:
    print(f'El numero mayor es: {numTres}')
