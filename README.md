# Speedio-test

Desafio Speedio para a vaga de Ciência de Dados. Resultado final do projeto `Speedio-test/excel/estabelecimentos.xlsx`:
<p align="center"><img src="https://user-images.githubusercontent.com/48140546/127709691-efff139d-b47e-4492-8f40-4a20f4fc1151.png"></p>

## Requisitos:

- Este projeto utiliza a ferramenta de terminal `mongoimport`, que precisa ser instalada separadamente do **MongoDB**. Link para download: [MongoDB Database Tools](https://www.mongodb.com/try/download/database-tools/ "MongoDB Database Tools"). Depois de instalada a ferramenta, siga uma das duas seguintes opções:

    - Adicionar o caminho do arquivo ***mongoimport.exe*** a variável de ambiente PATH. Obs: Certifique-se de que o caminho do arquivo está correto. Exemplo:  **C:\ProgramFiles\MongoDB\Tools\100\bin**
    - Substituir o comando `mongoimport` no script `Speedio-test/writer.py (linha 56)` pelo caminho completo do arquivo ***mongoimport.exe***. Exemplo (ANTES/DEPOIS):
<p align="center"><img src="https://user-images.githubusercontent.com/48140546/128960750-9ee00663-3a78-4382-a51b-4e189263514d.png"></p>
<p align="center"><img src="https://user-images.githubusercontent.com/48140546/128960708-ce96f28f-0f6c-4f7e-b904-2cb3c184181b.png"></p>

- Certifique-se de instalar as libs presentes no arquivo `requirements.txt` utilizando o comando `pip install -r requirements.txt` no terminal.
- Finalmente, extraia o zip contendo o arquivo CSV a ser processado no diretório `Speedio-test/raw`. Garanta que o nome do arquivo seja ***K3241.K03200Y0.D10612.csv***.
- Rode o script `Speedio-test/main.py` e aguarde a execução do código. ***Obs***: certifique-se que o **MomgoDB** está rodando corretamente!

## Performance:
O programa levou em média 5~6 minutos para finalizar a execução de acordo com os testes realizados. A máquina utilizada para rodar os testes tem as seguintes especificações: 

- Sistema Operacional: Windows 10 Pro
- Prcessador: i5 9400f (6 núcleos, 2.90 GHz clock base e 4.10 GHz clock max)
- Memória: 8GB DDR4
- Disco: SSD 240GB

***ATENÇÃO:*** O desempenho pode váriar de acordo com o a máquina uitilizada. Quanto mais potente o processador e mais memória RAM disponível, melhor. Também é extremamente recomendável o uso de um SSD no lugar do HD.

## Observações:

Este programa foi desenvolvido e testado no Windows 10. O funcionamento em outros Sistemas Operacionais não é garantido.

**Créditos:** Eduardo Franco
