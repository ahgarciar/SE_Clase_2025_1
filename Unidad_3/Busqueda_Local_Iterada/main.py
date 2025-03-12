
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
    solucion_temporal = crea_solucion(5)  #S0
    print("solucion temporal: ", solucion_temporal)
    best_solucion = solucion_temporal[:] #copia de los valores
    best_vo = calcula_fo(best_solucion)
    print("solucion vo inicial: ", best_vo)

    max_it_ils = 100  #iterated local search = ils
    it_ils = 0

    max_it_local = 10000
    it_local  = 0

    while it_ils < max_it_ils: #busqueda local iterada

        while it_local < max_it_local: #busqueda local
            solucion_temporal = crea_solucion_vecina(solucion_temporal)
            vo_temporal = calcula_fo(solucion_temporal)

            if vo_temporal < best_vo:
                best_vo = vo_temporal
                best_solucion = solucion_temporal[:]
                print("nueva best solucion: ", solucion_temporal, end="    ")
                print("vo: ", vo_temporal)

            #print("it", end="   ")
            #print("solucion: ", solucion_temporal, end="    ")
            #print("vo: ", vo_temporal)
            it_local+=1

        solucion_temporal = perturbacion(solucion_temporal)
        vo_temporal = calcula_fo(solucion_temporal)
        if vo_temporal < best_vo:
            best_vo = vo_temporal
            best_solucion = solucion_temporal[:]
            print("nueva best solucion: ", solucion_temporal, end="    ")
            print("vo: ", vo_temporal)
        it_ils +=1

    print("mejor solucion: ", best_solucion)
    print("mejor vo: ", best_vo)

    #soft and hard constrainst