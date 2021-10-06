# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros.
# b) Os últimos 4 colocados
# c) Times em ordem alfabética
# d) Em que posição está o time do São Paulo.

times = ('Atlético-MG','Palmeiras','Flamengo','Fortaleza','Bragantino',
         'Corinthians','Internacional','Fluminense','Athlerico-PR',
         'Atlético-GO','Cuiabá','Ceará SC','São Paulo','América-MG',
         'Juventude','Bahia','Santos','Grêmio','Sport Recife','Chapecoense')

print(f'Os cinco primeiros classificados são: {times[0:5]}')
print(f'\nOs quatro últimos classificados são: {times[-4:]}')
print(f'\nTimes em ordem alfabética: {sorted(times)}')
print(f'\nO São Paulo está na {times.index("São Paulo")+1}ª posição.')

