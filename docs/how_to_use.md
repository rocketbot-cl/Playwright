## How to use this module
This module is an alternative to the other web modules like WebPro where instead of using the Selenium library, it uses the Playwright library.

1. The modules depedencies are not included in the module, and they will be automatically downloaded in the libs folder after using any command for the first time.

2. If the dependencies are updated in a future version of the module, the user will need to run the command "Check Libraries" with the force download option enabled to download the updated dependencies.

3. The Playwright library may not work if the user opens a new tab manually or uses the "Click on object" command to click a button or link that opens a new tab. We recommend using the "Click link to new tab" command to click on such buttons or links. If any webpage opens a new tab without even clicking, it is recommended to use the "Wait For Object" command to update Playwright's state.

4. It is recommended to always close the browser using the "Close Browser" command to avoid possible issues when reusing a profile folder or a session.

5. To click on buttons or links that will download a file, it is necessary to use the "Download" command. Without this command, it will be impossible to download files.

6. To interact with an element inside a ShadowRoot, it is necessary to interact with it using the `CSS` selector type. To obtain such selector, you need to right click on the element in the webpage's html, select the Copy option and then Copy selector.

## About the Open Chrome command:
1. The command "Open Chrome" will open a new instance of the Chrome browser. A temporary profile folder will be created for each session the users opens without specifying a profile folder, and it will be deleted when the session is closed. This means that any data, such as cookies or browsing history, will not be saved after the session ends.

2. The command can only open an instance of the Chrome browser per each profile folder, so if you want to open multiple instances of the Chrome browser, you will to open each instance with a different profile folder. The browser may need a few seconds after closing to be able to use a profile folder that was previously in use.

## About using commands from other Web modules in the browser:
1. It is possible to use commands from other Web modules like WebPro or the native Web module, using the "Take Playwright" command from WebPro. This command allows such web modules to connect to the port set in Open Chrome's Debugging Port.

2. Since the browser was opened by Playwright, it will still be necessary to use commands like "Download" or "Click link to new tab" to download files or click on buttons or links that open a new tab.

3. The way Playwright interacts with iframes is different from other web modules. This means that if you need to enter an iframe and within it use commands from both Playwright and another module, you will need to enter the iframe using the respective command from both modules.

---

## Como usar este modulo
Este modulo es una alternativa a los otros modulos web como WebPro donde en vez de usar la librería Selenium, usa la librería Playwright. Debido a esto ultimo, va a tener que tener algunas cosas en cuenta:

1. Las dependencias del modulo no están incluidas en el modulo, y se descargarán automáticamente en la carpeta libs después de usar por primera vez algun comando.

2. Si las dependencias se actualizan en una futura versión del modulo, el usuario necesitará ejecutar el comando "Validar Librerías" con la opción de "Forzar descarga" habilitada para descargar las dependencias actualizadas.

3. La librería Playwright puede no funcionar si el usuario abre una nueva pestaña manualmente o usa el comando "Click en objeto" para hacer click en un botón o enlace que abre una nueva pestaña. Recomendamos usar el comando "Click link a nueva pestaña" para hacer click en dichos botones o enlaces. Si alguna pagina web abre una nueva pestaña sin siquiera hacer click, se recomienda usar el comando "Esperar a Objeto" para actualizar el estado de Playwright.

4. Es recomendable siempre cerrar el navegador usando el comando "Cerrar Navegador" para evitar posibles problemas al reutilizar una carpeta de perfil o una sesion.

5. Para dar clicks en botones o links que descargaran un archivo, es necesario utilizar el comando "Descargar". Sin este comando, sera imposible descargar archivos.

6. Para interactuar con un elemento dentro de un ShadowRoot, es necesario interactuar con este utilizando el tipo de selector `CSS`. Para obtener dicho selector, se necesita dar click derecho al elemento en el html de la pagina, seleccionar la opcion Copy y luego Copy selector. 

## Sobre el comando Open Chrome:
1. El comando "Open Chrome" abrirá una nueva instancia del navegador Chrome. Se creará una carpeta de perfil temporal para cada sesión que el usuario abra sin especificar una carpeta de perfil, y se eliminará cuando la sesión se cierre. Esto significa que cualquier dato, como cookies o historial de navegación, no se guardará después de que la sesión termine.

