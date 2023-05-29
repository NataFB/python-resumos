endereco = "Rua Rui Barbosa 110, Maruipe, Vitória, ES, 29043-020"
import re #Regular expression -- reqEx

#5 digitos + hífen (opcional) + 3 digitos
#o ? significa que é opcional aquele padrão anterior
#o {} é quantidade de repetições do padrão
#o - entre 0 e 9 significa que pode ser qualquer algaritmo entre 0 e 9
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") 

busca = padrao.search(endereco) #retorna Match ou none 

if busca:
    cep = busca.group()
    print(cep)