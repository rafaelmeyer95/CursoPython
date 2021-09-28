import pycep_correios

endereco = input('Digite seu CEP (somente números): ')
endereco = pycep_correios.get_address_from_cep(endereco)

print('Você mora em {} - {}, {} - Bairro: {}.'.format(endereco['cidade'],endereco['uf'],endereco['logradouro'],endereco['bairro']))
