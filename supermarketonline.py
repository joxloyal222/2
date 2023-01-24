import os
import csv
admin = "kevin leal"
contra = "202020"



def usuario_verif():
    while True:
        p1 = input("ingrese el usuario\n>>>")

        if p1 == "kevin leal":
           print("usuario verificado\n")
           break
        else:
            print("usuario incorrecto")
            print("vuelva a intentarlo")
            print()
            print()





def password_verif ():
    while True:
        p2 = str(input("ingrese la contraseña\n>>>"))
        if p2 == "202020":
            print("bienvenido")
            break

        else:
            print("contraseña incorrecta")



usuario_verif()
password_verif()

os.system('cls')

queso_parmesano = ("""
>>>>>

(1) Queso Parmesano

Precio = 4500 colones
Descripcion = Queso de muy alta calidad importado desde belgica.

>>>>>

""")

leche_proteina = ("""

(2) Leche Proteina

Precio = 2000 colones 
Descripcion = caja de leche dos pinos con proteina , contenido neto = 1 litro

""")

cafe1820 = ("""

(3) Cafe 1820

Precio = 3850 colones
Descripcion = cafe 1820 100% puro , molido ,clasico.

""")

frutos_secos = ("""

(4) Frutos Secos

Precio = 3500 colones
Descripcion = paquete de frutos secos mixtos de almendras, pistachos, nueces , avellanas.

""")

pan_baguette = ("""

(5) Pan Baguette

Precio= 800 colones
Descripcion= pan baguette artesalan de la casa, bajo en calorias.

""")

coca_cola = ("""

(6) Coca Cola

Precio= 1700 colones
Descripcion= Coca cola Zero de 2 litros 

""")

print(queso_parmesano)
print(leche_proteina)
print(cafe1820)
print(frutos_secos)
print(pan_baguette)
print(coca_cola)

lista_principal = []
with open('lista_productos.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    file.close()


def producto_1():
    if chose == 1:
        item1 = ("Queso parmesano", "// 4500 colones")
        lista_principal.append(item1)


def producto_2():
    if chose == 2:
        item2 = ("Leche proteina", "// 2000 colones")
        lista_principal.append(item2)


def producto_3():
    if chose == 3:
        item3 = ("Cafe 1820", "// 3850 colones")
        lista_principal.append(item3)


def producto_4():
    if chose == 4:
        item4 = ("Frutos secos", "// 3500 colones")
        lista_principal.append(item4)


def producto_5():
    if chose == 5:
        item5 = ("Pan baguette", "// 800 colones")
        lista_principal.append(item5)


def producto_6():
    if chose == 6:
        item6 = ("Coca cola", "// 1780 colones")
        lista_principal.append(item6)


while True:
    chose = int(input("escribe el indice del producto que deseas añadir a lista\n>>>"))
    print("presiona el numero 0 para salir al menu")
    if chose == 1:
        producto_1()
    if chose == 2:
        producto_2()
    if chose == 3:
        producto_3()
    if chose == 4:
        producto_4()
    if chose == 5:
        producto_5()
    if chose == 6:
        producto_6()
    if chose == 0:
        with open('lista_productos.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(lista_principal)
            file.close()
        break

os.system('cls')
def ver_lista():

    print("si deseas ver la lista de compras presiona 1")
    finalopcion = int(input("\n>>>"))

    if finalopcion == 1:
        with open('lista_productos.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)








ver_lista()










  # for i in range(len(usuarios)):



