



# Playwright

Módulo con funcionalidades avanzadas para el navegador que utiliza Playwright en lugar de Selenium

*Read this in other languages: [English](Manual_Playwright.md), [Português](Manual_Playwright.pr.md), [Español](Manual_Playwright.es.md)*

![banner](imgs/Banner_Playwright.jpg)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.



## Como usar este modulo
Este modulo es una alternativa a los otros modulos web como WebPro donde en vez de usar la librería Selenium, usa la librería Playwright. Debido a esto ultimo, va a tener que tener algunas cosas en cuenta:

1. Las dependencias del modulo no están incluidas en el modulo, y se descargarán automáticamente en la carpeta libs después de usar por primera vez algun comando.

2. Si las dependencias se actualizan en una futura versión del modulo, el usuario necesitará ejecutar el comando "Validar Librerías" con la opción de "Forzar descarga" habilitada para descargar las dependencias actualizadas.

3. La librería Playwright puede no funcionar si el usuario abre una nueva pestaña manualmente o usa el comando "Click en objeto" para hacer click en un botón o enlace que abre una nueva pestaña. Recomendamos usar el comando "Click link a nueva pestaña" para hacer click en dichos botones o enlaces. Si alguna pagina web abre una nueva pestaña sin siquiera hacer click, se 
recomienda usar el comando "Esperar a Objeto" para actualizar el estado de Playwright.

4. Es recomendable siempre cerrar el navegador usando el comando "Cerrar Navegador" para evitar posibles problemas al reutilizar una carpeta de perfil o una sesion.

5. Para dar clicks en botones o links que descargaran un archivo, es necesario utilizar el comando "Descargar". Sin este comando, sera imposible descargar archivos.

6. Para interactuar con un elemento dentro de un ShadowRoot, es necesario interactuar con este utilizando el tipo de selector `CSS`. Para obtener dicho selector, se necesita dar click derecho al elemento en el html de la pagina, seleccionar la opcion Copy y luego Copy selector. 

## Sobre el comando Open Chrome:
1. El comando "Open Chrome" abrirá una nueva instancia del navegador Chrome. Se creará una carpeta de perfil temporal para cada sesión que el usuario abra sin especificar una carpeta de perfil, y se eliminará cuando la sesión se cierre. Esto significa que cualquier 
dato, como cookies o historial de navegación, no se guardará después de que la sesión termine.

2. El comando solo puede abrir una instancia del navegador Chrome por cada carpeta de perfil, por lo que si deseas abrir múltiples instancias del navegador Chrome, se necesitara abrir cada instancia con una carpeta de perfil diferente. El navegador puede necesitar unos segundos después de cerrar para poder usar una carpeta de perfil que estaba en uso previamente.

## Sobre utilizar comandos de otros modulos Web en el navegador:
1. Es posible utilizar comandos de otros modulos Web como WebPro o el modulo nativo Web, utilizando el comando "Tomar Playwright" de WebPro. Este comando permite que dichos modulos web se conecten al puerto puesto en Puerto de Depuracion de Abrir Chrome.

2. Como el navegador fue abierto por Playwright, seguira siendo necesario el utilizar comandos como "Descargar" o "Click link a nueva pestaña" para descargar archivos o hacer click en botones o links que abren una 
nueva pestaña.

3. La forma en la que Playwright interactua con los iframes es diferente a la de otros modulos web. Esto signfica que, si se requiere entrar a un iframe y dentro de este  usar comandos tanto de Playwright, como de otro modulo, sera necesario entrar al iframe usando el respectivo comando de ambos modulos.


## Descripción de los comandos

### Abrir Chrome

