



# Playwright

Módulo con funcionalidades avanzadas para el navegador que utiliza Playwright en lugar de Selenium

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.


## Overview


1. Abrir Navegador
Abre una nueva instancia del navegador.

2. Ir a URL
Navegar hacia una URL y esperar hasta que ocurra el evento seleccionado.

3. Cerrar navegador
Cerrar el navegador y todas las pestañas, y guarda el estado del perfil.

4. Esperar a Objeto
Esperar a que un elemento esté en cierto estado.

5. Click en objeto
Hacer click en un elemento.

6. Limpiar input y enviar Texto
Elimina el contenido de un objeto input y envía el texto.

7. Extraer Texto Playwright
Obtener el texto interno de un elemento.

8. Tomar Captura
Tomar una captura de pantalla de la página.

9. Descargar
Permite hacer click en un botón para descargar un elemento.

10. Seleccionar Opción
Selecciona una o varias opciones en un elemento desplegable.

11. Enviar combinacion de teclas
Comando para atajos de teclado al elemento activo. Atajos que no sean de la pagina web, sino que sean del navegador y del sistema no estan soportados. 

12. Marcar / Desmarcar
Marcar o desmarcar la casilla.

13. Obtener Atributo
Obtener el valor de un atributo.

14. Esperar estado de carga
Esperar hasta que la página alcance un estado de carga requerido.

15. Obtener títulos de pestañas
Devuelve una lista con los títulos de todas las pestañas abiertas en el navegador.

16. Cambiar pestaña por título
Cambiar a una pestaña por su título en el contexto actual.

17. Evaluar JS.
Evalua JS en el contexto de la página. Retorna el resultado de la ejecución.

18. Contar elementos
Contar cuántas veces aparece un elemento en la página.

19. Cambiar a IFRAME
Cambia a un IFRAME y establece su contenido como predeterminado.

20. Cambiar a contenido del body
Deja el contenido del body de la página como contenido por defecto.




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**playwright**](https://pypi.org/project/playwright/)
### License

![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)
[MIT](https://opensource.org/license/mit)