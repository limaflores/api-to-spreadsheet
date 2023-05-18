import pandas as pd
import json
import requests
from openpyxl import Workbook
from datetime import datetime

def main():
    try:
        url = 'https://my-json-server.typicode.com/limaflores/my-fake-api/data'
        response = requests.get(url)
        json_data = response.json()

        events = json_data
        event_list = []

        for event in events:
            event_info = {
                'id': event['id'],
                'start_date': event['start_date'],
                'end_date': event['end_date'],
                'name': event['name'],
                'detail': event['detail'],
                'private_event': event['private_event'],
                'published': event['published'],
                'cancelled': event['cancelled'],
                'image': event['image'],
                'url': event['url'],
                'address_name': event['address']['name'],
                'address_address': event['address']['address'],
                'address_address_num': event['address']['address_num'],
                'address_address_alt': event['address']['address_alt'],
                'address_neighborhood': event['address']['neighborhood'],
                'address_city': event['address']['city'],
                'address_state': event['address']['state'],
                'address_zip_code': event['address']['zip_code'],
                'address_country': event['address']['country'],
                'host_name': event['host']['name'],
                'host_description': event['host']['description'],
                'category_prim_name': event['category_prim']['name'],
                'category_sec_name': event['category_sec']['name']
            }
            event_list.append(event_info)

        df_events = pd.DataFrame(event_list)
        wb = Workbook()
        ws = wb.active
        ws.append(['ID', 'Data de Início', 'Data de Término', 'Nome', 'Detalhes', 'Evento Privado',
                   'Publicado', 'Cancelado', 'Imagem', 'URL', 'Nome do Endereço', 'Endereço', 'Número',
                   'Complemento', 'Bairro', 'Cidade', 'Estado', 'CEP', 'País', 'Nome do Anfitrião',
                   'Descrição do Anfitrião', 'Categoria Primária', 'Categoria Secundária'])

        for _, row in df_events.iterrows():
            ws.append([
                row['id'], row['start_date'], row['end_date'], row['name'], row['detail'], row['private_event'],
                row['published'], row['cancelled'], row['image'], row['url'], row['address_name'],
                row['address_address'], row['address_address_num'], row['address_address_alt'],
                row['address_neighborhood'], row['address_city'], row['address_state'],
                row['address_zip_code'], row['address_country'], row['host_name'], row['host_description'],
                row['category_prim_name'], row['category_sec_name']
            ])

        datanow = datetime.now()
        wb.save(f'dados_api_{datanow.strftime("%Y-%m-%d_%H-%M-%S")}.xlsx')

    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
