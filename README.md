# Speedio-test

Desafio Speedio para a vaga de Ciência de Dados. Resultado final do projeto `Speedio-test/excel/estabelecimentos.xlsx`:
<p align="center"><img src="https://user-images.githubusercontent.com/48140546/127709691-efff139d-b47e-4492-8f40-4a20f4fc1151.png"></p>

## Requisitos:

- Este projeto utiliza o comando de terminal `mongoimport`, que precisa ser instalado separadamente do **MongoDB**. Link para download: [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools/ "MongoDB Database Tools"). Depois de instalado o conjunto de ferramentas, siga uma das seguintes opções:

    - Adicionar o caminho do diretório do arquivo recém istalado ***mongoimport.exe*** a variável de ambiente PATH. Obs: Certifique-se de que o caminho do arquivoestá correto. Exemplo:  **C:\ProgramFiles\MongoDB\Tools\100\bin**
    - Substituir o comando `mongoimport` no script `Speedio-test/insert_mongodb.py (linha 44)` pelo caminho completo do arquivo recém istalado ***mongoimport.exe***. Exemplo:
<p align="center"><img src="https://user-images.githubusercontent.com/48140546/127712741-dad3a878-fad2-4e63-8c1b-38e43d3e8546.png"></p>

- Certifique-se de instalar as libs presentes no arquivo `requirements.txt` utilizando o comando `pip install -r requirements.txt` no terminal.
- Finalmente, extraia o zip contendo o arquivo CSV a ser processado no diretório `Speedio-test/raw`. Garanta que o nome do arquivo seja ***K3241.K03200Y0.D10612.csv***.
- Rode o script `Speedio-test/main.py` e aguarde a execução do código. ***Obs***: certifique-se que o **MongoDB** está instalado e rodando corretamente!

## Performance:
O programa levou em média 5~6 minutos para finalizar a execução de acordo com os testes realizados. A máquina utilizada para rodar os testes tem as seguintes especificações: 

- Sistema Operacional: Windows 10 Pro
- Prcessador: i5 9400f (6 núcleos, 2.90 GHz clock base e 4.10 GHz clock max)
- Memória: 8GB DDR4
- Disco: SSD 240GB

***ATENÇÃO:*** O desempenho pode váriar de acordo com o a máquina uitilizada. Quanto mais potente o processador e mais memória RAM disponível, melhor. É extremamente recomendável que o sistema possua um SSD.

## Observações:!


Este programa foi desenvolvido e testado no Windows 10. O funcionamento em outros Sistemas Operacionais não é garantido.

**Créditos:** Eduardo Franco
