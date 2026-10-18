import networkx as nx
import matplotlib.pyplot as plt


def problema_rutas():
    """Encuentra la ruta de menor costo entre ubicaciones usando Dijkstra."""
    grafo = nx.DiGraph()

    # Aristas dirigidas con costo ilustrativo de traslado (minutos).
    conexiones = [
        ("Inicio", "A", 4),
        ("Inicio", "B", 2),
        ("A", "C", 5),
        ("B", "A", 1),
        ("B", "C", 8),
        ("B", "D", 10),
        ("C", "Meta", 3),
        ("D", "Meta", 2),
        ("A", "Meta", 12),
    ]
    for origen, destino, costo in conexiones:
        grafo.add_edge(origen, destino, weight=costo)

    inicio, meta = "Inicio", "Meta"
    ruta = nx.dijkstra_path(grafo, inicio, meta, weight="weight")
    costo_total = nx.dijkstra_path_length(grafo, inicio, meta, weight="weight")

    print("\nPROBLEMA 1: RUTA DE MENOR COSTO")
    print("Estado inicial:", inicio)
    print("Estado objetivo:", meta)
    print("Acciones: desplazarse por una conexión disponible.")
    print("Ruta encontrada:", " -> ".join(ruta))
    print("Costo total (minutos ilustrativos):", costo_total)

    posiciones = {
        "Inicio": (0, 1), "A": (1, 2), "B": (1, 0),
        "C": (2, 2), "D": (2, 0), "Meta": (3, 1)
    }
    etiquetas = {(u, v): f"{d['weight']}" for u, v, d in grafo.edges(data=True)}
    plt.figure(figsize=(9, 5))
    nx.draw_networkx(grafo, posiciones, with_labels=True, node_size=1800,
                     node_color="lightblue", arrows=True, font_size=9)
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas, font_size=8)
    ruta_aristas = list(zip(ruta, ruta[1:]))
    nx.draw_networkx_edges(grafo, posiciones, edgelist=ruta_aristas,
                           edge_color="green", width=3, arrows=True)
    plt.title("Problema 1: ruta de menor costo (etiquetas = costo)")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("grafo_rutas_generado.png", dpi=180)
    plt.close()


def problema_laberinto():
    """Encuentra un camino válido en una cuadrícula mediante búsqueda BFS."""
    # 0 = celda transitable; 1 = obstáculo.
    mapa = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    filas, columnas = len(mapa), len(mapa[0])
    inicio, meta = (0, 0), (4, 4)
    grafo = nx.Graph()

    # Cada celda libre es un estado; cada movimiento ortogonal cuesta 1.
    for f in range(filas):
        for c in range(columnas):
            if mapa[f][c] == 0:
                grafo.add_node((f, c))
                for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nf, nc = f + df, c + dc
                    if 0 <= nf < filas and 0 <= nc < columnas and mapa[nf][nc] == 0:
                        grafo.add_edge((f, c), (nf, nc), weight=1)

    ruta = nx.shortest_path(grafo, inicio, meta)  # BFS para grafo no ponderado
    print("\nPROBLEMA 2: NAVEGACIÓN EN LABERINTO")
    print("Estado inicial (fila, columna):", inicio)
    print("Estado objetivo (fila, columna):", meta)
    print("Acciones: arriba, abajo, izquierda o derecha; no atravesar obstáculos.")
    print("Ruta encontrada:", ruta)
    print("Costo (número de movimientos):", len(ruta) - 1)

    # Representación visual: camino encontrado, espacios transitables y obstáculos.
    plt.figure(figsize=(6, 6))
    for f in range(filas):
        for c in range(columnas):
            if mapa[f][c] == 1:
                plt.scatter(c, filas - 1 - f, s=800, marker="s", color="dimgray")
            else:
                plt.scatter(c, filas - 1 - f, s=800, marker="s", color="white",
                            edgecolors="black")
    xs = [p[1] for p in ruta]
    ys = [filas - 1 - p[0] for p in ruta]
    plt.plot(xs, ys, linewidth=3, marker="o", color="green")
    plt.text(inicio[1], filas - 1 - inicio[0], " I ", ha="center", va="center", weight="bold")
    plt.text(meta[1], filas - 1 - meta[0], " M ", ha="center", va="center", weight="bold")
    plt.title("Problema 2: laberinto (I = inicio, M = meta)")
    plt.xticks(range(columnas)); plt.yticks(range(filas))
    plt.grid(True); plt.gca().set_aspect("equal")
    plt.tight_layout()
    plt.savefig("grafo_laberinto_generado.png", dpi=180)
    plt.close()


if __name__ == "__main__":
    problema_rutas()
    problema_laberinto()