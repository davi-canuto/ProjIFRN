# CDU011. Definir equipe

- **Ator principal**: gerente de projeto
- **Atores secundários**: não existem
- **Resumo**: define usuários cadastrados envolvidos no desenvolvimento do projeto
- **Pré-condição**: deve ter usuários cadastrados no sistema. 
- **Pós-Condição**: atribuído cargo de gerente ao usuário, esse tem permissão em submeter postagens de projeto

## Fluxo Principal - definir equipe na criação do projeto
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessa o perfil no lado superior direito presente em todas páginas no sistema | |  
| | 2 - Listas opções para ver perfil, editar perfil e postar projeto |
| 3 - Clica na opção de postar projeto | | 
| | 4 - Abre um formulário de informações acerca do projeto |
| 5 - Preenche o formulário e define pelo menos um integrante para o projeto | | 
| | 6 - Guarda as informações |
| 7 - Submete o formulário | |
| | 8 - Retorna uma mensagem de sucesso e redireciona para página que usuário estava antes |

## Fluxo Alternativo I - definir equipe em projeto já postado
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| X.1 - Navega até página de seu perfil | |  
| | X.2 -  Carrega as informações do usuário |
| X.3 - Desce até a listagens de projetos que é gerente | |
| | X.4 - Lista horizontalmente os projetos | 
| X.5 - Acessa um projeto que deseja | |
| | X.6 - Carrega as informações do projeto | |
| X.7 - Acessa a opção de edição de projeto | 
| | X.8 - Carrega o mesmo formulário de postagem de projeto com as informações pré-definidas |
| X.9 - Insere novos membros ou remove | |
| | X.10 - Guarda as alterações |
| X.11 Submete | |
| | X.12 - Salva as alterações no banco de dados e retorna uma mensagem de sucesso |

## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| Y.1 - ... | |  
| | Y.2 - ... |  
