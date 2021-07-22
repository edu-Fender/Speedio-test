# Speedio-test

Desafio Speedio para a vaga de Ciência de Dados.

## Requisitos:

- Este projeto utiliza o comando de terminal `mongoimport`, que precisa ser instalado separadamente do MongoDB. Link para download: [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools/ "MongoDB Database Tools"). Depois de instalado o conjunto de ferramentas, siga uma das seguintes opções:

    - Adicionar o diretório do arquivo mongoimport.exe a variável de ambiente PATH. Obs: Certifique-se de que o diretório esta correto. Exemplo:  **C:\ProgramFiles\MongoDB\Tools\100\bin**
    - Substituir o comando `mongoimport` no arquivo `Speedio-test/insert_mongodb.py` (linha 45) pelo caminho completo do arquivo mongoimport.exe no **seu** sistema. Exemplo:

<p align="right"><img src="https://user-images.githubusercontent.com/48140546/126717270-02b85358-a404-4a1f-bb8a-cf0fc5064ed9.png"></p>

- Certifique-se de instalar as libs Pandas e PyMongo presentes no arquivo `requirements.txt` utilizando o comando `pip install -r requirements.txt` na linha de comando.
- Finalmente, extraia o zip contendo o arquivo CSV a ser processado no diretório `Speedio-test/raw`.
- Rode o script `Speedio-test/main.py` e aguarde a execução do código. Atenção: certifique-se que o **MongoDB** está instalado e rodando corretamente!

## Observações:
Este programa processa arquivos extremamente pesados. Por este motivo, a execução do código pode demorar algum tempo, o que é normal. O tempo de execução pode variar em até 40 minutos dependendo das especificações de hardware. 

---

**Créditos:** Eduardo Franco