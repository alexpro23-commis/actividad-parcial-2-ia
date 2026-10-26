"""
ACTIVIDAD 3 — BÚSQUEDA LOCAL

"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# Dominio acotado: -5 <= x <= 5.
# Función con varios mínimos locales para mostrar la diferencia entre métodos.
def objetivo(x):
    return (x - 3)**2 + 0.15 * math.sin(5*x) + 0.1 * math.sin(11*x)


def hill_climbing(x_inicial=-4.5, iteraciones=800, paso=0.08, semilla=17):
    """Solo acepta movimientos que mejoran el valor objetivo."""
    rng = random.Random(semilla)
    x = x_inicial
    valor = objetivo(x)
    mejor_x, mejor_valor = x, valor
    historial = []

    for _ in range(iteraciones):
        direccion = rng.choice([-1, 1])
        candidato = max(-5.0, min(5.0, x + direccion * paso))
        valor_candidato = objetivo(candidato)

        # Minimización: aceptar únicamente si el candidato es mejor.
        if valor_candidato < valor:
            x, valor = candidato, valor_candidato

        if valor < mejor_valor:
            mejor_x, mejor_valor = x, valor
        historial.append(mejor_valor)

    return mejor_x, mejor_valor, historial


def simulated_annealing(x_inicial=-4.5, iteraciones=800, temperatura_inicial=1.0,
                        enfriamiento=0.992, paso=0.25, semilla=17):
    """Puede aceptar movimientos peores al principio para escapar de mínimos locales."""
    rng = random.Random(semilla)
    x = x_inicial
    valor = objetivo(x)
    mejor_x, mejor_valor = x, valor
    historial = []
    temperatura = temperatura_inicial

    for _ in range(iteraciones):
        candidato = max(-5.0, min(5.0, x + rng.uniform(-paso, paso)))
        valor_candidato = objetivo(candidato)
        diferencia = valor_candidato - valor

        # Si empeora, se acepta con probabilidad exp(-diferencia / temperatura).
        if diferencia < 0 or rng.random() < math.exp(-diferencia / max(temperatura, 1e-12)):
            x, valor = candidato, valor_candidato

        if valor < mejor_valor:
            mejor_x, mejor_valor = x, valor
        historial.append(mejor_valor)
        temperatura *= enfriamiento

    return mejor_x, mejor_valor, historial


def main():
    iteraciones = 800
    x_hc, f_hc, hist_hc = hill_climbing(iteraciones=iteraciones)
    x_sa, f_sa, hist_sa = simulated_annealing(iteraciones=iteraciones)

    # Aproximación de referencia por evaluación densa de la función.
    xs = np.linspace(-5, 5, 20001)
    ys = [objetivo(float(x)) for x in xs]
    indice = int(np.argmin(ys))
    x_ref, f_ref = float(xs[indice]), float(ys[indice])

    print("ACTIVIDAD 3 — RESULTADOS DE BÚSQUEDA LOCAL")
    print(f"Hill Climbing: x={x_hc:.5f}, f(x)={f_hc:.6f}")
    print(f"Simulated Annealing: x={x_sa:.5f}, f(x)={f_sa:.6f}")
    print(f"Referencia en malla: x={x_ref:.5f}, f(x)={f_ref:.6f}")

    plt.figure(figsize=(9, 5))
    plt.plot(range(1, iteraciones + 1), hist_hc, label="Hill Climbing")
    plt.plot(range(1, iteraciones + 1), hist_sa, label="Simulated Annealing")
    plt.axhline(f_ref, linestyle="--", label="Referencia en malla")
    plt.xlabel("Iteración")
    plt.ylabel("Mejor valor de f(x)")
    plt.title("Convergencia de los algoritmos")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafica_convergencia_actividad3.png", dpi=180)
    plt.show()

    plt.figure(figsize=(7, 4))
    plt.bar(["Hill Climbing", "Simulated Annealing", "Referencia"], [f_hc, f_sa, f_ref])
    plt.ylabel("Valor objetivo (menor es mejor)")
    plt.title("Comparación de resultados finales")
    plt.grid(axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig("comparacion_resultados_actividad3.png", dpi=180)
    plt.show()


if __name__ == "__main__":
    main()
