# Investigación Git Básico

## 1. ¿Qué es el "staging area" o "índice" en Git y para qué sirve?

El **staging area** (también llamado *índice*) es una zona intermedia entre tu **working directory**
(y donde editas los archivos) y el **repository** (donde se almacenan los commits). Sirve para
seleccionar exactamente qué cambios incluir en el próximo commit usando `git add`.

- **Working directory:** Tu carpeta local con los archivos que editás.
- **Staging area:** Lista de cambios preparados para el siguiente commit.
- **Repository:** Histórico de commits (la base de datos de Git).

Tener esta área intermedia permite controlar y agrupar cambios lógicos, evitar subir cosas
incompletas o archivos temporales, y construir commits claros.

## 2. ¿Qué hace el comando `git status` y por qué usarlo frecuentemente?

`git status` indica el estado del repo: en qué rama estás, qué archivos están modificados,
cuáles están en staging y cuáles son nuevos (untracked). Es fundamental para no equivocarse
al commitear.

Al menos 3 tipos de información que provee:
1. La **rama** actual (ej. `On branch main`).
2. Archivos **untracked** (nuevos, no añadidos).
3. Archivos **staged** listos para commit y archivos **modificados** pero no staged.

## 3. Diferencia entre `git fetch` y `git pull`

- `git fetch`: descarga los cambios del remoto pero **no los fusiona** con tu rama local.
  Sirve para revisar cambios antes de aplicarlos.
- `git pull`: hace `fetch` + `merge` (o `rebase`), descarga y fusiona automáticamente en tu rama.

**Cuándo usar:**
- `git fetch` si querés revisar primero (más seguro).
- `git pull` si querés actualizar tu rama directo y estás seguro.

`git fetch` es más seguro porque evita mezclar cambios sin revisarlos.

## 4. ¿Qué es un "merge conflict" y cómo se resuelve?

Un *merge conflict* ocurre cuando Git no puede decidir automáticamente qué versión conservar
porque dos ramas cambiaron la misma parte de un archivo.

**Ejemplo:** cambiás la misma línea de `README.md` en `main` y en `desarrollo`.
