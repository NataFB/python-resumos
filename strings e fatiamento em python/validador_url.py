#https://www.bytebank.com.br/cambio
import re

url = 'https://www.bytebank.com.br/cambio'
#(tem que ser exatamente o que tem dentro), [pode ser qualquer um dos que tem dentro]
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é válida.")

print("A URL é válida")
