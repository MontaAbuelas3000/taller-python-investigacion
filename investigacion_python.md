# Investigación sobre Conceptos Básicos de Python

## 1. ¿Qué es una variable en Python?

Una **variable** es un espacio en memoria que almacena un valor.  
Sirve para guardar datos que pueden cambiar durante la ejecución del programa.

**Tipos de datos comunes:**
- Enteros (`int`)
- Decimales (`float`)
- Cadenas de texto (`str`)
- Booleanos (`bool`)

**Ejemplos válidos:**
```python
nombre = "Juan"
edad = 25
es_mayor = True

1nombre = "Juan"   # No puede iniciar con número
nombre-usuario = "Ana"  # No se usan guiones
class = 10   # No se puede usar palabras reservadas

2. Diferencia entre = y ==

= asigna un valor a una variable.

== compara dos valores.

Ejemplo:

x = 10        # Asignación
print(x == 10)  # True, comparación

3. ¿Qué es la indentación y por qué es importante?

La indentación son los espacios o tabulaciones al inicio de una línea de código.
En Python indica qué líneas pertenecen a un bloque (por ejemplo, dentro de un if o for).

Si no indentas bien, Python lanza un error:

if True:
print("Hola")  # Error: falta indentación

4. Diferencia entre ciclo for y while

for: se usa cuando se sabe cuántas veces se repetirá.

while: se usa cuando la condición depende de algo que cambia durante la ejecución.

Ejemplo for:

for i in range(5):
    print(i)


Ejemplo while:

x = 0
while x < 5:
    print(x)
    x += 1

5. ¿Qué hace la función range()?

range() genera una secuencia de números.

range(5) → 0, 1, 2, 3, 4

range(1, 10) → 1, 2, 3, 4, 5, 6, 7, 8, 9

range(0, 10, 2) → 0, 2, 4, 6, 8 (el último valor es el paso)

Se usa normalmente en bucles for para repetir acciones.

