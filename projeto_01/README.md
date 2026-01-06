# Etapa 01 - Criando o ambiente de desenvolvimento

`
Nesta etapa, vamos criar o ambiente de desenvolvimento para o nosso projeto Django. Vamos utilizar o PDM (Python Development Manager / Product Development Master) para gerenciar as dependências do projeto e criar um ambiente virtual. 
`

Criaremos uma nova pasta chamada `projeto_01`. Dentro desta pasta, criaremos outras duas pastas, uma chamada `backend` e outra chamada `frontend`. 

Execute no terminal os seguintes comandos:
```bash
mkdir projeto_01
cd projeto_01
mkdir backend
mkdir frontend
cd backend
code .
```

Agora usaremos o PDM para criar um ambiente virtual e instalar o Django. No terminal, digite o seguinte comando:
```bash
pdm init
```

> Selecione a opção 0 para criar um novo ambiente. O arquivo `pyproject.toml` será criado.

Agora, ainda no terminal, abra a pasta no VSCode, executando o seguinte comando:
```bash
code .
```

Depois de aberto, vá novamente ao terminal e digite o seguinte comando para instalar o Django:
```bash
pdm add django
```

Neste momento será criado o arquivo pdm.lock.

Novamente no terminal, criaremos o projeto Django, que será a administração do nosso backend. Digite o seguinte comando:

> **ATENÇÃO:** O ponto no final do comando é importante para que o projeto seja criado na pasta atual.
```bash
pdm run django-admin startproject config .
```

Neste momento já temos uma pasta nova no projeto. A pasta `config` é a pasta principal do projeto Django. Dentro dessa pasta estão os arquivos:
- `asgi.py`: Arquivo de configuração para o ASGI (Asynchronous Server Gateway Interface).
- `settings.py`: Arquivo de configuração do projeto.
- `urls.py`: Arquivo de configuração das rotas do projeto.
- `wsgi.py`: Arquivo de configuração para o WSGI (Web Server Gateway Interface).

Agora, inclusive, já temos um serviço Django rodando. Para testar, execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Acesse o endereço `http://localhost:8000/` no navegador. Você verá a página inicial do Django.

Para parar o servidor, pressione `Ctrl + C` no terminal.

Embora já exista a interface administrativa do projeto, ainda não temos o banco de dados configurado. Para isso, execute o seguinte comando no terminal:
```bash
pdm run python manage.py migrate
```

Ainda no terminal, precisamos criar um usuário que terá acesso à interface administrativa. Este usuário é conhecido como `superusuario`. Execute o seguinte comando:
```bash
pdm run python manage.py createsuperuser
```

> SUGESTÃO: Use o nome `admin` para o superusuário.
> 
> Para o e-mail, neste momento, use também `admin@admincom`
>
> A senha pode ser `admin`. Repita novamente `admin`, obedecendo o solicitado.
>
> **ATENÇÃO:** A senha não será exibida no terminal.
>
> **ATENÇÃO:** O e-mail é fictício e não será utilizado para envio de e-mails.
>
> **ATENÇÃO:** Aparecerá um aviso confirmando se deseja prosseguir com a criação deste usuário e senha, pois a senha é muito comum. Digite `yes` e pressione `Enter`. Não se preocupe, neste momento, com questões de segurança.

Agora, para acessar a interface administrativa, execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Algumas alterações que podem ser realizadas no arquivo `settings.py`, que está na pasta `config`:
- Alterar o idioma do sistema:
```python
LANGUAGE_CODE = 'pt-br'
```
- Alterar o fuso horário:
```python
TIME_ZONE = 'America/Sao_Paulo'
```

Acesse o endereço `http://localhost:8000/admin/` no navegador. Faça login com o usuário criado anteriormente.

**Usuário:** admin
**Senha:** admin

# O serviço está rodando? Perfeito, então vamos para a próxima etapa.

# Etapa 02 - Criando a aplicação alunos

Nesta etapa, criaremos uma aplicação chamada `alunos` que será responsável por cadastrar os alunos de uma escola, informando apenas o nome, cidade, data de nascimento, e-mail e telefone. Como temos a cidade, e ela pode ser repetida para vários alunos, criaremos uma tabela chamada `Cidade` para armazenar as cidades e relacioná-las com os alunos. Várias cidades podem pertencer ao mesmo estado, então criaremos uma tabela chamada `Estado` para armazenar os estados e relacioná-los com as cidades.

## Criando a aplicação alunos

No terminal, execute o seguinte comando para criar a aplicação `alunos`:
```bash
pdm run python manage.py startapp alunos
```

Agora já temos uma nova app criada. Você pode perceber que uma nova pasta foi criada, a pasta `alunos`. Dentro dessa pasta estão os arquivos:
- `admin.py`: Arquivo de configuração do Django Admin.
- `models.py`: Arquivo de configuração dos modelos de dados.
- `tests.py`: Arquivo de testes.
- `views.py`: Arquivo de configuração das views.

