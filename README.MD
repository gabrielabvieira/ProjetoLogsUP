# DOCUMENTAÇÃO LOGSUP
#### Gabriela Brito Vieira
&nbsp;
&nbsp;
---
### 1. Objetivo

Desenvolver um sistema web com Django para gestão de produtos, autenticação de usuários e controle de permissões, incluindo:
- Cadastro e login de usuários.
- Definição de grupos (Analistas e Supervisores) via Django Admin.
- CRUD de produtos com permissões baseadas em grupos.
- API RESTful para consulta de produtos (somente leitura).
- Painel web interativo para visualização e gestão de produtos.


### 2.  Requisitos Técnicos
O projeto foi desenvolvido com as seguintes premissas:

- **Framework**: Django 4.2
- **Banco de Dados**: PostgreSQL 16
- **Autenticação**: Sistema nativo do Django (AbstractUser).
- **API**: Django REST Framework.
- **Frontend**: Templates HTML com Bootstrap para o painel web.


---
### 3. Escopo do Desenvolvimento

##### 3.1 - Autenticação de Usuários

- Formulário de cadastro com campos: `Usuário`,`Nome`, `Email`, `Senha`, `Confirmação de Senha`.
- Login e logout de usuários.
- Acesso restrito ao painel e API apenas para usuários autenticados.

&nbsp;

##### 3.2 - Controle de Permissões

- **Grupos no Django Admin**:
  - **Analistas**: Podem visualizar e criar produtos.
  - **Supervisores**: Podem visualizar, criar, editar e excluir produtos.
- Permissões aplicadas nas views e templates (botões de edição/exclusão desabilitados para Analistas).

&nbsp;
##### 3.3 - Gestão de Produtos
- Modelo `Produto` com campos:
  ```python
  class Produto(models.Model):
      nome = models.CharField(max_length=100)
      descricao = models.TextField()
      preco = models.DecimalField(max_digits=10, decimal_places=2)
      quantidade = models.IntegerField()
      data_criacao = models.DateTimeField(auto_now_add=True)
      usuario = models.ForeignKey(User, on_delete=models.CASCADE)```
- Funcionalidades CRUD integradas ao painel web.

&nbsp;
##### 3.4 - API RESTful
- Endpoint: /api/painel/

- Métodos permitidos: GET (apenas para usuários autenticados).

- Serialização dos dados em JSON.

&nbsp;
##### 3.5 - Painel Web
- Listagem de produtos em tabela com filtro por nome.

- Botões condicionais (Editar/Excluir habilitados apenas para Supervisores).

- Formulário de criação de produtos acessível para Analistas e Supervisores.

&nbsp;
### 4. Estrutura do Projeto
```
📁 PROJETOLOGSUP/
├── 📁 core/ # Configurações principais do projeto
│ ├── settings.py # Configurações globais
│ ├── urls.py # Rotas principais
│ ├── wsgi.py
│
├── 📁 products/ # App para gestão de produtos
│ ├── migrations/
│ ├── admin.py # Registro de models no Django Admin
│ ├── apps.py
│ ├── models.py # Modelo Produto
│ ├── serializers.py # Serializadores para a API
│ ├── urls.py # Rotas específicas de produtos
│ └── views.py # Lógica de CRUD e API
│
├── 📁 usuarios/ # App para autenticação e usuários
│ ├── migrations/
│ ├── templatetags/ # Custom template tags
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py # Formulários de login/cadastro
│ ├── models.py # Modelo User personalizado 
│ ├── urls.py # Rotas de autenticação
│ └── views.py # Lógica de login/logout/cadastro
│
├── 📁 static/ # Arquivos estáticos (CSS, JS, imagens)
│ └── 📁 templates/ # Templates HTML
│ ├── adicionar_produto.html
│ ├── editar_produto.html
│ ├── login.html
│ ├── panel.html
│ └── registrar.html
│
├── 📁 projeto/ # Ambiente virtual (venv)
│ ├── Include/
│ ├── Lib/
│ ├── Scripts/
│ ├── .gitignore
│ └── pyvenv.cfg
│
├── 📄 manage.py # Script de gerenciamento do Django
├── 📄 db.sqlite3 # Banco de dados SQLite (dev)
└── 📄 README.MD # Documentação do projeto
```

&nbsp;
### 5. Instruções para Execução
##### 5.1 - Clonar repositório:
```
   git clone [URL_DO_REPOSITÓRIO]
   cd PROJETOLOGSUP
```

##### 5.2 - Ativar ambiente virtual :

- Windows
```.\projeto\Scripts\activate```

- Linux/Mac
```source projeto/bin/activate```

##### 5.3 - Instalar dependências:
```
pip install -r requirements.txt
```
##### 5.4 - Executar migrações do banco de dados:

```python manage.py migrate```
##### 5.5 - Criar superusuador (para acessar o Django Admin):

```python manage.py createsuperuser```

##### 5.6 - Iniciar servidor:

```python manage.py runserver```


##### 5.7 - Acessar a Aplicação:
```
Painel web: http://127.0.0.1:8000/

Django Admin: http://127.0.0.1:8000/admin/

API: http://127.0.0.1:8000/api/painel/
```

&nbsp;
