# Mapa do Site

```mermaid
flowchart TD
    Início --> meuPerfil[Meu Perfil]
    Início --> Feed[Feed dos Projetos]
    Início --> Pesquisa
    meusProjetos --> Projetos
    
    Feed[Feed dos Projetos] --> Projetos
    Projetos --> PerfilEquipe[Perfis da Equipe]
    Pesquisa --> Filtros
    Filtros --> Projetos

    subgraph meuPerfil[Meu Perfil]
        editarPerfil[Editar Meu Perfil]
        meusProjetos[Meus Projetos]
        Contato
        Contato --> Email
        Contato --> SocialMidia[Redes Sociais]
    end 
```
