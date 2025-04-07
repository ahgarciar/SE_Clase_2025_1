import math
import random as rnd
#rnd.seed(5)
xmin = -10
xmax = 10

def crea_solucion_vecina(solucion):
    vector = solucion[:]
    index = rnd.randint(0, len(solucion)-1)
    nuevo_valor = rnd.randint(xmin, xmax)
    vector[index] = nuevo_valor
    return vector

def calcula_fo(solucion):
    vo = sum([i**2 for i in solucion])
    return vo

def crea_solucion(n):
    v = [rnd.randint(xmin, xmax) for i in range(n)]
    return v

def perturbacion(solucion): #modificacion brusca de la solucion
    vector = solucion[:]

    index1 = rnd.randint(0, len(solucion) - 1)
    index2 = index1  ####
    while index2 == index1:
        index2 = rnd.randint(0, len(solucion) - 1)

    nuevo_valor1 = rnd.randint(xmin, xmax)
    nuevo_valor2 = rnd.randint(xmin, xmax)

    vector[index1] = nuevo_valor1
    vector[index2] = nuevo_valor2

    return vector


if __name__ == "__main__":
    print("Inicia algoritmo:")

    #Seleccionar una solución inicial S;

    solucion_temporal = crea_solucion(5)  #S0
    print("solucion temporal: ", solucion_temporal)
    best_solucion = solucion_temporal[:]  # copia de los valores
    best_vo = calcula_fo(best_solucion)

    better_solucion = solucion_temporal[:]
    better_vo = best_vo
    print("solucion vo inicial: ", best_vo)

    #Seleccionar una temperatura inicial Ti > 0;
    T = 1000

    #Seleccionar una función de reducción de la temperatura α;
    alfa = 0.8  #  [0.8 - 0.99]

    #Seleccionar un número de iteraciones N;
    max_it = 100
    it = 0

    #Seleccionar un criterio de parada;
    #-> alcanzar a revisar todas las iteraciones mrcadas
    #-> que la temperatura (T) llegue a cierto umbral

    while T > 1: #ciclo externo
        it = 0
        while it < max_it: #ciclo interno
            solucion_temporal = crea_solucion_vecina(solucion_temporal)
            vo_temporal = calcula_fo(solucion_temporal)

            deltaF = vo_temporal - better_vo

            if deltaF < 0:
                better_vo = vo_temporal
                better_solucion = solucion_temporal[:]
                #print("nueva better solucion: ", solucion_temporal, end="    ")
                #print("vo: ", vo_temporal)
            else:
                t = rnd.random() # 0 - 1
                #print(deltaF, "     ",  T,"     ", math.e)
                c = math.pow(math.e, deltaF/T)
                if t < c:
                    better_vo = vo_temporal
                    better_solucion = solucion_temporal[:]
                    #print("nueva better** solucion: ", solucion_temporal, end="    ")
                    #print("vo: ", vo_temporal)

            #print("it", end="   ")
            #print("solucion: ", solucion_temporal, end="    ")
            #print("vo: ", vo_temporal)
            it+=1

        if better_vo < best_vo:
            best_vo = better_vo
            best_solucion = better_solucion[:]
            print("nueva BEST solucion: ", better_solucion, end="    ")
            print("vo: ", best_vo)

        T = T * alfa

    print("mejor solucion: ", best_solucion)
    print("mejor vo: ", best_vo)

    #soft and hard constrainst