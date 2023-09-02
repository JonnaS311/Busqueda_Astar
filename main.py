from grafo_ciudades import adyacentes,lista_ciudades, visitados

ciudad_inicial = lista_ciudades[0]
sumatoria_fn = 0

def busqueda_A(ciudad_Actual, sumatoria):
    if ciudad_Actual != lista_ciudades[9]:   # verificamos que no estamos en cartagena
        pesos = []
        ciudades_adyacentes = {}
        for i in range(len(adyacentes[ciudad_Actual.id])):
            if adyacentes[ciudad_Actual.id][i] != 0: #calculo de gn y la ciudad de la que es el dato
                pesos.append(calcular_gn(lista_ciudades[i],ciudad_Actual)+sumatoria)
                ciudades_adyacentes[lista_ciudades[i].id] = lista_ciudades[i].destino
        pesos = list(map(lambda x,y: x+y,pesos,ciudades_adyacentes.values()))
        for i in range(len(pesos)):
            if pesos[i] == min(pesos): #llamamos la función busqueda_A con la ciudad siguiente
                id = list(ciudades_adyacentes.keys())[i]
                sumatoria += calcular_gn(lista_ciudades[id],ciudad_Actual)
                print(lista_ciudades[id])
                print(sumatoria)
                busqueda_A(lista_ciudades[id],sumatoria)

def calcular_gn(nodo,nodo_ant):
    distancia = adyacentes[lista_ciudades[nodo.id].id][nodo_ant.id]
    visitados[lista_ciudades[nodo.id].id][nodo_ant.id], visitados[nodo_ant.id][lista_ciudades[nodo.id].id] = 1,1
    return distancia

busqueda_A(ciudad_inicial, sumatoria_fn)
