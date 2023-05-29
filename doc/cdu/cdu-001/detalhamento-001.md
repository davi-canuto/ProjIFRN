# CDU001. Pesquisar projeto

- **Ator principal**: todos usuários do site
- **Atores secundários**:	não existe
- **Resumo**: pesquisa por projetos especifícos dentros do sistema
- **Pré-condição**: deve ter pelo menos um projeto cadastrado no sistema
- **Pós-Condição**: caso não exista um projeto correspondente a pesquisa, o sistema deve retorna uma mensagem informndo que o projeto não existe

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Seleciona a opção de busca presente no topo de todas páginas do site | |  
| | 2 - Aciona a barra de pesquisa a aguarda os critérios de pesquisa |
| 3 - Informa o critério de pesquisa na barra de pesquisa | |
| | 4 - Guarda no formulário de pesquisa os critérios |
| 5 - Clica no botão de pesquisar | |
| | 6 - Busca no banco de dados os projetos correspondentes a pesquisa | |
| | 7 - Carrega na página as pesquisas que correspondem a pesquisa |

## Fluxo Alternativo I - Sem projeto correspondência a pesquisa
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| X.1 - Seleciona a opção de busca | |  
| | X.2 - Aciona a barra de pesquisa a aguarda os critérios de pesquisa |
| X.3 - Informa o critério de pesquisa na barra de pesquisa | |
| | X.4 - Guarda no formulário de pesquisa os critérios |
| X.5 - Clica no botão de pesquisar | |
| | X.6 - Busca no banco de dados os projetos correspondentes a pesquisa | |
| | X.7 - Mostra na página a mensagem que não projetos que correspondam a pesquisa |


## Fluxo Alternativo II - Tentar pesquisa campo vazio
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| Y.1 - Seleciona a opção de busca  | |  
| | Y.2 - Aciona o campo de busca |
| Y.3 - Não digita algo para busca | |
| | Y.4 - Aguarda algo ser digitado |
| Y.5 - Clica na opção para buscar | |
| | Y.6 - As bordas ficam vermelhas | |
| | Y.77 - Aguarda algo ser digitado |
