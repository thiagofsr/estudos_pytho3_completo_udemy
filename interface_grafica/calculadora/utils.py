import re

# ^começa, $ termina, entre 0 e 9, ou ponto
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

# verifica se esta de acordo com o regex acima
def isNUmOrDot(string:str):
    return bool(NUM_OR_DOT_REGEX.search(string))

# verifica se não esta vazio
def isEmpty(string:str):
    return len(string) == 0