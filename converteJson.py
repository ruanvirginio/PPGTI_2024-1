import csv
import json

def csv_to_json(csv_file):
    json_data = []

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Situação'] == 'ATIVA':
                json_row = {
                    "nome": row['Nome'],
                    "longLat": [float(row['Longitude']), float(row['Latitude'])],
                    "nomeFantasia": row['Fantasia'],
                    "endereco": {
                        "rua": row['Tipo_Logradouro'] + ' ' + row['Logradouro'],
                        "numero": row['Número'],
                        "bairro": row['Bairro'],
                        "municipio": row['Município'],
                        "estado": row['UF']
                    }
                }
                json_data.append(json_row)

    return json_data

def main():
    csv_file = "resultado.csv"  # Substitua "dados.csv" pelo caminho do seu arquivo CSV
    json_data = csv_to_json(csv_file)
    with open("dados.json", 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
