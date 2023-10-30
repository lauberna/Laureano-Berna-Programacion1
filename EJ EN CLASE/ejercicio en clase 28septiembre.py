dia = input("Ingrese el día de la semana: ").lower().strip()
num_dia = int(input("Ingrese el número del día: "))
num_mes = int(input("Ingrese el número del mes: "))

dias_semana = ["lunes", "martes", "miercoles",
               "jueves", "viernes", "sabado", "domingo"]

""" establezco una condicion general para que si los datos ingresados en el comienzo son incorrectos no se siga con la ejecucion del programa
 """
if dia in dias_semana and 1 <= num_dia <= 31 and 1 <= num_mes <= 12:
    """ luego establezco condiciones secundarias segun el dia ingresado donde se evaluaran
    y ejecutara el codigo especifico"""

    if dia == "lunes" or dia == "martes" or dia == "miercoles":
        examenes = input("se tomaron los examenes?(s/n): ").lower()
        if examenes == "s":
            aprobados = int(input("ingrese la cantidad de aprobados: "))
            desaprobados = int(input("ingrese la cantidad de desaprobados: "))
            porcentaje_aprobados = round(
                (aprobados*100)/(aprobados+desaprobados))
            print(f"porcentaje de aprobados: {porcentaje_aprobados}%")
        else:
            print("Opcion incorrecta.")
    elif dia == "jueves":
        asistencia = int(
            input("ingrese el porcentaje de asistencia a clase: "))
        print("asistio la mayoria" if asistencia >
              50 else "no asistio la mayoria")
    elif dia == "viernes" and num_dia == 1 and num_mes == 1 or num_mes == 7:
        print("comienzo de nuevo ciclo")
        alumnos = int(
            input("ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = int(input("ingrese el arancel por cada alumno: "))
        print(f"el ingreo total es de {alumnos*arancel}$")
    elif (dia == "sabado" or dia == "domingo"):
        print("es fin de semana")
else:
    print('Error en los datos ingresados')
