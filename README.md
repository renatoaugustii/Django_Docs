## WebDocs

WebDocs é um projeto criado com o objetivo de documentar e demonstrar boas práticas em desenvolvimento web.
A proposta é ter uma documentação interativa, onde cada conceito explicado conta com exemplos práticos diretamente na página, permitindo que o desenvolvedor teste e visualize o funcionamento em tempo real.

### Objetivo

- Centralizar boas práticas utilizadas em projetos web.
- Facilitar a manutenção futura e a padronização do código.
- Servir como guia de consulta rápida para mim (e para outros devs que colaborarem).
- Criar um ambiente de documentação + laboratório prático, inspirado no formato de docs como o Bootstrap.

### Instalação e Configuração

Siga os passos abaixo para rodar o projeto Django_Docs em seu ambiente local antes de publicar no Railway (ou em outro serviço):

##### 1. Clonar o repositório
`git clone https://github.com/seu-usuario/Django_Docs.git`
`cd Django_Docs`

##### 2. Criar ambiente virtual

Crie um ambiente virtual com o Python para isolar as dependências do projeto:
`python -m venv venv`


**Ative o ambiente:**

Windows (PowerShell):
`venv\Scripts\activate`


Linux/Mac:
`source venv/bin/activate`

3. Instalar dependências

Instale todas as dependências listadas no requirements.txt:

`pip install -r requirements.txt`

4. Criar arquivo .env

Crie um arquivo chamado .env na raiz do projeto.
Esse arquivo armazenará as credenciais sensíveis (Django e Banco de Dados).

### Exemplo de .env:

#### Django settings.py
```python
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
ALLOWED_HOSTS=127.0.0.1,localhost
```

#### Banco de Dados (Postgres como exemplo)
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=5432
```

## Importante:

O arquivo `.env` não deve ser versionado no GitHub. Adicione-o ao `.gitignore` para manter suas credenciais seguras.

5. Rodar migrações e iniciar o servidor
`python manage.py migrate`
`python manage.py runserver`


## Configurando SECRET_KEY de forma segura

Para manter seu projeto Django seguro, é importante não deixar a SECRET_KEY exposta no GitHub. Siga os passos abaixo:

1️⃣ Gerar nova SECRET_KEY

No terminal Python:
`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`


Copie a chave gerada — ela será a nova SECRET_KEY.

2️⃣ Criar arquivo .env

Na raiz do projeto, crie um arquivo .env para armazenar credenciais e variáveis sensíveis:

```python
SECRET_KEY=sua_nova_chave_aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```


⚠️ Não versionar este arquivo no GitHub.
Adicione-o ao .gitignore.

3️⃣ Configurar settings.py com Decouple

Instale a biblioteca se ainda não tiver:
`pip install python-decouple`


Substitua a linha fixa da SECRET_KEY:
`from decouple import config`

```python
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')
```

4️⃣ Remover SECRET_KEY antiga do histórico do Git (opcional, mas recomendado)

Para evitar exposição da chave antiga no GitHub, use o BFG Repo-Cleaner:
Crie um arquivo passwords.txt contendo a chave antiga:

chave_antiga_do_template

Clone o repositório em modo mirror:

`git clone --mirror https://github.com/seu-usuario/Django_Docs.git`
`cd Django_Docs.git`


Execute o BFG para substituir a chave antiga:

`bfg --replace-text passwords.txt`


Limpe e compacte o histórico:
```git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```


Isso remove a chave antiga do histórico do GitHub.