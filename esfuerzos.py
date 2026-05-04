import math

def calcular_esfuerzos():
    # --- INTRODUCCIÓN ---
    print("-" * 65)
    print("  ALGORITMO PARA CÁLCULO DE ESFUERZO NORMAL (FLEXIÓN BIAXIAL)")
    print("-" * 65)
    print("Este programa calcula el esfuerzo normal total en los puntos")
    print("críticos de las secciones L, I y Circular de la Tabla 1.")
    print("Funcionamiento: Seleccione el caso y proporcione dimensiones en metros.")
    print("-" * 65)

    # --- SELECCIÓN DE CASO ---
    print("Seleccione el caso a analizar:")
    print("a. Perfil en L")
    print("b. Perfil en I")
    print("c. Sección Circular Hueca")
    opcion = input("Ingrese su opción (a, b o c): ").lower()

    # Datos de carga constantes (según el problema)
    Mx = 100.0
    My = 50.0

    # --- LÓGICA DE CÁLCULO ---
    if opcion in ['a', 'b', 'c']:
        print("\n--- Entrada de Geometría (Unidades en METROS) ---")
        
        if opcion == 'a': # Caso L
            b = float(input("Ancho de la base (b): "))
            h = float(input("Altura total (h): "))
            t = float(input("Espesor (t): "))
            
            # Centroide e Inercia (Teorema de Ejes Paralelos)
            A1, A2 = t * h, (b - t) * t
            x1, y1 = t/2, h/2
            x2, y2 = t + (b - t)/2, t/2
            Xb = (A1*x1 + A2*x2)/(A1+A2)
            Yb = (A1*y1 + A2*y2)/(A1+A2)
            Ix = ((t*h**3)/12 + A1*(y1-Yb)**2) + (((b-t)*t**3)/12 + A2*(y2-Yb)**2)
            Iy = ((h*t**3)/12 + A1*(x1-Xb)**2) + ((t*(b-t)**3)/12 + A2*(x2-Xb)**2)
            
            puntos = {'a': (0-Xb, h-Yb), 'b': (t-Xb, h-Yb), 'h': (0-Xb, 0-Yb), 'j': (b-Xb, 0-Yb)}

        elif opcion == 'b': # Caso I
            b = float(input("Ancho de patines (b): "))
            h = float(input("Altura total (h): "))
            t = float(input("Espesor (t): "))
            
            Ix = (b * h**3)/12 - ((b-t)*(h-2*t)**3)/12
            Iy = (2 * t * b**3 / 12) + ((h - 2*t) * t**3 / 12)
            
            puntos = {'a': (-b/2, h/2), 'c': (b/2, h/2), 'h': (0, 0), 'n': (-b/2, -h/2), 'o': (b/2, -h/2)}

        elif opcion == 'c': # Caso Circular
            r_int = float(input("Radio interno (r_int): "))
            t = float(input("Espesor de pared (t): "))
            
            r_ext = r_int + t
            I_c = (math.pi/4) * (r_ext**4 - r_int**4)
            Ix = Iy = I_c
            
            puntos = {'a': (0, r_ext), 'c': (-r_ext, 0), 'f': (r_ext, 0), 'h': (0, -r_ext)}

        # --- MOSTRAR RESULTADOS ---
        print("\n" + "="*50)
        print(f"{'PUNTO':<10} | {'ESFUERZO NORMAL TOTAL (Pa)':<25}")
        print("-" * 50)
        for p, coord in puntos.items():
            x, y = coord
            # Fórmula de flexión biaxial
            sigma = -(Mx * y / Ix) + (My * x / Iy)
            print(f"Punto {p:<5} | {sigma:>25.2f}")
        print("="*50)
        print("Nota: (+) Tensión | (-) Compresión")

    else:
        print("Opción no válida. Reinicie el programa.")

if __name__ == "__main__":
    calcular_esfuerzos()
