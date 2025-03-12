# Actual -> valor leido desde el sensor
# Objetivo -> valor obtenido desde el heuristico
actuadores = {
    "temperatura1": {"actual": 22, "objetivo": 20},
    #"intensidad_luminosa": {"actual": 200, "objetivo": 210},
    #"humedad": {"actual": 50, "objetivo": 40},
    #"ruido": {"actual": 100, "objetivo": 30}
    "temperatura2": {"actual": 18, "objetivo": 20},
    "temperatura3": {"actual": 24, "objetivo": 24},
}


#Funcion asociada a apicar el ajuste a los actuadores.
# El ajuste dependera de cada actuador, por ejemplo subir un poco la intensidad por vez
# o prender el dispositivo (ej. AC, calefector), etc.
def ajustar_actuador(actuador, diferencia): #codigo de muestra, debe asociarse a cada actuador.!!
    if diferencia == 0:
        print("No se hace nada")
    elif diferencia < 0:
        print("Se ajusta en sentido A. Por ejemplo, se enciende el AC")
    elif diferencia > 0: #else
        print("Se ajusta en sentido B. Por ejemplo se enciende el Calefactor")


# Se determina si es necesario hacer algun ajuste por cada actuador
for actuador, valores in actuadores.items():
    diferencia = valores["objetivo"] - valores["actual"]
    print("Actuador", actuador, " diferencia -> ", diferencia)
    ajustar_actuador(actuador, diferencia)
    print()

#DE MANANERA GENERAL EL FUNCIONAMIENTO PUDIERA SER...
#   1.- SE LEE UN VALOR DE LOS SENSORES
#   2.- SE APLICA UN HEURISTICO
#   3.- CON BASE EN LOS VALORES SE DETERMINA UNA ACCION CON LOS ACTUADORES
#       - PUEDE:
#           *APLICARSE EL CAMBIO Y DETENERSE HASTA ALCANZAR QUE LA DIFERENCIA SEA CERO
#               (NO MUY RECOMENDABLE, PORQUE DETIENE LA EJECUCION DEL PROCESO GENERAL)#
#           *APLICARSE EL CAMBIO Y VOLVER AL PUNTO 1 PARA REPETIR EL PROCESO (RECOMENDABLE)