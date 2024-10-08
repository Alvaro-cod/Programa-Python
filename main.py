from Vagon import Vagon
from tren import Tren
from Pasajero import Pasajero
from boleto import Boleto

# aqui el numero de paradas 
def main():
    tren = Tren(paradas=["Estación 1", "Estación 2", "Estación 3"])
    
    for i in range(1, 4):  # numero de vagones
        tren.agregar_vagon(Vagon(i))
    
    while True:
        print("\nMenú de opciones:")
        print("1. Subir pasajero")
        print("2. Bajar pasajero")
        print("3. Listar pasajeros")
        print("4. Contar pasajeros por género")
        print("5. Buscar pasajero")
        print("6. Ordenar pasajeros por edad")
        print("7. Calcular total pagado")
        print("8. Mostrar estadísticas")
        print("9. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        # pide toda la informacion del pasajero 
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            genero = input("Género (M/F): ")
            numero_vagon = int(input("Número de vagón: "))
            numero_silla = int(input("Número de silla: "))
            
            boleto = Boleto(numero_vagon, numero_silla, None, edad)
            pasajero = Pasajero(nombre, edad, genero, boleto)
            tren.subir_pasajero(pasajero)
        
        # al ingresar el numero de una silla baja al pasajero que haya en ella
        elif opcion == "2":
            numero_silla = int(input("Número de silla a liberar: "))
            tren.bajar_pasajero(numero_silla)
        
        # hace una lista de todos los pasajeros del tren 
        elif opcion == "3":
            pasajeros = tren.listar_pasajeros()
            for pasajero in pasajeros:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}, Precio: {pasajero.boleto.precio}")
        
        # hace la cuenta de cuantos pasajeros hay por genero 
        elif opcion == "4":
            conteo = tren.contar_pasajeros_por_genero()
            print(f"Hombres: {conteo['M']}, Mujeres: {conteo['F']}")
        
        # busca un pasajero por nombre y ofrece la informacion que hay de el
        elif opcion == "5":
            nombre = input("Nombre del pasajero a buscar: ")
            pasajero = tren.buscar_pasajero(nombre)
            if pasajero:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}, Precio: {pasajero.boleto.precio}")
            else:
                print("Pasajero no encontrado.")
        
        #  ordena todos los pasajeros por edad de menor a mayor
        elif opcion == "6":
            pasajeros = tren.ordenar_pasajeros_por_edad()
            for pasajero in pasajeros:
                print(f"Nombre: {pasajero.nombre}, Edad: {pasajero.edad}, Género: {pasajero.genero}, Asiento: {pasajero.boleto.get_numero_asiento()}, Precio: {pasajero.boleto.precio}")
        
        # calcula el total pagado por los pasajeros
        elif opcion == "7":
            total = tren.calcular_total_pagado()
            print(f"Total pagado: {total}")
        
        # muestra cuntas personas hay subidad cuantas bajadas y lo que se ha pagado
        elif opcion == "8":
            tren.mostrar_estadisticas()
        
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
