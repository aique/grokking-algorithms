# Algoritmos

Estos programas/apuntes han sido realizados para seguir los contenidos del libro Grokking Algorithms.

## Estructuras de datos y complejidades

### Arrays

Colecciones contiguas de elementos con un tamaño limitado, donde el acceso a una posición concreta es inmediato pero la
inserción y el borrado pueden llegar a tener un coste de O(n) debido a la reubicación de elementos.

### Listas enlazadas

Colecciones de elementos donde cada uno de ellos tiene un enlace al siguiente. Dado que no hay un espacio que gestionar,
las inserciones y los borrados son inmediatos, sin embargo el acceso a un elemento en concreto ha de hacerse recorriendo
la colección desde el principio.

Típicamente cuentan con un puntero para acceder directamente al primer y al último elemento de la colección.

### Tablas hash

Colecciones de elementos donde el espacio reservado es autogestionado por la estructura de datos y la posición de cada
elemento dentro de esta colección se determina por una `función hash`.

De esta manera en función de un identificador se asigna una posición única dentro del espacio reservado, el cual aumenta
o disminuye en función de la ocupación.

Se consigue que las operaciones sean inmediatas tanto en el acceso directo a un
elemento como en la inserción y borrado.

### Complejidades

A continuación se muestran las complejidades de distintas operaciones básicas sobre las estructuras mencionadas:

![data structures](./doc/data_structures.jpg)

## Métricas de evaluación

A continuación se adjunta una tabla con la estimación en tiempo de las complejidades más populares:

![big o notation](./doc/big_o_notation.png)

En cuando a la notación, cabe destacar que en caso de una complejidad ` O(n)`, el coste real en tiempo es `c*n`, siendo
`c` una cantidad determinada de tiempo que se requiere en cada paso.

A este valor se le llama `constante`. Generalmente suele ser ignorada ya que no es determinante en la mayoría de casos,
salvo en alguna excepción que se verá más adelante, al evaluar la eficiencia del algoritmo `quicksort`. 

## Estrategias de resolución

### Recursión

Las funciones recursivas constan de al menos dos elementos, el caso base y el caso recursivo.

El caso base cuando se trata de colecciones suele referirse a cuando éstas tienen ninguno o un elemento. En caso de no tener claro cual puede ser el caso base en un algoritmo, probar estas opciones primero.

### Divide y vencerás

Uno de los ejemplos del uso de esta técnica es la ordenación denominada `quicksort`.

#### Quicksort

En el caso peor, su complejidad puede ser cuadrática, pero en el caso medio su complejidad es `O(n*log n)`, siendo tan
óptima como la alcanzada en el algoritmo `mergesort`.

El caso medio mencionado se alcanzará siempre que el elemento seleccionado como `pivot` sea un elemento aleatorio de la
colección.

Dado que la constante de este algoritmo es más baja que en `mergesort`, esto le convierte en el algoritmo de ordenación
más eficiente.

### Grafos

Muchos problemas se pueden representar utilizando esta estructura.

#### Búsqueda en anchura

Permite dar respuesta a las cuestiones:

- ¿Hay un camino desde un nodo hasta otro?
- ¿Cuál es el camino más corto desde un nodo hasta otro?

#### Algoritmo de Dijkstra

Se utiliza en caso de que las conexiones entre nodos tengan un peso.

Es capaz de determinar el peso menor y el camino a seguir para conseguir llegar a un determinado nodo desde otro.

No se puede aplicar en los siguientes casos:

- Cuando existan pesos negativos, en ese caso utilizar el algoritmo `Bellman-Ford`.
- Cuando existan ciclos entre dos nodos (desde un nodo A existe una conexión directa con otro nodo B y viceversa).

### Algoritmos devoradores

Se basa en el principio de obtener la solución óptima a cada paso, componiendo una solución final que aunque puede no
ser la solución óptima, se aproxima mucho a ella con buenos rendimientos.

### Programación dinámica

La programación dinámica descompone el problema en otros más sencillos, buscando la solución óptima para ellos y
componiendo finalmente la solución óptima para el problema general.

Un ejemplo clásico es el problema de la mochila, donde hay un conjunto de objetos con un peso y un valor, que hay que
introducir en una mochila, sin rebasar su capacidad pero maximizando el valor introducido en ella.

Mientras que los algoritmos devoradores pueden no alcanzar la solución óptima, ésta sí se podría conseguir utilizando
esta técnica.

La resolución implica la composición de una tabla, donde cada celda es un suproblema. Será necesario alcanzar la manera
de descomponer el problema en estos subproblemas y determinar el algoritmo que a partir de ella obtiene la solución
óptima.   

## Problemas NP-Completos

Este tipo de problemas no tienen una forma de alcanzar una solución óptima en un tiempo computacional razonable.

Un ejemplo es el "problema del viajante", a cuya solución óptima se alcanzaría con una complejidad factorial, siendo
computacionalmente demasiado costoso de alcanzar cuando el número de nodos aumenta.

La mejor estrategia para su resolución es adoptar una solución aproximada con un coste computacional razonable, por
ejemplo utilizando un algoritmo devorador.
