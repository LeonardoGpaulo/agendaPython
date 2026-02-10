# Agenda em Python usando Flask

Este projeto foi elaborado e desenvolvido para permitir o aprendizado de padrão de projetos MVC (Model-View-Controller), framework Flask e seus componentes, váriaveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguaguem de programação Python.

para implementar este projeto localmente, siga os seguintes passos:

1. Faça um fork deste repositório, clicando o botão `Fork`

2. Clone seu repositório localmente:

    ~~~bash
    git clone <url_seu_repositorio>
    ~~~

3. Abrao projeto utlizando seu IDE preferido

4. Crie um ambiente virtual (opcional) utilizando uma versão do Python >= 3.12.10:

    ~~~bash
    python -m venv .venv
    ~~~

5. Ative seu ambiente virtual.

    No bash:

    ~~~bash 
    source .venv/Scripts/activate
    ~~~

    No PowerShell:

    ~~~powershell
    .\.venv\Scripts\Activate.ps1
    ~~~

6. Instale todas as dependências constantes no `requirements.txt`:

    ~~~Python
    pip install -r requirements.txt
    ~~~

7. Copie o arquvio `.env.example`, cole na raiz do projeto e renomeie a cópia para `.env`.

8. Edite o arquivo `.env` para definir o caminho do seu banco de dados na constante `DATABASE`. Exemplo:

    ~~~env
    DATABASE='./data/meubanco.db'
    ~~~

9. Rode a aplicação no Python utilizando o comando:

    ~~~bash
    flask run 
    ~~~

10. Acesse a aplicação no endereço e porta inidicados no terminal. Exemplo: `http://127.0.0.1:5000`