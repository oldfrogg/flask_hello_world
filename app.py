# Hello World em Python

# Via prompt:
# - Abrir diretório
# - Criar o arquivo app.py 
# - Criar o ambiente virtual: >python -m venv venv /// ou python3 -m venv venv
# - Abrir o ambiente virtual: >.\venv\Scripts\activate (WINDOWS)  /// source venv/bin/activate (LINUX)
# - Instalar o Flask: >pip install flask

from flask import Flask # Importo o Flask para criar e gerenciar a aplicação

app = Flask(__name__) # Instancio o aplicativo base do Flask (é como criar a aplicação Flask), com __name__ indicando o nome do módulo atual, com isso consigo configurar rotas e outras funcionalidades básicas de um aplicativo Flask

@app.get('/') # Defino a rota
def home(): # Nomeio e defino a função dessa rota
    return 'Hello, World!' # Retorno da função e rota

if __name__ == '__main__':  # Verifica se à variável especial __name__ foi atribuído valor de '__main__', ou seja, se foi executada, e não importada
    app.run(debug=True) # Respeitando a condição, a aplicação é executada, em modo de desenvolvedor



# Quando um arquivo Python é executado, a variável especial __name__ é atribuída automaticamente. Ela pode ter dois valores principais:
# '__main__': Se o arquivo Python foi executado diretamente pelo usuário (por exemplo, com o comando python app.py), o valor de __name__ será '__main__'.
# Nome do módulo: Se o arquivo for importado como um módulo em outro arquivo (por exemplo, import app), o valor de __name__ será o nome do arquivo ou módulo, sem a extensão .py.
# Isso é usado para evitar que código destinado à execução direta seja executado ao importar o arquivo como módulo.
