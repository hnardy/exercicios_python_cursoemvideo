# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests
try:
    url = "https://www.google.com"
    t = requests.get(url).status_code

except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print('o site  não está disponivel ou você está sem internet')

else:
    if t == 200:
        print('o site está operando normalmente')
    else:
        print(f' o site está operando no status {t}')
# o professor resolveu com a biblioteca urllib