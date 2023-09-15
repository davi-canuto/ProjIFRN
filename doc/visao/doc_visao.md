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
   <td>15/09/2023
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

O ProjIFRN tem como objetivo principal disponibilizar uma plataforma web para a comunidade acadêmica do curso de TADS (Tecnologia em Análise e Desenvolvimento de Sistemas) do Instituto Federal do Rio Grande do Norte (IFRN). Essa plataforma será destinada aos discentes e docentes do curso, com o propósito de permitir a postagem e divulgação de projetos de desenvolvimento web desenvolvidos pelos discentes do curso e supervisionados e orientados pelos docentes do curso, relacionados às disciplinas de Projeto de Desenvolvimento de Sistemas Web, Projeto de Desenvolvimento de Sistemas Distribuídos e Projeto de Desenvolvimento de Sistemas Corporativos. Os projetos desenvolvidos e postados na plataforma ProjIFRN abordarão assuntos e temas diversos, proporcionando um espaço flexível e aberto para a exploração de uma ampla gama de trabalhos já realizados e em andamento pelos alunos do curso, todos relacionados ao desenvolvimento de sistemas web.

**2. Descrição do Problema**

O curso de TADS enfrenta um desafio crítico relacionado à ausência de uma plataforma web dedicada para postagens, divulgação e gerenciamento de projetos desenvolvidos pelos discentes durante as disciplinas de desenvolvimento de projetos do curso. Essa lacuna tem um impacto significativo na falta de visibilidade para a comunidade acadêmica interessada, incluindo discentes, docentes e público externo. A falta de um sistema centralizado dificulta a divulgação eficaz e a gestão adequada desses projetos, resultando em uma perda de oportunidades de colaboração e compartilhamento de conhecimento.

<table>
  <tr>
   <td><strong>Problema</strong>
   </td>
   <td>Ausência de uma plataforma web dedicada para postagens, divulgação e gerenciamento de projetos desenvolvidos por discentes.
   </td>
  </tr>
  <tr>
   <td><strong>Afeta</strong>
   </td>
   <td>Comunidade acadêmica do curso de TADS. Público externo interessado.
   </td>
  </tr>
  <tr>
   <td><strong>Impacta</strong>
   </td>
   <td>Falta de visibilidade dos projetos. Dificuldades na divulgação. Gestão ineficaz de projetos.
   </td>
  </tr>
  <tr>
   <td><strong>Solução</strong>
   </td>
   <td>Desenvolvimento de uma plataforma dedicada para postagens, divulgação e gerenciamento de projetos de desenvolvimento de sistemas.
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
<p> - Criar equipe.
<p> - Editar projeto quando necessário.
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

O ambiente dos usuários da plataforma ProjIFRN é acessível a qualquer usuário por meio de um dispositivo com acesso à internet e a utilização de um navegador (browser). Os usuários são divididos em dois tipos principais:

<strong>Gerente de Projeto (docentes)</strong>:
O Gerente de Projeto é responsável por gerenciar os dados de um projeto na plataforma ProjIFRN. Suas responsabilidades incluem:
<ol type="i">
<li>Criar, editar, atualizar e excluir projetos quando necessário;</li>
<li>Criar equipes de projeto;</li>
<li>Adicionar membros (discentes) às equipes de projeto.</li>
</ol>

<strong>Usuário (discentes)</strong>:
Os Usuários são indivíduos sem privilégios de autenticação específicos na plataforma. Suas responsabilidades se concentram em:
<ol type="i">
<li>Acessar informações públicas de projetos disponíveis na plataforma;</li>
<li>Realizar pesquisas sobre projetos existentes.</li>
</ol>

Apenas os Gerentes de Projeto (docentes) têm o privilégio adicional de cadastrar novos projetos no sistema.

**5. Principais Necessidades dos Usuários**

<p> Os discentes do curso de TADS apresentam diversas necessidades específicas que a plataforma ProjIFRN visa atender de forma abrangente e eficaz:</p> 

