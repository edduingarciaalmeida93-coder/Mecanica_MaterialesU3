# Análisis de Esfuerzo Normal por Flexión Biaxial

## Descripción del Proyecto
Este repositorio contiene un algoritmo desarrollado en **Python** para el cálculo y análisis de esfuerzos normales totales en perfiles estructurales sometidos a momentos flectores en dos ejes ($M_x$ y $M_y$). 

El proyecto permite automatizar el cálculo de propiedades mecánicas y esfuerzos para tres tipos de secciones transversales:
1. **Caso A:** Perfil en L (Ángulo de lados iguales/desiguales).
2. **Caso B:** Perfil en I (Viga estructural).
3. **Caso C:** Sección Circular Hueca (Tubería).

## Características del Algoritmo
* **Entrada Dinámica:** El usuario ingresa las dimensiones directamente en metros (m).
* **Cálculo Automático de Inercia:** Aplica el Teorema de Ejes Paralelos para obtener $I_x$ e $I_y$ según la geometría.
* **Análisis de Puntos Críticos:** Determina el esfuerzo total en las coordenadas más alejadas del eje neutro.
* **Interfaz de Consola:** Presenta los resultados en una tabla organizada para facilitar su interpretación académica.

## Fundamento Teórico
El cálculo se basa en la superposición de efectos de flexión simple:

$$σ = -\frac{M_x \cdot y}{I_x} + \frac{M_y \cdot x}{I_y}$$

Donde:
* **$σ$**: Esfuerzo normal total (Pa).
* **$M_x, M_y$**: Momentos flectores aplicados (Nm).
* **$x, y$**: Coordenadas del punto respecto al centroide (m).
* **$I_x, I_y$**: Momentos de inercia de la sección (m⁴).

## Requisitos
* Python 3.7 o superior.
* Biblioteca estándar `math`.

## Integrantes del Equipo (ITSC)
CARPIZO ALEJANDRO ALAN JAVIER.
COLORADO ROMERO LUIS ANGEL.
GARCIA ALMEIDA EDDUIN JAVIER.
IZQUIERDO CORDOVA ROGELIO.