Como criamos uma nova app, precisamos registrá-la no arquivo `config/settings.py`. Abra o arquivo `settings.py`, que está na pasta `config` e adicione a app `alunos` na lista `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'alunos',
]
```

## Criando os modelos de dados

Vamos criar os modelos de dados para a aplicação `alunos`. Abra o arquivo `models.py`, que está na pasta `alunos`, e adicione o seguinte código:
```python
from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
```

> Neste arquivo temos, na primeira linha, a importação do módulo `models` do Django.
> 
> Em seguida, criamos a classe `Estado` que herda de `models.Model`.
> 
> Esta classe possui dois atributos: `nome` e `sigla`, ambos do tipo `CharField`.
> 
> O método `__str__` retorna o nome do estado, que será exibido no Django Admin.

No terminal, execute o seguinte comando para criar a tabela `Estado` no banco de dados:
```bash
pdm run python manage.py makemigrations
pdm run python manage.py migrate
```

Agora, abra o arquivo `admin.py`, que está na pasta `alunos`, e adicione o seguinte código:
```python
from django.contrib import admin
from .models import Estado

admin.site.register(Estado)
```

Este código registra o modelo `Estado` no Django Admin.

> **Pare, pense e compreenda:** _Veja que inicialmente criamos o projeto Django admin, chamado `config`. Depois, criamos uma aplicação, chamada `alunos`. Para relacionar os dois, fomos no arquivo `settings.py`da pasta `config` para "instalar" a aplicação na administração do Django. Posteriormente foi então criada a model `Estado`, no arquivo `models.py`. Então, no arquivo `admin.py` da aplicação `alunos` registramos esta model criada, para que ela possa ficar acessível na interface administrativa do Django. Cria-se uma ligação entre a administração do django, a app criada e a model da app._

Se você acessar o Django Admin, verá a tabela `Estado` disponível para cadastro. Para acessar o Django Admin, execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Acesse o endereço `http://localhost:8000/admin/` no navegador. Você verá a página de login do Django Admin. Faça login com o superusuário criado anteriormente (usuário `admin` e senha `admin`). Após o login, você verá a página inicial do Django Admin. Clique em `Estado` para cadastrar um novo estado.

## Criando a tabela Cidade

Vamos criar a tabela `Cidade` para armazenar as cidades e relacioná-las com os estados. Abra o arquivo `models.py`, que está na pasta `alunos`, e adicione o seguinte código:
> *Deixe uma linha de intervalo em branco entre as classes.*
```python
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
```

> Neste código, criamos a classe `Cidade` que herda de `models.Model`.
>
> Esta classe possui dois atributos: `nome` e `estado`.
>
> O atributo `estado` é uma chave estrangeira que relaciona a cidade com o estado.
>
> O método `__str__` retorna o nome da cidade, que será exibido no Django Admin.
>
> A chave estrangeira `estado` é do tipo `ForeignKey` e recebe como parâmetro a classe `Estado` criada anteriormente.
>
> O parâmetro `on_delete=models.PROTECT` indica que, caso um estado seja excluído, as cidades relacionadas a ele não serão excluídas.
>
> **Pare, pense e compreenda:** _Veja que criamos a model `Cidade` e relacionamos com a model `Estado`. A model `Estado` foi criada anteriormente e já está disponível na interface administrativa do Django. Agora, criamos a model `Cidade` e relacionamos com a model `Estado`. A model `Cidade` também será disponibilizada na interface administrativa do Django._

No terminal, execute o seguinte comando para criar a tabela `Cidade` no banco de dados:
```bash
pdm run python manage.py makemigrations
pdm run python manage.py migrate
```

Agora, abra o arquivo `admin.py`, que está na pasta `alunos`, e adicione o seguinte código:
```python
from .models import Cidade

admin.site.register(Cidade)
```

Este código registra o modelo `Cidade` no Django Admin e o torna disponível para cadastro.

Uma possibilidade é, ao invés de ter duas linhas para importar de .models, importar tudo de uma vez:
```python
from .models import Estado, Cidade
```

Se você acessar o Django Admin, verá a tabela `Cidade` disponível para cadastro. Para acessar o Django Admin, execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Acesse o endereço `http://localhost:8000/admin/` no navegador. Você verá a página de login do Django Admin. Faça login com o superusuário criado anteriormente (usuário `admin` e senha `admin`). Após o login, você verá a página inicial do Django Admin. Clique em `Cidade` para cadastrar uma nova cidade.

**SUGESTÃO**

Altere a definição do método `__str__` da classe `Estado` para exibir o nome e a sigla do estado:
```python
def __str__(self):
    return f'{self.nome} - {self.sigla}'
```

