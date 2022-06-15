import os
os.system("cls")

def calcula_iva(monto):
    try:
        if monto == 0:
            print("Monto ingresado, es cero o vacio, reintente")
            return

        else:
            iva = monto * (19 / 100)
            return monto + iva
    except:
            print("Monto ingresado, es cero o vacio, reintente")        

def descuento(monto):
    try:
        if monto == "" or monto == 0:
            print("Monto ingresado, es cero o vacio, reintente")
            return
        elif monto >= 1000:
            descuento = monto * (10 / 100)
            print("Descuento aplicado 10%")
            return monto - descuento
        elif monto >= 5000:
            descuento = monto * (15 / 100)
            print("Descuento aplicado 15%")
            return monto - descuento
        elif monto >= 10000:
            descuento = monto * (20 / 100)
            print("Descuento aplicado 20%")
            return monto - descuento
        elif monto >= 25000:
            descuento = monto * (30 / 100)
            print("Descuento aplicado 30%")
            return monto - descuento     
        else:
            print("Sin Descuento aplicado")
            return monto
    except:
        print("Monto ingresado, es cero o vacio, reintente")

def calcula_imc(peso,estatura):
    try:
        if peso == 0 and  estatura == 0:
            print("Monto ingresado, es cero o vacio, reintente")
            return False

        else:
            imc =round(peso / (estatura**2))
            if imc < 18.5:
                print("Bajo Peso")
            elif imc >= 18.6 and imc <= 24.9:
                print("Adecuado")
            elif imc >= 25 and imc <= 29.9:
                print("Sobrepeso")
            elif imc >= 30 and imc <= 34.9:
                print("Obesidad grado 1")
            elif imc >= 35 and imc <= 39.9:
                print("Obesidad grado 2")
            elif imc > 40:
                print("Obesidad grado 3")
            return imc
    except:
            print("Monto ingresado, es cero o vacio, reintente")

sw = True
while sw == True:
    print("1.- Calcular IVA")
    print("2.- Calcular Descuento")
    print("3.- Calcular IMC")
    print("4.- Salir")
    try:
        op=int(input("Seleccione una Opcion: "))
        if (op > 0 and op < 5 ):
            if op == 1:
                print("Ha Seleccionado la  opcion 1")
                precio_articulo=int(input("Ingrese precio del Producto ej 4500 : "))
                if precio_articulo !=0:
                    precio_con_iva=calcula_iva(precio_articulo)
                    print("Precio sin IVA: ",precio_articulo)
                    print("Precio Con IVA: ",precio_con_iva)
                    sw=False
            if op == 2:
                print("Ha Seleccionado la  opcion 2")
                precio_articulo=int(input("Ingrese precio del Producto ej 4500 : "))
                if precio_articulo !=0:
                    precio_con_desc=descuento(precio_articulo)
                    print("Precio Real: ",precio_articulo)
                    print("Precio Con Descuento: ",precio_con_desc)
                    sw=False
            if op == 3:
                print("Ha Seleccionado la  opcion 3")
                peso=float(input("Ingrese peso de la Persona 75.7 : "))
                estatura=float(input("Ingrese estatura de la Persona 1.80 : "))
                if peso !=0 and estatura !=0:
                    imc=calcula_imc(peso,estatura)
                    print(imc);
                    sw=False
            if op == 4:
                print("Ha Seleccionado Salir del menu, adios")
                sw=False

        else:            
            print("Opcion ingresada es INVALIDA.")

    except:
            print("ERROR, de ingreso, reintente")
