# CDU012. Definir gerente

- **Ator principal**: administrador
- **Atores secundários**: não existem
- **Resumo**: atribui um usuário cadastrado o cargo de gerente dentro do sistema
- **Pré-condição**: usuário precisa comprovar que faça parte do grupo docente
- **Pós-Condição**: atribuído cargo de gerente ao usuário, esse tem permissão em submeter postagens de projeto

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessa página restrita aos administradores do sistema | |  
| | 2 - Carrega os models do sistema |
| 3 - Acessa o model de usuários | | 
| | 4 - Lista os usuários cadastrados no sistema |
| 5 - Pesquisa pelo o usuário desejado e clica | | 
| | 6 - Abre página de formulários acessa das informações do usuário |
| 7 - Marca a opção que atribui gerência ao usuário e submete | |
| | 8 - Mensagem de sucesso e redireciona para página da listagem dos usuário |

## Fluxo Alternativo I - ...
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| X.1 - ... | |  
| | X.2 - ... |

## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| Y.1 - ... | |  
| | Y.2 - ... |  
