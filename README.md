# ProjIFRN

<img src="logo.png" width="200" height="200" />

Uma plataforma que possibilita a comunidade acadêmica compartilhar projetos

# Equipe e Formas de Contato

1. Antônio Fernandes da Cruz Junior
2. Debora Lavínia da Silva Melo
3. Lucas Nithael Silva de Souza
4. Vinicius Vasconcelos Ferreira Soares
5. Wagner Amadeus Galvão de Souza

# Contatos
1. cruz.junior@escolar.ifrn.edu.br
2. melo.debora@escolar.ifrn.edu.br
3. lucas.nithael@escolar.ifrn.edu.br
4. soares.vinicius@escolar.ifrn.edu.br
5. amadeus.galvao@escolar.ifrn.edu.br

# Horário de Reuniões

- **Quartas-feiras:** reunião com o orientador no campus
- **Segundas-feiras, Sextas-feiras e Sábados:** reunião da equipe no discord 

# Tecnologias Utilizadas

- Python
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
- `pip install django` 
- `pip install django-summernote`
- `pip install pillow`

Crie o banco de dados:
- `python manage.py migrate`

(Opcional) Crie um superusuário:
- `python manage.py createsuperuser`

Inicie o servidor: 
- `python manage.py runserver`


## Observação
caso ocorra o erro `TypeError: clean() got an unexpected keyword argument 'styles'` na execução do projeto, significa um ajuste para versões recentes do django-summernote. Siga estes passos:

1. Acesse a pasta do seu ambiente virtual
2. Siga este caminho: `/lib64/python3.11/site-packages/django_summernote/fields.py`
3. Aonde tem `return bleach.clean(value, tags=ALLOWED_TAGS, attributes=ATTRIBUTES, styles=STYLES` mude o argumento `styles=STYLES` para `css_sanitizer=STYLES`