Abre una nueva instancia de chrome.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|URL que se abrirá automáticamente una vez inicializado el navegador y la página.|https://rocketbot.com/es/|
|Ejecutable del navegador|Ruta del ejecutable de Google Chrome. Solo necesario si es que se usa dicho navegador.|C:/Program Files/Google/Chrome/Application/chrome.exe|
|Carpeta de perfil|Ruta de la carpeta de perfil de usuario usada por navegador. Si se deja vacio, se creara uno temporal que se borrara al iniciar nuevamente sin una carpeta de perfil o al usar el comando Cerrar navegador.|C:/folder/profile/|
|Servidor Proxy|Dirección del servidor proxy (ej., http//myproxy8080)|http://myproxy:8080|
|Usuario Proxy|Nombre de usuario para la autenticación del proxy|username|
|Contraseña Proxy|Contraseña para la autenticación del proxy|password|
|Modo Headless|Ejecutar el navegador en modo headless (sin GUI)||
|Puerto de Depuración|Permite que otros modulos web que utilizan Selenium tomen control del navegador. Esto se hace usando el comando Tomar Playwright del modulo Web Pro.|9222|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) para la carga de la URL inicial.|30|
|ID de Sesión|ID único para esta sesión de Playwright. Permite ejecutar múltiples navegadores o bots en paralelo sin interferencias entre sí.|1|

### Validar Librerías

Verifica si existen las librerías necesarias para el SO actual y permite forzar su descarga.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Forzar descarga|Si es marcada, eliminará las librerías existentes y las descargará de nuevo.||
|Asignar resultado a variable|Variable donde se almacenará el resultado del comando|Variable|

### Cerrar navegador

Cerrar el navegador y todas las pestañas, y guarda el estado del perfil.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Ir a URL

Navegar hacia una URL y esperar hasta que ocurra el evento seleccionado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|||
|Esperar hasta|Loaded Espera a que cargue toda la página, incluyendo imágenes y estilos.
DOMContentLoaded Espera a que aparezca la estructura HTML sin esperar a las imágenes.
Network Idle Espera a que la actividad de red se detenga por completo por 500ms.
Commit considera que la navegación ha terminado cuando se recibe la respuesta de red y el documento comenzó a cargarse.||
|Abrir en nueva pestaña|Si está marcado, abre la URL en una nueva pestaña en lugar de la actual.||
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Esperar a Objeto

Esperar a que un elemento esté en cierto estado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Estado|Estado a esperar||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que el objeto esté en el estado seleccionado.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Click en objeto

Hacer click en un elemento.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda hacer click en el elemento.|30|
|Forzar Click|Si se debe forzar la acción de click, incluso si el elemento no es visible o interactuable.||
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Limpiar input y enviar Texto

Elimina el contenido de un objeto input y envía el texto.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Texto a Escribir|||
|Tecla especial|Seleccione una tecla especial para apretar después del texto. (Opcional)|SPACE|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda escribir en el elemento.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Extraer Texto Playwright

Obtener el texto interno de un elemento.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda extraer el texto del elemento.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Tomar Captura

Tomar una captura de pantalla de la página.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la Carpeta||C:/Users/User/Downloads/|
|Nombre de Archivo|Nombre del archivo y extensión|screenshot.jpg|
|Página Completa|Marcar para capturar la página completa desplazable o solo la ventana gráfica.||
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Descargar

Permite hacer click en un botón para descargar un elemento.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a clickear.|Data|
|Tipo de Selector|||
|Carpeta de Guardado|Carpeta donde se guardará el archivo. Opcional.|C:/Users/User/Downloads/|
|Sobreescribir Nombre Archivo|Opcional. Si está vacío, usa el nombre original.|nombre_archivo|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda descargar el elemento.|60|
|Ruta del archivo|Variable para guardar la ruta final del archivo||
|Variable Nombre Archivo|Variable para guardar el nombre del archivo||
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Seleccionar Opción

Selecciona una o varias opciones en un elemento desplegable.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Opción|Seleccione las etiquetas, valores o índices de las opciones a elegir. Si es múltiple, enviar una lista ej [opción1, opción2].|opción1|
|Seleccionar la opción por|Selecciona para elegir la opción por su valor, etiqueta o índice.|Select by|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda seleccionar una opción del elemento.|30|

### Enviar combinacion de teclas