Altere a definição do método `__str__` da classe `Cidade` para exibir o nome da cidade e a sigla do estado ao qual ela pertence:
```python
def __str__(self):
    return f'{self.nome} - {self.estado.sigla}'
```

## Criando a tabela Aluno

Vamos criar a tabela `Aluno` para armazenar os alunos. Abra o arquivo `models.py`, que está na pasta `alunos`, e adicione o seguinte código:

```python
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
```

> Neste código, criamos a classe `Aluno` que herda de `models.Model`.
>
> Esta classe possui cinco atributos: `nome`, `data_nascimento`, `email`, `telefone` e `cidade`.
>
> O atributo `cidade` é uma chave estrangeira que relaciona o aluno com a cidade.
>
> O método `__str__` retorna o nome do aluno, que será exibido no Django Admin.
>
> A chave estrangeira `cidade` é do tipo `ForeignKey` e recebe como parâmetro a classe `Cidade` criada anteriormente.
>
> O parâmetro `on_delete=models.PROTECT` indica que, caso uma cidade seja excluída, os alunos relacionados a ela não serão excluídos.

No terminal, execute o seguinte comando para criar a tabela `Aluno` no banco de dados:
```bash
pdm run python manage.py makemigrations
pdm run python manage.py migrate
```

Agora, abra o arquivo `admin.py`, que está na pasta `alunos`, e adicione o seguinte código:
```python
from .models import Aluno

admin.site.register(Aluno)
```

Este código registra o modelo `Aluno` no Django Admin e o torna disponível para cadastro.

Ao invés de ter duas linhas para importar de .models, você pode importar tudo de uma vez, numa linha só:
```python
from .models import Estado, Cidade, Aluno
```

Se você acessar o Django Admin, verá a tabela `Aluno` disponível para cadastro. Para acessar o Django Admin, execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Acesse o endereço `http://localhost:8000/admin/` no navegador. Você verá a página de login do Django Admin. Faça login com o superusuário criado anteriormente (usuário `admin` e senha `admin`). Após o login, você verá a página inicial do Django Admin. Clique em `Aluno` para cadastrar um novo aluno.

**SUGESTÃO**

Altere a definição do método `__str__` da classe `Aluno` para exibir o nome do aluno e a cidade e estado ao qual ele pertence:
```python
def __str__(self):
    return f'{self.nome} - {self.cidade.nome} ({self.cidade.estado.sigla})'
```

# Estados, Cidades e Alunos cadastrados? Então vamos para a próxima etapa!

Agora que criamos as tabelas `Estado`, `Cidade` e `Aluno`, cadastramos alguns estados, cidades e alunos, vamos para a próxima etapa. Nesta etapa, vamos criar uma API REST para listar, cadastrar, atualizar e excluir os alunos cadastrados.

# Etapa 03 - Criando a API REST

Nesta etapa, vamos criar uma API REST para listar, cadastrar, atualizar e excluir os alunos cadastrados.

## Django REST Framework

O Django REST Framework é uma biblioteca que facilita a criação de APIs REST em projetos Django. Para instalar o Django REST Framework, execute o seguinte comando no terminal:
```bash
pdm add djangorestframework
```

Agora, adicione o Django REST Framework ao arquivo `INSTALLED_APPS` do arquivo `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

> **Adicione a linha `rest_framework` antes da linha referente a aplicação `cadastro`.**
>
> **ATENÇÃO:** O arquivo `settings.py` está na pasta `config`.

## Criando o arquivo de serialização

Vamos criar um arquivo de serialização para a aplicação `alunos`. Clique com o botão direito do mouse na pasta `alunos` e selecione a opção `New File`. Nomeie o arquivo como `serializers.py`.

Adicione o seguinte código ao arquivo `serializers.py`:
```python
from rest_framework.serializers import ModelSerializer
from .models import Estado

