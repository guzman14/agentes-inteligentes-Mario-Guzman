# agentes-inteligentes-Mario-Guzman
Hoja de Trabajo 

Este repositorio contiene la solución a varios problemas de agentes inteligentes, implementados en Python. Los problemas resueltos incluyen:
- Control de semáforo
- Buscador de objetos en una cuadrícula
- Diagnóstico simple con un sistema experto
- Recomendación de películas según género

A continuación, se describe cada uno de los problemas resueltos:

## 1. Agente Semafórico

Este agente controla un semáforo, cambiando su estado entre verde, amarillo y rojo, dependiendo del flujo del tráfico. El agente ajusta la duración de cada estado según el número de vehículos detectados. Para simular la detección de vehículos, el código utiliza condiciones y ajusta los tiempos de espera en función de la cantidad de vehículos.

**Funcionamiento:**
- El semáforo comienza en el estado verde.
- Si se detectan más vehículos, el semáforo permanece verde por más tiempo.
- Si no se detectan vehículos, el semáforo pasa rápidamente al estado amarillo y luego al rojo.

**Código:** [ver código](semaforo.py)

## 2. Agente Buscador de Objetos

Este agente se desplaza en una cuadrícula de 5x5, buscando un objeto colocado aleatoriamente. El agente avanza paso a paso hasta encontrar el objeto.

**Funcionamiento:**
- La cuadrícula es representada por una matriz.
- El agente se mueve hacia el objetivo (el objeto), paso a paso.
- El estado de la cuadrícula se imprime después de cada movimiento del agente.

**Código:** [ver código](buscador_objetos.py)

## 3. Sistema Experto para Diagnóstico Simple

Este sistema experto realiza diagnósticos básicos según los síntomas ingresados por el usuario. Utiliza reglas de diagnóstico basadas en condiciones.

**Funcionamiento:**
- El usuario ingresa los síntomas.
- El sistema aplica las reglas para identificar el diagnóstico.
- Dependiendo de los síntomas, se sugiere un diagnóstico básico.

**Código:** [ver código](sistema_experto.py)

## 4. Agente de Recomendación de Películas

Este agente recomienda una película según el género favorito del usuario. Utiliza un diccionario de películas organizadas por género (acción, comedia, drama, etc.).

**Funcionamiento:**
- El usuario ingresa su género favorito.
- El agente recomienda una película aleatoria dentro de ese género.
   
**Código:** [ver código](recomendador_peliculas.py)