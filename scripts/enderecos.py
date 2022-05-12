# -*- coding: iso-8859-15 -*-

import json
from urllib import request
from pprint import pprint

def viacep():
    for cep in range(30400000,39999999):
        print(cep, end='')
        with request.urlopen(f'https://viacep.com.br/ws/{cep}/json/') as response:
            html = response.read()
            CEP = json.loads(html.decode('utf-8'))
            if 'erro' in CEP:
                print('\r', end='', flush=True)
                continue
            print(CEP['cep'], CEP['logradouro'])

def logradouros_from_ceps(estado_code, cidade_code):
    bairros = []
    entries = []
    for i in range(1,8):
        req = request.Request(f'http://cep.la/{estado_code}/{cidade_code}/{i}', headers={'Accept':'application/json'})
        with request.urlopen(req) as response:
            html = response.read()
            page = json.loads(html.decode('utf-8'))
            #for bairro in page:
            #    bairros.append(bairro['nome'])
            bairros.extend(page)
    
    for bairro in bairros:
        bairro_ = {
            'nome':bairro['nome'], 
            'logradouros':[]
            }
        for i in range(1,100):
            req = request.Request(f'http://cep.la/{estado_code}/{cidade_code}/{bairro["id"]}/{i}', headers={'Accept':'application/json'})
            with request.urlopen(req) as response:
                data = response.read()
                if len(data)<=2:
                    break
                ceps = json.loads(data.decode('utf-8'))
                for cep in ceps:
                    bairro_['logradouros'].append({
                        'nome': cep['nome'],
                        'cep':cep['cep']
                        })
                    print(cep['cep'], bairro['nome'], cep['nome'])

        entries.append(bairro_)
    json.dump(entries, open(cidade_code+".json", 'w'), indent=2)


logradouros_from_ceps('MG', 'Montes-Claros')