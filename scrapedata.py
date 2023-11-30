import json
import requests
from io import BytesIO
from PIL import Image
from Criminal import Criminal
from Upload_data import upload_data


def scrape_data():
    with open('data.json') as f: 
        json_data = json.load(f)

    criminaldata = json_data['_embedded']['notices']
    criminalslist = []

    for criminal in criminaldata:
        for i in criminal:
            if i == '_links':
                imageurl = criminal[i]['thumbnail']['href']
                response = requests.get(imageurl)
                image = Image.open(BytesIO(response.content))
                rgb_im = image.convert('RGB')
                rgb_im.save(f"./images/criminalpic_{criminal['name']}.png")
                geturl = f"https://storage.cloud.google.com/interpol_criminal_pics/images/criminalpic_{criminal['name']}.png?authuser=1"
                tableid = "interpol_criminals_list"
                datasetid = "interpol_criminals"
                model_criminal = Criminal(date_of_birth=criminal['date_of_birth'], nationalities=criminal['nationalities'][0], entity_id=criminal['entity_id'], forename=criminal['forename'], name=criminal['name'], image=geturl)
                dict_data = model_criminal.dict()
                print(dict_data.date_of_birth)
                if dict_data.date_of_birth is not None and dict_data.nationalities is not None and dict_data.entity_id is not None and dict_data.forename is not None and dict_data.name is not None:
                    criminalslist.append(dict_data)

    upload_data(dataset_id=datasetid, table_id=tableid, data=criminalslist)

scrape_data()