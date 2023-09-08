Este é o projeto final da disciplina de Algoritmos e Programação de Computadores, que consiste em  um blog com funcionalidade de To-Do List usando o framework Django. Este projeto permite aos usuários criar, visualizar, editar e excluir postagens de blog, bem como gerenciar suas tarefas diárias em uma lista de afazeres.
Funcionalidades Principais

    Postagens de Blog:
        Os usuários podem criar postagens de blog com título, conteúdo e data de publicação.
        Eles podem editar e excluir suas próprias postagens.
        As postagens são exibidas em ordem cronológica inversa (a mais recente no topo).

    To-Do List:
        Os usuários podem adicionar tarefas à sua lista de afazeres.
        Eles podem marcar as tarefas como concluídas e removê-las quando desejarem.
        A lista de afazeres é atualizada em tempo real.

Requisitos de Instalação

    Django 3.x
    Outras dependências (verifique o arquivo requirements.txt)

Como Executar o Projeto

    Clone o repositório para o seu ambiente de desenvolvimento:

bash

git clone https://github.com/Deivisson-dev/FuturoTech.git

    Navegue até a pasta do projeto:

bash

cd FuturoTech

    Crie um ambiente virtual (recomendado) e ative-o:

bash

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

    Instale as dependências do projeto:

bash

pip install -r requirements.txt

    Realize as migrações do banco de dados:

bash

python3 manage.py migrate

    Crie um superusuário para acessar a interface de administração:

bash

python3 manage.py createsuperuser

    Inicie o servidor de desenvolvimento:

bash

python manage.py runserver

    Acesse a aplicação em seu navegador em http://localhost:8000/.

Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:


Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) ou enviar pull requests. Sua contribuição é bem-vinda!
Licença

Este projeto é distribuído sob a licença MIT.