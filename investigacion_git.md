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


# Investigación GitHub y Colaboración

## 1. ¿Qué es un Pull Request (PR) y cuál es su propósito?

Un **Pull Request (PR)** es una solicitud que un colaborador envía para que sus cambios sean revisados e integrados a la rama principal de un proyecto (por ejemplo, `main`).  
Su propósito es **permitir revisión, comentarios y aprobación** antes de fusionar el código.

**Diferencia con un merge directo:**  
- Un *merge* directo mezcla los cambios sin revisión previa.  
- Un *pull request* permite revisar, discutir y aprobar antes de mezclar.

**Ventajas:**
- Permite control de calidad antes de integrar el código.  
- Facilita la colaboración entre varios programadores.  
- Mantiene un historial claro de qué se cambió y por qué.

---

## 2. ¿Qué es un fork en GitHub y cuándo se usa?

Un **fork** es una copia completa de un repositorio de otra persona en tu propia cuenta.  
Se usa cuando quieres **contribuir a un proyecto sin afectar el original**.

**Diferencia entre fork y clone:**
- *Fork:* se hace en GitHub, crea una copia en la nube (tu perfil).  
- *Clone:* descarga el repositorio a tu computador local.

**Cómo contribuir a un proyecto open source:**
1. Haces un *fork* del repo original.  
2. Clonas tu fork a tu PC.  
3. Creas una rama, haces tus cambios y commits.  
4. Subes la rama y creas un *Pull Request* al repo original.  

---

## 3. ¿Qué es el archivo `.gitignore` y por qué es importante?

El archivo **`.gitignore`** le dice a Git qué archivos o carpetas **no deben incluirse** en los commits ni subirse al repositorio.  
Es esencial para evitar subir archivos innecesarios, sensibles o pesados.

**Ejemplos de archivos que no deben subirse en proyectos Python:**
1. `__pycache__/`
2. Archivos `.pyc`
3. Carpetas de entorno virtual: `venv/` o `env/`
4. Archivos temporales de VS Code: `.vscode/`
5. Archivos de configuración local: `.env`, `.DS_Store`

**Problemas si no usas `.gitignore`:**
- Repositorios pesados e innecesarios.  
- Posibles fugas de contraseñas o claves API.  
- Conflictos entre equipos por archivos locales.

---

## 4. ¿Qué son los issues en GitHub y para qué sirven?

Los **issues** son herramientas para **reportar errores, proponer mejoras o hacer preguntas** dentro del proyecto.  
Sirven como una lista pública de tareas o problemas pendientes.

**Un buen issue debe incluir:**
- Título descriptivo.  
- Descripción del problema o propuesta.  
- Pasos para reproducir el error (si aplica).  
- Etiquetas (`bug`, `enhancement`, `help wanted`).  
- Asignación (quién lo resolverá).

**Relacionar issues con commits:**  
Puedes referenciar un issue desde un commit o PR usando el número con `#`.  
Ejemplo:  
> “fix: corregir error en login (#12)”  
GitHub cerrará automáticamente el issue #12 al fusionar el commit.

---

## 5. ¿Qué es GitHub Actions y para qué se utiliza?

**GitHub Actions** es una herramienta de **automatización de tareas** dentro de GitHub.  
Permite ejecutar scripts o flujos de trabajo (workflows) automáticamente cuando ocurre algo (como un push, pull request o release).

**Se usa para:**
- Integración continua (CI): probar código automáticamente.  
- Despliegue continuo (CD): publicar tu app o sitio web tras cada actualización.

**Ejemplos de tareas automatizables:**
1. Ejecutar pruebas con `pytest` cada vez que alguien haga un push.  
2. Construir y desplegar el proyecto en un servidor o en GitHub Pages.  


# Investigación sobre Buenas Prácticas y Comandos Avanzados en Git

## 1. Git Rebase vs Git Merge
- **Merge:** combina ramas creando un nuevo commit de fusión.  
- **Rebase:** reescribe la historia moviendo commits al final de otra rama.

Usa **merge** en trabajo colaborativo, y **rebase** para mantener un historial limpio.

“Reescribir la historia” significa cambiar el orden o los hashes de commits existentes.

---

## 2. git stash
Guarda temporalmente tus cambios sin hacer commit.

**Ejemplo:**
```bash
git stash
git pull origin main
git stash pop
Sirve cuando necesitas cambiar de rama sin perder el trabajo actual.

3. Commits convencionales
Mensajes estructurados que indican el tipo de cambio:

feat: nueva funcionalidad

fix: corrección

docs: documentación

refactor: reestructuración

style: formato

test: pruebas

Ayudan a mantener orden y generar changelogs automáticos.

4. Git Flow
Estrategia de ramas:

main → producción

develop → desarrollo

feature/ → nuevas funciones

release/ → versiones

hotfix/ → parches urgentes

