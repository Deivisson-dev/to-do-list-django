Este é o projeto final da disciplina de Algoritmos e Programação de Computadores, que consiste em  um To-Do List usando o framework Django. Este projeto permite aos usuários criar, visualizar, editar e excluir gerenciar suas tarefas diárias em uma lista de afazeres.

Funcionalidades Principais:

    To-Do List:
        Os usuários podem adicionar tarefas à sua lista de afazeres.
        Eles podem marcar as tarefas como concluídas e removê-las quando desejarem.
        A lista de afazeres é atualizada em tempo real.


Como Executar o Projeto

#Clone o repositório para o seu ambiente de desenvolvimento:


    git clone https://github.com/Deivisson-dev/To-do-list.git


#Crie um ambiente virtual:


    python -m venv venv

#Ative o ambiente virtual

    Linux: source venv/bin/activate /  No Windows: venv\Scripts\activate

#Instale as dependências do projeto:


    pip install -r requirements.txt


#Navegue até a pasta do projeto

    cd blog/

#Realize as migrações do banco de dados:

    python manage.py makemigrations
    python manage.py migrate



#Inicie o servidor de desenvolvimento:


    python manage.py runserver

#Acesse a aplicação em seu navegador em http://localhost:8000/.


Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) ou enviar pull requests. Sua contribuição é bem-vinda!
Licença

Este projeto é distribuído sob a licença MIT.