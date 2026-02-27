



# Playwright

Módulo com funcionalidades avançadas para o navegador que utiliza Playwright em vez de Selenium

*Read this in other languages: [English](Manual_Playwright.md), [Português](Manual_Playwright.pr.md), [Español](Manual_Playwright.es.md)*

![banner](imgs/Playwright.jpg)
## Como instalar este módulo

Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.


## Descrição do comando

### Abrir Navegador

Abre uma nova instância do navegador.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Navegador |Navegador para abrir|Google Chrome|
|URL|URL que será aberta automaticamente uma vez que o navegador e a página forem inicializados.|https://rocketbot.com/pr/|
|Servidor Proxy|Endereço do servidor proxy (ex., http//meuproxy8080)|http://meuproxy:8080|
|Usuário Proxy|Nome de usuário para autenticação do proxy|usuário|
|Senha Proxy|Senha para autenticação do proxy|password|
|Executável do navegador|Caminho para o executável do Google Chrome. Somente necessário se estiver usando esse navegador.|C:/Program Files/Google/Chrome/Application/chrome.exe|
|Pasta de perfil|Caminho para a pasta de perfil do usuário usada pelo navegador. Se deixado vazio, um temporário será criado e excluído ao reiniciar sem uma pasta de perfil ou ao usar o comando Fechar Navegador.|C:/folder/profile/|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) para o carregamento da URL inicial.|30|
|Modo Headless|Executar o navegador em modo headless (sem GUI)||
|ID de Sessão|ID único para esta sessão do Playwright. Permite executar vários navegadores ou bots em paralelo sem interferência entre eles.|1|

### Ir para URL

Navegar para uma URL e esperar até que o evento selecionado aconteça.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|||
|Esperar até|Loaded Aguarda o carregamento de toda a página, incluindo imagens e estilos.
DOMContentLoaded Aguarda a estrutura HTML aparecer, sem esperar por imagens.
Network Idle Aguarda até que a atividade de rede pare completamente por 500ms.
Commit considere a navegação como concluída quando a resposta da rede for recebida e o documento começar a carregar.||
|Abrir em nova aba|Se marcado, abre a URL em uma nova aba em vez da atual.||
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Fechar navegador

Fechar o navegador e todas as abas, e salva o estado do perfil.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Esperar Objeto

Esperar que um elemento esteja em um determinado estado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Estado|Estado para esperar||
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que o objeto esteja no estado selecionado.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Clique no objeto

Clicar em um elemento.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que seja possível clicar no elemento.|30|
|Forçar Clique|Se deve forçar a ação de clique, mesmo que o elemento não seja visível ou interagível.||
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Limpar input e enviar Texto

Apaga o conteúdo de um objeto input e envia o texto.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Texto para Preencher|||
|Tecla especial|Selecione uma tecla especial para apertar após o texto. (Opcional)|SPACE|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que seja possível escrever no elemento.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Extrair Texto Playwright

Obter o texto interno de um elemento.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que o texto do elemento possa ser extraído.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Tirar Screenshot

Tirar uma screenshot da página.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho da Pasta||C:/Users/User/Downloads/|
|Nome do Arquivo|Nome do arquivo e extensão|screenshot.jpg|
|Página Completa|Marque para capturar a página inteira rolável ou apenas a janela de visualização.||
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Download

Permite clicar em um botão para baixar um item.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a clicar.|Data|
|Tipo de Seletor|||
|Diretório de Salvamento|Pasta onde o arquivo será salvo. Opcional.|C:/Users/User/Downloads/|
|Substituir Nome do Arquivo|Opcional. Se estiver vazio, usa o nome original.|nome_arquivo|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que seja possível baixar o elemento.|60|
|Caminho do arquivo|Variável para armazenar o caminho final do arquivo||
|Variável Nome do Arquivo|Variável para armazenar o nome do arquivo||
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Selecionar Opção

Seleciona uma ou várias opções em um elemento suspenso.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Opção|Selecione os rótulos, valores ou índices das opções a escolher. Se for múltiplo, envie uma lista ex [opção1, opção2].|opção1|
|Selecionar a opção por|Selecione para escolher a opção por seu valor, rótulo ou índice.|Select by|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que uma opção do elemento possa ser selecionada.|30|

### Enviar combinação de teclas

Comando para enviar combinação de teclas para o elemento ativo. Atalhos que não fazem parte da página web, mas são atalhos do navegador ou do sistema não são suportados.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Primeira tecla especial|Primeira tecla especial a combinar com uma letra/numero e/ou com uma segunda tecla especial|SPACE|
|Segunda tecla especial|Segunda tecla especial para combinar com a primeira tecla se necessário.|SPACE|
|Letra ou número|Letra ou número para combinar com as teclas especiais, se necessário.|a|
|ID de Sessão|ID único para esta sessão do Playwright|4|

### Marcar / Desmarcar

Marcar ou desmarcar a caixa.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Marcar ou desmarcar|Marcar ou desmarcar a caixa.||
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que o elemento possa ser marcado / desmarcado.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Obter Atributo

Obter o valor de um atributo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de Seletor|||
|Nome do atributo|Nome do atributo cujo valor se quer obter.|value|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que o atributo do elemento possa ser obtido.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Esperar estado de carga

Esperar até que a página alcance um estado de carga requerido.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Estado de carga|Loaded Aguarda o carregamento de toda a página, incluindo imagens e estilos.
DOMContentLoaded Aguarda a estrutura HTML aparecer, sem esperar por imagens.
 Network Idle Aguarda até que a atividade de rede pare completamente por 500ms.|Load|
|Tempo de espera (seg)|Tempo máximo de espera (em segundos) até que a página alcance o estado de carregamento requerido.|30|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Obter títulos das abas

Retorna uma lista com os títulos de todas as abas abertas no navegador.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado do comando será armazenado|Variável|

### Mudar de aba por título

Mudar para uma aba pelo seu título no contexto atual.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Título|Título da aba para a qual deseja mudar|Variável|

### Avaliar JS.

Avalia JS no contexto da página. Retorna o resultado da execução.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Código JS|Código JS para avaliar no contexto da página. Retorna o resultado da execução.|function(data) {
	return param1 * param2;
}|
|Parâmetros da função|Lista de valores dos parâmetros a serem passados para a função. Os valores da lista são passados como strings.|[value1, value2, ...]|
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado do código JS será armazenado|Variável|

### Contar elementos

Contar quantas vezes um elemento aparece na página.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor dos elementos a selecionar.|Data|
|Tipo de Seletor|||
|ID de Sessão|ID único para esta sessão do Playwright|1|
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Mudar para IFRAME

Mudar para um IFRAME e definir seu conteúdo como padrão.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do iframe.|Data|
|Tipo de Seletor|||
|ID de Sessão|ID único para esta sessão do Playwright|1|

### Mudar para conteúdo do body

Mudar para o conteúdo do body da página como conteúdo padrão.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID de Sessão|ID único para esta sessão do Playwright|1|
