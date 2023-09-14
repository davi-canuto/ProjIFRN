# Documento de Visão

**Histórico de Revisões**


<table>
  <tr>
   <td><strong>Data</strong>
   </td>
   <td><strong>Versão</strong>
   </td>
   <td><strong>Descrição das Alterações</strong>
   </td>
   <td><strong>Autores</strong>
   </td>
  </tr>
  <tr>
   <td>20/04/2023
   </td>
   <td>1.0
   </td>
   <td>Criação do documento
   </td>
   <td>Equipe
   </td>
  </tr>
  <tr>
   <td>24/04/2023
   </td>
   <td>1.1
   </td>
   <td>Adição de requisitos
   </td>
   <td>Equipe
   </td>
  </tr>
  <tr>
   <td>14/05/2023
   </td>
   <td>1.2
   </td>
   <td>Atualização de todos os itens
   </td>
   <td>Equipe
   </td>
  </tr>
  <tr>
   <td>14/09/2023
   </td>
   <td>2.0
   </td>
   <td>Revisão de todos os itens
   </td>
   <td>Equipe
   </td>
  </tr>
</table>


**1. Objetivo do Projeto**

O ProjIFRN tem como objetivo principal disponibilizar uma plataforma para a comunidade acadêmica do curso de TADS da Instituição Federal do Rio Grande do Norte (IFRN) onde seja possível realizar postagens de projetos desenvolvidos na instituição.

**2. Descrição do Problema**

O IFRN enfrenta um desafio relacionado à descentralização de informações sobre os projetos desenvolvidos, o que afeta tanto a comunidade acadêmica quanto o público externo. A falta de uma plataforma dedicada para postagens, divulgação e gerenciamento de projetos resulta em falta de visibilidade, dificuldades na divulgação e na gestão adequada desses projetos.


<table>
  <tr>
   <td><strong>Problema</strong>
   </td>
   <td>Descentralização de Projetos
   </td>
  </tr>
  <tr>
   <td><strong>Afeta</strong>
   </td>
   <td>Comunidade acadêmica e externo
   </td>
  </tr>
  <tr>
   <td><strong>Impacta</strong>
   </td>
   <td>Falta de visibilidade, divulgação e gerência de projetos
   </td>
  </tr>
  <tr>
   <td><strong>Solução</strong>
   </td>
   <td>Plataforma dedicada a postagens, divulgação e gerenciamento de projetos
   </td>
  </tr>
</table>


**3. Descrição dos Usuários**


<table>
  <tr>
   <td><strong>Tipo de Usuário</strong>
   </td>
   <td><strong>Descrição</strong>
   </td>
   <td><strong>Responsabilidades</strong>
   </td>
  </tr>
  <tr>
   <td>Gerente de Projeto
   </td>
   <td>Gerencia os dados de um projeto.
   </td>
   <td>- Criar projeto.
<p>
- Criar equipe.
<p>
- Editar projeto quando necessário.
   </td>
  </tr>
  <tr>
   <td>Usuário
   </td>
   <td>Usuário sem privilégios de autenticação.
   </td>
   <td>- Acessar informações públicas de projetos.
    <p>
    - Pesquiasar projeto.
    <p>
   </td>
  </tr>
</table>


**4. Descrição do Ambiente dos Usuários**

Qualquer usuário poderá acessar a plataforma ProjIFRN por meio de um dispositivo com acesso à internet. Os usuários com permissões de gerente terão o privilégio de cadastrar projetos no sistema.

**5. Principais Necessidades dos Usuários**

* Discentes do curso de TADS precisam de uma plataforma que centralize os projetos de PDS (Projeto de Desenvolvimento de Sistema), criando um histórico de participação em desenvolvimento de projetos e uma página simplificada com essas informações.
* Criar um Website que sirva de portfólio para demosntração de PDS para os discentes ingressantes na disciplina.
* Criar uma plaforma que forneça exemplares de projetos finalizados e em andamento para formentação de novas ideias e continuação de projetos órfãos.

**6. Alternativas Concorrentes**

**GitHub **- Plataforma de versionamento de projetos com diversas funcionalidades.

* **Pontos Positivos:** Colaboração em projetos públicos.
* **Pontos Negativos**: Confuso para usuários não familiarizados com tecnologia.

**Portal IFRN **- Plataforma dedicada a informações dos campi do IFRN, incluindo projetos e pesquisas.

* **Pontos Positivos**: Informações sobre toda a instituição.
* **Pontos Negativos**: Dificuldade de acesso rápido aos projetos devido à diversidade de informações.

**7. Visão Geral do Produto**

O ProjIFRN será uma plataforma focada na comunidade acadêmica de TADS do IFRN, permitindo que orientadores realizem o upload de informações detalhadas sobre projetos. Isso proporcionará uma apresentação objetiva dos projetos para o público interessado. A plataforma terá uma interface de fácil navegação, garantindo acesso rápido e seguro às informações desejadas.

**8. Requisitos Funcionais**

<table>
  <tr>
   <td><strong>Código</strong>
   </td>
   <td><strong>Nome</strong>
   </td>
   <td><strong>Descrição</strong>
   </td>
   <td><strong>Prioridade</strong>
   </td>
  </tr>
  <tr>
   <td>F01
   </td>
   <td>Pesquisar Projeto
   </td>
   <td>Listar projetos de acordo com critérios de busca
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>F02
   </td>
   <td>Acessar Projeto
   </td>
   <td>Visualizar detalhes de um projeto
   </td>
   <td>Necessário
   </td>
  </tr>
   <tr>
   <td>F03
   </td>
   <td>Criar projeto
   </td>
   <td>Criar um novo projeto
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>F04
   </td>
   <td>Gerenciar Projeto
   </td>
   <td>Editar projetos
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>F05
   </td>
   <td>Definir Equipe
   </td>
   <td>Definir membros da equipe de projeto
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>F06
   </td>
   <td>Alterar Status
   </td>
   <td>define o estado que o projeto está
   </td>
   <td>Necessário
   </td>
  </tr>
</table>


**9. Requisitos Não-funcionais**


<table>
  <tr>
   <td><strong>Código</strong>
   </td>
   <td><strong>Nome</strong>
   </td>
   <td><strong>Descrição</strong>
   </td>
   <td><strong>Categoria</strong>
   </td>
   <td><strong>Classificação</strong>
   </td>
  </tr>
  <tr>
   <td>NF01
   </td>
   <td>Segurança de Dados Pessoais
   </td>
   <td>Proteção das informações pessoais dos usuários
   </td>
   <td>Segurança
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>NF02
   </td>
   <td>Interface
   </td>
   <td>Interface responsiva para qualquer dispositivo
   </td>
   <td>Visão
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>NF03
   </td>
   <td>Permissão
   </td>
   <td>Apenas gerentes podem criar projetos
   </td>
   <td>Controle
   </td>
   <td>Necessário
   </td>
  </tr>
  <tr>
   <td>NF04
   </td>
   <td>Permissão
   </td>
   <td>Integração com API do GitHub
   </td>
   <td>Controle
   </td>
   <td>Necessário
   </td>
  </tr>
   <tr>
   <td>NF05
   </td>
   <td>Permissão
   </td>
   <td>Integração com API do SUAP
   </td>
   <td>Controle
   </td>
   <td>Necessário
   </td>
  </tr>
</table>


Este documento de visão define os objetivos, requisitos e contexto geral do projeto ProjIFRN, proporcionando uma visão clara do que está sendo desenvolvido e como atenderá às necessidades dos usuários.
