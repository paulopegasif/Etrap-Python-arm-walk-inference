import requests
import json
from datetime import datetime
import os
# Conversao da imagem para base64
from PIL import Image
import base64
import shutil # Move img


def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    base64_data = base64.b64encode(image_data).decode("utf-8")
    return base64_data




def cadastrar_imagem(api_url, image_path, trap_code):
    #api_url = 'http://10.5.7.165:8000/ws-rest/trapimage'
    #image_path = "D:/phmad/Desktop/20230322_p54_afideo_1_cropped.jpg"
    headers = {'Content-Type': 'application/json'}

    data_atual = datetime.now()
    data_format = data_atual.strftime("%Y-%m-%d")

    base64_image = convert_image_to_base64(image_path)

    nome_arquivo = os.path.basename(image_path)
    #print(f"Nome Arquivo {nome_arquivo}")

    params = {
        "date": data_format,
        "trap": trap_code, #63
        "image_type": 1,
        "image_path": base64_image,
        "image_name_file": nome_arquivo

    }

    response = requests.post(api_url, headers=headers, data=json.dumps(params))
    response_data = response.json()
    print("\n")
    if response.status_code == 201:
        print(f"Status Code: {response.status_code}")
        id_image = response_data["id"]
        print(f"ID: {id_image}")
        print("### Imagem cadastrada com sucesso! ###")
    else:
        print(f"Status Code: {response.status_code}")
        print(response.text) # resposta completa
        print("### Ocorreu um erro ao cadastrar a imagem! ###")
        
    return id_image




# Fazendo inferencia

def fazer_inferencia(id_image, codigo_modelo, aspect_default_img):
    # Parametros default

    #codigo_modelo = 12
    #aspect_default_img = 0


    url_inference = f'http://10.5.7.165:8000/ws-rest/{id_image}/{codigo_modelo}/{aspect_default_img}/detect'
    response_inference = requests.get(url_inference)

    print("\n")
    if response_inference.status_code == 200:
        print(f"Status Code: {response_inference.status_code}")
        print("### OK - Inferência! ###")
    else:
        print(f"Status Code: {response.status_code}")
        print(response.text) # resposta completa
        print("### Ocorreu um erro ao realizar a inferência! ###")

    print("\n")

def change_dir(dirImg, dirSends, image_path):
    # Cria o diretório "img_sends" se não existir
    if not os.path.exists(dirSends):
        os.makedirs(dirSends)

    # Obtém o nome do arquivo da imagem
    nome_arquivo = os.path.basename(image_path)

    # Move a imagem para o diretório "img_sends"
    img_sends_path = os.path.join(dirSends, nome_arquivo)
    shutil.move(image_path, img_sends_path)

    print(f"A imagem foi movida para {img_sends_path}")
    