Comando para atajos de teclado al elemento activo. Atajos que no sean de la pagina web, sino que sean del navegador y del sistema no estan soportados. 
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Primera tecla especial|Primer tecla especial a combinar con una letra/numero y/o con una segunda tecla especial|SPACE|
|Segunda tecla especial|Segunda tecla especial a combinar con la primera tecla de ser necesario.|SPACE|
|Letra o numero|Letra o numero a combinar con las teclas especiales de ser necesario.|a|
|ID de Sesión|ID único para esta sesión de Playwright|4|

### Marcar / Desmarcar

Marcar o desmarcar la casilla.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Marcar o desmarcar|Marcar o desmarcar la casilla.||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que el elemento pueda ser marcado / desmarcado.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Obtener Atributo

Obtener el valor de un atributo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Nombre del atributo|Nombre del atributo cuyo valor se quiere obtener.|value|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda obtener el atributo del elemento.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Esperar estado de carga

Esperar hasta que la página alcance un estado de carga requerido.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Estado de carga|Loaded Espera a que cargue toda la página, incluyendo imágenes y estilos.
DOMContentLoaded Espera a que aparezca la estructura HTML sin esperar a las imágenes.
 Network Idle Espera a que la actividad de red se detenga por completo por 500ms.|Load|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que la página alcance el estado de carga requerido.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Obtener títulos de pestañas

Devuelve una lista con los títulos de todas las pestañas abiertas en el navegador.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado del comando|Variable|

### Cambiar pestaña por título

Cambiar a una pestaña por su título en el contexto actual.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Título|Título de la pestaña a la que se desea cambiar|Variable|

### Evaluar JS.

Evalua JS en el contexto de la página. Retorna el resultado de la ejecución.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Codigo de JS|Código JS a evaluar en el contexto de la página. Retorna el resultado de la ejecución.|function(data) {
	return param1 * param2;
}|
|Parametros de la función|Lista de valores de los parámetros que se le pasará a la función. Los valores de la lista se pasan como cadenas.|[value1, value2, ...]|
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado del codigo JS|Variable|

### Contar elementos

Contar cuántas veces aparece un elemento en la página.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector de los elementos a seleccionar.|Data|
|Tipo de Selector|||
|ID de Sesión|ID único para esta sesión de Playwright|1|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Cambiar a IFRAME

Cambia a un IFRAME y establece su contenido como predeterminado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del Iframe.|Data|
|Tipo de Selector|||
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Cambiar a contenido del body

Deja el contenido del body de la página como contenido por defecto.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Click link a nueva pestaña

Hacer click en un elemento que abrirá una nueva pestaña.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda hacer click en el elemento.|30|
|Esperar hasta|Loaded Espera a que cargue toda la página, incluyendo imágenes y estilos.
DOMContentLoaded Espera a que aparezca la estructura HTML sin esperar a las imágenes.
Network Idle Espera a que la actividad de red se detenga por completo por 500ms.||
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Subir Archivo

Comando para subir uno o más archivos a un input de tipo file. Solo completar un unico valor según cuántos archivos se deseen subir.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Subir Archivo|Seleccionamos los archivos a subir|C:/Users/user/file1.pdf|
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda hacer click en el elemento.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Interactuar con alerta

Interactua con una alerta en la pagina. Se la puede aceptar o rechazar.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de Selector|||
|Interaccion con alerta|||
|Tiempo de espera (seg)|Tiempo máximo de espera (en segundos) hasta que se pueda hacer click en el elemento.|30|
|ID de Sesión|ID único para esta sesión de Playwright|1|

### Imprimir como PDF

Imprimir la página como PDF en Chrome. El PDF se genera en base al contenido disponible de la página. No representa una copia fiel del sitio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta y nombre del Archivo|Seleccionamos la ruta y el nombre del archivo a guardar, sin la extension .pdf|path/to/file.pdf|
|Formato de Hoja|Seleccione el formato de hoja para el PDF.||
|Modo Paisaje|Marcar para descargar el pdf en modo paisaje (horizontal).|True|
|ID de Sesión|ID único para esta sesión de Playwright|1|
