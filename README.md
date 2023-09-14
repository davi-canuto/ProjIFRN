# ProjIFRN

<img src="logo.png" width="200" height="200" />

Uma plataforma que possibilita a comunidade acadêmica compartilhar projetos

# Equipe e Formas de Contato

1. Antônio Fernandes da Cruz Junior
2. Davi Alessandro Canuto da Silva Gregório
3. Debora Lavínia da Silva Melo
4. Neemias Renan Santos de Oliveira
5. Wagner Amadeus Galvão de Souza

# Contatos
1. cruz.junior@escolar.ifrn.edu.br
2. davi.gregorio@escolar.ifrn.edu.br
3. melo.debora@escolar.ifrn.edu.br
4. neemias.renan@escolar.ifrn.edu.br
5. amadeus.galvao@escolar.ifrn.edu.br

# Horário de Reuniões

- **Quartas-feiras:** reunião com o orientador no campus
- **Segundas-feiras, Sextas-feiras e Sábados:** reunião da equipe no discord 

# Tecnologias Utilizadas

- Node
- Vue.js
- LucidChart
- VsCode
- Word

# Documentação

[Link para os documentos do projeto](doc/documentacao.md)

# Manual da Desenvolvedor

No terminal do seu computador digite para clonar:
- `git clone <url do repositório>`

Verifique se python está instalado na sua máquina:
- `python --version`

Entre no diretório que clonou o repositório:
- `cd <caminho do diretório>`

Crie um ambiente virutal:
- `python -m venv venv`

Ative o ambiente virtual:
- **windows:** - `venv\Scripts\activate`
- **linux/mac:** - `source venv/bin/activate`

Instale as dependências: 
- `pip install -r requirements.txt` 

Crie o banco de dados:
- `python manage.py migrate`

(Opcional) Crie um superusuário:
- `python manage.py createsuperuser`

Inicie o servidor: 
- `python manage.py runserver`