2. El comando solo puede abrir una instancia del navegador Chrome por cada carpeta de perfil, por lo que si deseas abrir múltiples instancias del navegador Chrome, se necesitara abrir cada instancia con una carpeta de perfil diferente. El navegador puede necesitar unos segundos después de cerrar para poder usar una carpeta de perfil que estaba en uso previamente.

## Sobre utilizar comandos de otros modulos Web en el navegador:
1. Es posible utilizar comandos de otros modulos Web como WebPro o el modulo nativo Web, utilizando el comando "Tomar Playwright" de WebPro. Este comando permite que dichos modulos web se conecten al puerto puesto en Puerto de Depuracion de Abrir Chrome.

2. Como el navegador fue abierto por Playwright, seguira siendo necesario el utilizar comandos como "Descargar" o "Click link a nueva pestaña" para descargar archivos o hacer click en botones o links que abren una nueva pestaña.

3. La forma en la que Playwright interactua con los iframes es diferente a la de otros modulos web. Esto signfica que, si se requiere entrar a un iframe y dentro de este  usar comandos tanto de Playwright, como de otro modulo, sera necesario entrar al iframe usando el respectivo comando de ambos modulos.

---

## Como usar este módulo
Este módulo é uma alternativa a outros módulos web, como o WebPro, onde, em vez de usar a biblioteca Selenium, usa a biblioteca Playwright.

1. As dependências do módulo não estão incluídas no módulo, e serão baixadas automaticamente na pasta libs após usar qualquer comando pela primeira vez.

2. Se as dependências forem atualizadas em uma versão futura do módulo, o usuário precisará executar o comando "Verificar Bibliotecas" com a opção de forçar download habilitada para baixar as dependências atualizadas.

3. A biblioteca Playwright pode não funcionar se o usuário abrir uma nova guia manualmente ou usar o comando "Clique no objeto" para fazer click em um botão ou link que abre uma nova guia. Recomendamos usar o comando "Clicar em link para nova aba" para fazer click em tais botões ou links. Se alguma página da web abrir uma nova guia sem nem mesmo clicar, é recomendado usar o comando "Esperar por Objeto" para atualizar o estado do Playwright.

4. É recomendado sempre fechar o navegador usando o comando "Fechar Navegador" para evitar possíveis problemas ao reutilizar uma pasta de perfil ou uma sessão.

5. Para clicar em botões ou links que baixarão um arquivo, é necessário usar o comando "Baixar". Sem este comando, será impossível baixar arquivos.

6. Para interagir com um elemento dentro de um ShadowRoot, é necessário interagir com ele usando o tipo de seletor `CSS`. Para obter tal seletor, você precisa clicar com o botão direito do mouse no elemento no html da página, selecionar a opção Copiar e depois Copiar seletor.

## Sobre o comando Open Chrome:
1. O comando "Abrir Chrome" abrirá uma nova instância do navegador Chrome. Uma pasta de perfil temporária será criada para cada sessão que o usuário abrir sem especificar uma pasta de perfil, e será excluída quando a sessão for fechada. Isso significa que quaisquer dados, como cookies ou histórico de navegação, não serão salvos após o término da sessão.

2. O comando só pode abrir uma instância do navegador Chrome por cada pasta de perfil, então, se você quiser abrir várias instâncias do navegador Chrome, precisará abrir cada instância com uma pasta de perfil diferente. O navegador pode precisar de alguns segundos após o fechamento para poder usar uma pasta de perfil que estava em uso anteriormente.

## Sobre usar comandos de outros módulos Web no navegador:
1. É possível usar comandos de outros módulos Web, como WebPro ou o módulo Web nativo, usando o comando "Pegar Playwright" do WebPro. Este comando permite que tais módulos web se conectem à porta definida no Debugging Port do Open Chrome.

2. Como o navegador foi aberto pelo Playwright, ainda será necessário usar comandos como "Baixar" ou "Clicar em link para nova aba" para baixar arquivos ou clicar em botões ou links que abrem uma nova aba.

3. A forma como o Playwright interage com iframes é diferente de outros módulos web. Isso significa que, se você precisar entrar em um iframe e dentro dele usar comandos tanto do Playwright quanto de outro módulo, será necessário entrar no iframe usando o respectivo comando de ambos os módulos.