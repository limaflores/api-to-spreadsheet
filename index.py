import pandas as pd
import json
import requests
import gspread
from openpyxl import Workbook
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account

def main():
    try:
        # Server API
        url = 'https://my-json-server.typicode.com/limaflores/my-fake-api/data'
        response = requests.get(url)
        events = response.json()
        adress = []
        for event in events:
            adress_event = event['address']
            adress_event['event_name'] = event['name']
            adress.append(adress_event)
        df_adress = pd.DataFrame(adress)
        wb = Workbook()
        ws = wb.active
        ws.append(['Nome do Evento', 'Endereço', 'Número', 'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'País'])
        for i, row in df_adress.iterrows():
            ws.append([row['event_name'], row['address'], row['address_num'], row['address_alt'], 
                    row['neighborhood'], row['city'], row['state'], row['zip_code'], row['country']])

        wb.save('dados_api.xlsx')
        
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()

