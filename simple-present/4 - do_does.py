###############################################################################
#
# Algoritmos criados para fins educativos no projeto Inglês com Python
# Nos sigam no Instagram e Facebook @inglescompython 
# Aula 04 - Algoritmo Uso do "Do" e "Does"
#
###############################################################################

def do_does(pronome):

    terceira_pessoa_singular = ['He','She','It']

    if(pronome in terceira_pessoa_singular):
        return pronome+" Does"
    else:
        return pronome+ " Do"

todos_pronomes = ["I","You","He","She","It","We","You","They"]

for p in todos_pronomes:
    print(do_does(p))
