#implementando librerias
import time


st = time.time()   

graph = {
    '1': {'2': 7000000,'3': 1500000,'4': 6000000},
    '2': {'1': 7000000,'5': 300000,'6': 9000000,'7': 3500000,'8': 2100000},
    '3': {'1': 1500000, '9': 300000,'10': 1000000},
    '4': {'1': 6000000, '11': 1800000,'12': 3000000,'13': 2100000,'14': 1500000},
    '5': {'2': 300000,'15': 1000000},
    '6': {'2': 9000000,'16': 3700000,'17': 1600000},
    '7': {'2': 3500000,'26': 3700000,'27': 2100000,'28': 1400000,'29': 1200000},
    '8': {'2': 2100000,'39': 1600000,'40': 3000000,'41': 8000000},
    '9': {'3': 30000000,'48': 9000000},
    '10': {'3': 1000000},
    '11': {'4': 18000000},
    '12': {'4': 30000000},
    '13': {'4': 20000001},
    '14': {'4': 15000000},
    '15': {'5': 10000000,'16': 16000000,'17': 50000000},
    '16': {'15': 16000000},
    '17': {'15': 50000000},
    '18': {'6': 37000000,'20': 21000000,'21': 14000000,'22': 12000000},
    '19': {'6': 16000000,'22': 50000000,'23': 30000000,'24': 15000000},
    '20': {'18': 21000000},
    '21':{'18':14000000},
    '22':{'18':12000000},
    '23':{'19':50000000},
    '24':{'19':30000000},
    '25':{'19':15000000},
    '26':{'7':37000000,'30':18000000},
    '27':{'7':21000000,'31':30000000, '32':15000000,'33':18000000},
    '28':{'7':14000000,'34':15000000,'35':10000000},
    '29':{'7':12000000,'37':10000000,'38':80000000},
    '30':{'26':18000000},
    '31':{'27':30000000},
    '32':{'27':15000000},
    '33':{'27':18000000},
    '34':{'28':15000000},
    '35':{'28':10000000},
    '36': {'29':10000000},
    '37': {'29':80000000},
    '38': {'8':16000000,'41':10000000,'42':50000000},
    '39': {'8':30000000,'43':18000000,'44':21000000,'43':15000000},
    '40': {'8':80000000,'46':10000000,'47':12000000},
    '41': {'38':10000000},
    '42': {'38':50000000},
    '43': {'39':18000000},
    '44': {'39':21000000},
    '45': {'39':15000000},
    '46': {'40':10000000},
    '47': {'40':12000000},
    '48': {'9':90000000}
}

def greedy_search(graph, start_node, end_node):
    # Inicializar los nodos visitados y los nodos por visitar
    visited = [start_node]
    to_visit = [start_node]
    # Inicializar la suma total del camino
    total_value = 0

    while to_visit:
        # Obtener el siguiente nodo por visitar
        current = to_visit.pop(0)
        # Si es el nodo final, se ha encontrado el camino más corto
        if current == end_node:
            return visited, total_value
        # Buscar los nodos adyacentes al nodo actual y añadirlos a la lista de nodos por visitar
        neighbors = graph[current]
        neighbor_costs = [(neighbor, cost) for neighbor, cost in neighbors.items() if neighbor not in visited]
        #dependiendo de su costo.sort es para ordenar los nodos adyacentes del nodo actual
        neighbor_costs.sort(key=lambda x: x[1])
        for neighbor, cost in neighbor_costs:
            to_visit.append(neighbor)
            # Añadir el costo del nodo adyacente a la suma total del camino
            total_value += cost
            # Marcar el nodo adyacente como visitado
            visited.append(neighbor)

    # Si no se ha encontrado un camino entre los nodos de inicio y final, devolver None
    if end_node not in visited:
        return None
    return visited, total_value

start_node = input("Ingresa el nodo de inicio:") 
end_node = input("Ingresa el nodo a buscar: ")

shortest_path= greedy_search(graph, start_node, end_node)

if shortest_path is None:
    print("No hay camino posible.")
else:
    print("El camino más corto es:", shortest_path[0], "con un costo total de", shortest_path[1])

print("Process finished --- %s seconds ---" % (time.time()-st))