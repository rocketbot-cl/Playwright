



# Playwright

Módulo com funcionalidades avançadas para o navegador que utiliza Playwright em vez de Selenium

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo

Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.


## Overview


1. Abrir Chrome
Abre uma nova instância do Chrome.

2. Verificar Bibliotecas
Verifica se as bibliotecas necessárias para o SO atual existem e permite forçar seu download.

3. Fechar navegador
Fechar o navegador e todas as abas, e salva o estado do perfil.

4. Ir para URL
Navegar para uma URL e esperar até que o evento selecionado aconteça.

5. Esperar Objeto
Esperar que um elemento esteja em um determinado estado.

6. Clique no objeto
Clicar em um elemento.

7. Limpar input e enviar Texto
Apaga o conteúdo de um objeto input e envia o texto.

8. Extrair Texto Playwright
Obter o texto interno de um elemento.

9. Tirar Screenshot
Tirar uma screenshot da página.

10. Baixar
Permite clicar em um botão para baixar um item.

11. Selecionar Opção
Seleciona uma ou várias opções em um elemento suspenso.

12. Enviar combinação de teclas
Comando para enviar combinação de teclas para o elemento ativo. Atalhos que não fazem parte da página web, mas são atalhos do navegador ou do sistema não são suportados.

13. Marcar / Desmarcar
Marcar ou desmarcar a caixa.

14. Obter Atributo
Obter o valor de um atributo.

15. Esperar estado de carga
Esperar até que a página alcance um estado de carga requerido.

16. Obter títulos das abas
Retorna uma lista com os títulos de todas as abas abertas no navegador.

17. Mudar de aba
Mudar para uma aba pelo seu título ou índice no contexto atual.

18. Avaliar JS.
Avalia JS no contexto da página. Retorna o resultado da execução.

19. Contar elementos
Contar quantas vezes um elemento aparece na página.

20. Mudar para IFRAME
Mudar para um IFRAME e definir seu conteúdo como padrão.

21. Mudar para conteúdo do body
Mudar para o conteúdo do body da página como conteúdo padrão.

22. Clicar em link para nova aba
Clica em um link que abrirá uma nova aba.

23. Subir arquivo
Comando para fazer upload um ou mais arquivos para um input do tipo file. Basta preencher um único valor, dependendo de quantos arquivos você deseja enviar.

24. Interagir com alerta
Interage com uma alerta na página. Pode ser aceita ou rejeitada.

25. Imprimir como PDF
Imprima a página como PDF no Chrome. O PDF é gerado com base no conteúdo disponível da página. Não representa uma cópia verdadeira do site.

26. Fechar aba
Permite fechar uma aba por seu título ou índice.




----
### OS

- windows
- mac

### Dependencies
- [**playwright**](https://pypi.org/project/playwright/)
### License

![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)
[MIT](https://opensource.org/license/mit)