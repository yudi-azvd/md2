# Matemática Discreta 2

Repositório para a disciplina de Matemática Discreta 2 da Universidade de Brasília.

Esse repositório tem a implementações de algumas funções e algoritmos que me 
ajudaram a estudar o conteúdo.

## Instalação 

Você precisa do [Python 3.10+](https://www.python.org/downloads/) 
instalado em seu computador. Se você já o tem, instale as dependências:

```sh
pip install -r requirements.txt
```

## Uso

Para rodar o programa que resolve sistema de equações de congruência, execute:

```sh
python -m md2.tcr samples/input1.csv
```

Leia mais sobre esse programa em [tcr.py](md2/tcr.py).

## Testes
Execute todos os testes:

```sh
pytest
```

Execute todos os testes com o padrão:

```sh
# congruence_eq vai dar match com o arquivo test_congruence_eq
pytest -k congruence_eq
```

Execute um caso de teste :

```sh
pytest -k "congruence_eq[3-1-4-3]"
```

Para entender o comando anterior, observe como os dados dos testes parametrizados
são apresentados na listagem dos testes:

```sh
pytest --collect-only
```
