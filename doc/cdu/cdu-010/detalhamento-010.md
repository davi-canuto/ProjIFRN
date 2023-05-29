# CDU010. Gerenciar projeto

- **Ator principal**: Gerente de projeto
- **Atores secundários**: não existe
- **Resumo**: insere, altera e apaga informações acerca do projeto
- **Pré-condição**: necessário ter permissão de gerente de projeto e preencher todos campos obrigatórios do projeto
- **Pós-Condição**: inserida, alterada ou apagada informações no processo é constata imediatamente para todos usuários que acessarem o projeto

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessa a opção de perfil presente no header | |  
| | 2 - Abre uma janela flutuante com a opção de criar projeto | 
| 3 - Clica na opção de criar projeto | |
| | 4 - Abre uma página com formulário dos campos de informações de projeto |
| 7 - Preenche e submete | |
| | 9 - Mostra mensagem de sucesso redireciona para página que o usuário estava anteriormente |

## Fluxo Alternativo I - Alterar informações do projeto
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| X.1 - Navega até a página do perfil | |  
| | X.2 - Carrega as informações do perfil do usuário |
| X.3 - Navega até a seção de projetos | |
| | x.4 - Carrega os projetos que o usuário pertence |
| X.5 Abre um dos projetos | |
| | X.6 - Carrega as informações do projeto e uma opção de edição do projeto |
| X.7 - Clica na opção de edição | |

## Fluxo Alternativo II - Submeter uma postagem vazia
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| Y.1 - Navega até a opção de criar projeto | |  
| | Y.2 - Abre formulário para postagem de um novo projeto |
| Y.3 - Tenta submeter o formulário vazio | |
| | Y.4 - Mostra mensagem de campo vazio e aguarda o preenchimento |
