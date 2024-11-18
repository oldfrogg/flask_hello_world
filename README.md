# Flask - Hello World didático

O objetivo deste repositório é auxiliar e ensinar a fazer um simples Hello World em Flask.
Assim, é possível auxiliar os iniciantes a começar a usar este micro framework.

## Rotas
* / - GET - Página inicial, que mostra o "Hello, world!"

## Execução

**_O recomendável para quem está iniciando, é seguir os passos a partir do arquivo "app.py", deste repositório.
A execução seguindo o passo-a-passo a seguir deve ser feita em caso de ter algum problema seguindo o "app.py"._**


Caso queira executar o arquivo pronto, basta seguir a partir daqui:

O primeiro passo é fazer o download dos arquivos na pasta desejada.

Agora abra o diretório em seu ambiente de programação.

Para executar a aplicação, é recomendável realizar a instalação dos pacotes necessários e executá-lo em um ambiente virtual.

Para criar um ambiente virtual é necessário navegar no terminal até o diretório da aplicação e dar o comando:
```
> python -m venv venv
```

Além de criar é necessário deixá-lo ativado para a instalação das bibliotecas e execução da aplicação.

Para ativar o ambiente virtual, faça o  seguinte:

No Windows:

```
> .\venv\Scripts\activate
```
    
No Linux:
    
```
> source venv/bin/activate
```

Pronto, agora deve aparecer um "(venv)" no início da sua linha de comando no terminal. 

Isso indica que o ambiente virtual está ativo.

Caso queira desativá-lo, basta executar:
```
> deactivate
```


Agora, com o ambiente virtual ativo, você deve instalar as bibliotecas necessárias na aplicação.

Para isso, execute o comando:
```
> pip install -r requirements.txt
```

Com isso, a aplicação estará pronta para a execução.



Por fim, para executar a aplicação, basta executar o flask da seguinte forma:
```
> flask run
```

Com isso a aplicação ficará ativa em um servidor local. Você poderá acessá-lo através do navegador utilizando:
    <http://localhost:5000>
ou:
    <http://127.0.0.1:5000/>