class EstadoSerializer(ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'
```

Este código cria um serializador para a classe `Estado`. O serializador é responsável por converter os objetos em JSON.

## Criando as views

Vamos criar as views para a aplicação `alunos`. Abra o arquivo `views.py`, que está na pasta `alunos`, e adicione o seguinte código:
```python
from rest_framework.viewsets import ModelViewSet
from .models import Estado
from .serializers import EstadoSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
```

Este código cria uma view para a classe `Estado`. A view é responsável por listar, cadastrar, atualizar e excluir os objetos.

> _Apenas uma observação importante: O ponto que vai antes das palavras models e serializers é para indicar que os arquivos estão na mesma pasta que o arquivo views.py. Portanto, se os arquivos estiverem em pastas diferentes, é necessário indicar o caminho correto, mas, neste caso, o ponto é suficiente._

## Configurando as rotas

Vamos configurar as rotas para a aplicação `alunos`. Abra o arquivo `urls.py`, que está na pasta `config`, e adicione o seguinte código:
```python
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
```

Este código cria as rotas para a aplicação `alunos`. As rotas são responsáveis por direcionar as requisições para as views corretas.

Nas linhas 6 e 7, criamos um roteador padrão e registramos a view `EstadoViewSet` com o nome `estados`.

Na linha 9, incluímos as rotas do roteador no arquivo de rotas.

A linha 10 mantém a rota para a interface administrativa do Django. Ela é que possibilita que você acesse a URL `http://localhost:8000/admin/`. O admin após a porta corresponde à URL registrada na linha 10. **Não é mágica!**

Agora já é possível acessar a API REST. Execute o seguinte comando no terminal:
```bash
pdm run python manage.py runserver
```

Acesse a URL `http://localhost:8000/estados/` no navegador. Você verá a lista de estados cadastrados.

Também, se você acessar a URL `http://localhost:8000/estado/1/`, verá o estado com o ID 1.

Se você acessar a URL `http://localhost:8000/`, verá então todas as URLs que foram registradas no arquivo `urls.py`. Neste caso, a URL `http://localhost:8000/estados/` é a única que foi registrada e, por isso, é a única que aparece.

Para parar o servidor, pressione `Ctrl + C` no terminal.

# TAREFA

- [ ] Criar a API REST para a aplicação `cidade`.
- [ ] Criar a API REST para a aplicação `aluno`.


## Quando finalizar, não esqueça de publicar o código no GitHub. Avance para a próxima etapa para seguir as orientações 😉

# Etapa 4 - GitHub

Inclusive, não precisa esperar finalizar para publicar, pode ir publicando conforme for fazendo as tarefas. 😉

Porém, se preferir, pode publicar tudo de uma vez só. 🚀

Vai aqui uma dica:

Acesse a URL [gitignore.io](https://www.gitignore.io/) e gere um arquivo `.gitignore` para projetos Python. Este arquivo irá ignorar os arquivos e pastas que não precisam ser versionados.

Neste site, digite `Python` e também `Django` e clique em `Create`. Copie o conteúdo gerado e cole no arquivo `.gitignore` do seu projeto. O arquivo `.gitignore` deve ficar na pasta raiz do projeto.

Depois, siga os passos abaixo para publicar o código no GitHub:

1. No terminal, vá até a pasta do projeto.
2. Execute o comando `git init` para iniciar o repositório Git.
3. Execute o comando `git add .` para adicionar todos os arquivos ao repositório.
4. Execute o comando `git commit -m "Introdução API REST"` para fazer o commit identificando-o pela mensagem adequada.
5. No Visual Studio Code, vá na opção `Source Control` e clique nos três pontinhos `...` e selecione a opção `Push`, ou então `Publish to GitHub`.
6. Indique o nome do repositório.
7. Selecione se deseja que o repositório seja público ou privado.
8. Clique em `Create Repository`.
9. Pronto! Seu código estará publicado no GitHub.

Caso deseja abrir o projeto no repositório, o Visual Studio Code mostrará uma notificação no canto inferior direito. Clique em `Open in GitHub` ou então `Abrir no GitHub`.

Se tiver alguma dúvida, não hesite em me chamar. Estou à disposição para ajudar. 🤗

Claro, esses passos para publicar no GitHub demandam de alguns pré-requisitos. Já é necessário ter seu usuário logado no Visual Studio Code e é preciso ter seu `git config` também configurado.

## Você sabia?

Também é possível executar instruções SQL diretamente no Django, utilizando o comando `pdm run python manage.py dbshell`. Este comando abrirá um shell interativo onde você poderá executar comandos SQL diretamente no banco de dados configurado no seu projeto Django.

> Para executar o comando mencionado acima, certifique-se de que você está acessando a pasta do seu projeto Django no terminal. O comando `dbshell` permite que você interaja diretamente com o banco de dados, facilitando a execução de consultas SQL, inserções, atualizações e exclusões de dados.

Para fazer isso, você deve executar os seguintes passos:
1. Execute o comando `pdm run python manage.py dbshell` no terminal.
2. Você verá um prompt interativo onde poderá digitar comandos SQL.
3. Por exemplo, você pode digitar `SELECT * FROM nome_da_tabela;` para consultar dados de uma tabela específica.
4. Após digitar os comandos, pressione `Enter` para executá-los.
5. Para sair do shell, digite `exit` ou pressione `Ctrl + D`.
6. Para visualizar as tabelas existentes no banco de dados, você pode usar o comando `.tables` já dentro do shell interativo.
7. Para ver a estrutura de uma tabela específica, você pode usar o comando `.schema nome_da_tabela`.
8. Para sair do shell, digite `exit` ou pressione `Ctrl + D`. No Windows, digite `.quit`.

## Agora, ***let's work***!