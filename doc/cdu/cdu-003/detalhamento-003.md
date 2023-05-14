# CDU003. Visitar perfil

- **Ator principal**: todos usuários do site
- **Atores secundários**:	não existe
- **Resumo**: usuários do sistema podem acessar informações no perfil de usuários cadastrados no sistema
- **Pré-condição**: o sistema deve ter pelo menos um usuário cadastrado e tenha aceitado o compartilhamento de suas informações
- **Pós-Condição**: caso o usuário do perfil visitado não tenha aceitado o compartilhamento, será mostrado uma página de perfil sem informações

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessa um projeto | |  
| | 2 - Abre uma página com informações do projeto |
| 3 - Visualiza a equipe do projeto | |
| | 4 - Carrega uma lista de usuários relacionados ao projeto ao lado direto da página |
| 5 - Clica em no nome ou imagem de um integrante do projeto | |
| | 6 - Busca as informações do perfil no banco de dados | |
| | 7 - Abre uma página com as informações do perfil visitado |

## Fluxo Alternativo I - Acessar perfil a partir da barra de pesquisa
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| X.1 - Localiza a barra de pesquisa e seleciona | |  
| | X.2 - Aguarda algo ser digitado |
| X.3 - Marca a opção de busca por usuário e digita o nome | |
| | X.4 - Aguarda o que foi digitado na caixa de pesquisa |
| X.5 - Clica na busca | |
| | X.6 - Busca no banco de dados os usuários correspondente ao nome da busca |
| X.7 - Clica na imagem ou nome para ter acesso as informações de usuário | |
| | X.8 - Carrega uma página página com informações do perfil visitado |


## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| Y.1 - ... | |  
| | Y.2 - ... |  