<strong> Criação de um Website de Portfólio:</strong> 
<ol type="i">
<li> Há uma necessidade de criar um website que sirva como portfólio para as disciplinas de desenvolvimento (web, distribuido e corporativo), possibilitando a demonstração de projetos de desenvolvimento de sistemas para discentes ingressantes nas disciplinas de desenvolvimento;</li> 
<li> Esse portfólio é essencial para apresentar as habilidades e conquistas anteriores dos discentes, promovendo uma maior interação e colaboração entre as gerações de estudantes.</li> 
</ol>

<strong> Acesso a Exemplares de Projetos:</strong> 
<ol type="i">
<li> Os discentes desejam uma plataforma que forneça acesso a exemplares de projetos finalizados e em andamento;</li> 
<li> Essa funcionalidade é crucial para a formação de novas ideias e a continuação de projetos "órfãos," incentivando a inovação e o desenvolvimento contínuo.</li> 
</ol>

<p> A plataforma ProjIFRN busca atender a essas necessidades, proporcionando aos discentes um ambiente centralizado e acessível para explorar, compartilhar e colaborar em projetos de desenvolvimento de sistemas (web, distribuido e corporativo), além de fortalecer a comunidade acadêmica do curso de TADS. </p>

**6. Alternativas Concorrentes**

A plataforma ProjIFRN, atualmente em desenvolvimento, destaca-se por sua singularidade na comunidade de TADS. Ao analisar o cenário, observamos que ProjIFRN não enfrenta concorrentes diretos ou alternativas comparáveis no mercado acadêmico.
Esta ausência de concorrência é um reflexo da inovação e do comprometimento em atender às necessidades específicas dos discentes e docentes do curso de TADS do IFRN. A plataforma ProjIFRN foi concebida com o intuito de preencher uma lacuna crucial na descentralização de projetos, proporcionando um ambiente centralizado para postagem, divulgação e gerenciamento de projetos de desenvolvimento web.
Essa singularidade posiciona a ProjIFRN como uma solução inovadora e sob medida para a comunidade de TADS; compartilhando conhecimento, experiências e impulsionando o progresso no desenvolvimento de sistemas.

**7. Visão Geral do Produto**

O ProjIFRN é uma plataforma web, em desenvolvimento, sob medida para atender às necessidades da vibrante comunidade acadêmica do curso de TADS no IFRN. Este produto visa simplificar e aprimorar a gestão de projetos acadêmicos; desenvolvimento de sistemas web, permitindo que orientadores e discentes compartilhem informações detalhadas e relevantes sobre seus projetos.
Com uma abordagem centrada no usuário, o ProjIFRN oferece uma experiência intuitiva e eficiente. Os orientadores terão a capacidade de realizar o upload de informações detalhadas sobre projetos, proporcionando uma apresentação objetiva e informativa para o público acadêmico e externo interessado. Isso não apenas simplifica a divulgação de projetos, mas também promove a colaboração, permitindo que outros discentes e docentes se envolvam e se inspirem por meio de projetos já realizados ou em andamento.
A plataforma será dotada de uma interface de fácil navegação, garantindo que todos os usuários tenham acesso rápido e confiável às informações desejadas. Isso tornará a exploração e o compartilhamento de projetos uma tarefa simples e agradável, incentivando a disseminação do conhecimento e o fortalecimento da comunidade acadêmica de TADS no IFRN.

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
   <tr>
   <td>NF06
   </td>
   <td>Desempenho
   </td>
   <td>Tempo de carregamento das páginas
   </td>
   <td>Desempenho
   </td>
   <td>Importante
   </td>
  </tr>
   <tr>
   <td>NF07
   </td>
   <td>Escalabilidade
   </td>
   <td>Capacidade de lidar com um grande número de projetos
   </td>
   <td>Escalabilidade
   </td>
   <td>Importante
   </td>
  </tr>
   <tr>
   <td>NF08
   </td>
   <td>Conformidade com Padrões
   </td>
   <td>Adesão a padrões de acessibilidade web
   </td>
   <td>Visão
   </td>
   <td>Importante
   </td>
  </tr>  
</table>


<p>Este documento de visão estabelece os objetivos, requisitos e contexto abrangente do projeto ProjIFRN, fornecendo uma visão clara do que está sendo desenvolvido e de como irá atender às necessidades dos usuários.</p>
