# Documento de Visão

## Histórico de Revisões

| Data                |  Versão             |          Descrição  |  Autores            |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| 20/04/2023 | 1.0 | itens 1, 2, 3 |  Equipe |
| 24/04/2023 | 1.1 | itens 4,5,8,9 |  Equipe |
| 14/05/2023 | 1.2 | atualizaçãos de todos itens | Equipe |

## 1. Objetivo do Projeto: 
 O ProjIFRN almeja disponibilizar uma plataforma à comunidade acadêmica que possibilite postagens de projetos desenvolvidos na Instituição Federal do Rio Grande do Norte

## 2. Descrição do problema

O IFRN não tem uma plataforma exclusivo a postagens de projetos 

|     |      |
| --- | --- |
| **Problema**            | descentralização de projetos |
| **Afeta**               | comunidade acadêmica e externo |  
| **Impacta**             | falta de visibilidade, divulgação e gerencia de projetos |
| **Solução**             | plataforma dedicada a postagens, divulgação e gerenciamento de projetos | 

## 3. Descrição dos usuários 

| Nome                |  Descrição          |   Responsabilidade  |
| -----------------   | -----------------   | -----------------   |
| Gerente de projeto | Gerenciador dos dados do projeto | Gerenciar postagens de projetos dele, inserir equipe no projeto que gerencia, atualizar informações do projeto se necessário |
| Usuário cadastrado | Autenticado no sistema | Gerenciar as informações em sua conta |
| Usuário sem cadastrado | Sem privilégios |  Acessar informações de projetos e perfis públicos |

## 4. Descrição do ambiente dos usuários

 Qualquer usuário poderá acessar a plataforma mediante um dispositivo com acesso a internet. Usuários autenticados terão um perfil disponível e usuários com permissões de gerente tem privilégios de cadastrar postagens de projetos no sistema.


## 5. Principais necessidades dos usuários

 Alunos do IFRN necessitam de uma plataforma que centralize os projetos deles e crie um histórico de participação em desenvolvimentos de projetos de forma a criar uma página simplificada com essas informações. Docentes tem dificuldades em acessar de maneira rápida projetos que orientou ou que orienta. Público externo desejam acompanhar projetos desenvolvidos na Instituição e acessar históricos de usuários em projetos 


## 6. Alternativas concorrentes

* **GitHub:** uma plataforma de versionamento de projetos, existem múltiplas funcionalidades dentro da plataforma, desde interações entre usuários até a colaboração em projetos públicos. Atualmente essa plataforma é a principal para armazenar os projetos desenvolvidos pela disciplina Projeto de Sistema Web do curso de Análise e Desenvolvimento de Sistemas na Instituição Federal do Rio Grande do Norte. Contudo há pontos desfavoráveis para alguns situações na disciplina:

   * Confusa para usuários poucos instruídos em tecnologia;
   
* **Portal IFRN:** plataforma dedicada a encaminhar informações do campus à comunidade acadêmica, como também público externo em geral. Dentre isso, há as informações e divulgações de projetos e pesquisas desenvolvidos pela Instituição. Alguns pontos desfavoráveis são:
   * Como é uma plataforma responsável em informar assuntos acerca dos campus de todas regiões no Estado, pode tirar o foco nas divulgações dos projetos e pesquisa e tornar dificultoso o acesso aos projetos aos usuários interessados.


## 7. Visão geral do produto

 ProjIFRN será uma plataforma voltada para comunidade acadêmica aonde os orientadores poderão relizar upload de metas informações acerca dos projetos, aonde possibilite uma apresentação objetiva do projeto para o público interessado nos projetos do IFRN. Além disso, a plataforma almeja uma interface facilitadora de navegabilidade, em que qualquer pessoa tenha acessa a informações desejadas de forma rápida e segura.

## 8. Requisitos funcionais

| Código              |  Nome               |          Descrição  |  Prioridade         |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| F01 | Pesquisar projeto | Listagens de projetos com as características da busca  | Necessário |
| F02 | Visualizar projeto | Acessa informações do projeto | Necessário |
| F03 | Visitar perfil | Acessa informações de usuários | Necessário |
| F05 | Cadastrar conta | Cria conta na plataforma | Necessário |
| F06 | Login | Entra no sistema como usuários autenticado | Necessário |
| F07 | Logout | Encerra sessão no sistema | Necessário |
| F08 | Gerenciar perfil |Gerencia as informações do perfil  | Necessário |
| F10 | Gerenciar projeto | Mantém a integridade de postagens de projeto | Necessário | 
| F12 | Definir gerente | Permite conta ter permissões de gerente de projeto | Necessário |
| F13 | Gerenciar categoria | Gerencia Categorias | Necessário |
| F14 | Gerenciar Usuário | Gerencia usuários cadastrados | Necessário |
| F15 | Adicionar administrador | Cria novos administradores da plataforma | Necessário |

## 9. Requisitos não-funcionais

| Código              |  Nome               |          Descrição  |  Categoria          |  Classificação      |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| NF01 | Segurança de dados pessoais | O sistema tornará público informações de usuários que aceitarem os termos de política e privavidade do sistema | Segurança | Necessário |
| NF02 | Interface | A interface do site será responsiva para qualquer dispositivo | Visão | Necessário |
| NF03 | Permissão | Apenas usuários com permissão de gerentes de projeto poderão criar postagens | Controle | Necessário |
