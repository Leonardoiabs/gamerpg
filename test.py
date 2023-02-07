import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamerpg.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from gamerpg.settings import BASE_DIR
import requests
import json
import re
from card.models import Card, Tipo

response = requests.get("https://api.scryfall.com/cards/search?q=c%3Awhite+cmc%3D1")
data_json = json.loads(response.content)

dados = data_json["data"]
count = 0

for dado in dados:
    Tipo.objects.update_or_create(
        nome=str(dado["type_line"]).upper(),
        defaults={'nome': str(dado["type_line"]).upper()}
    )

count = 0
for dado in dados:
    try:
        if int(dado["power"]) >= 0 and int(dado["toughness"]) >= 0:

            namefile = str(re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', str(dado["name"]))).replace(' ', '_')
            file_name = '%s/%s.%s' % (os.path.join(BASE_DIR, 'www/statics/media/cards'), namefile.lower(), 'jpg')
            with open(file_name, 'wb') as imagem:
                resposta = requests.get(dado["image_uris"]["png"], stream=True)

                if not resposta.ok:
                    print("Ocorreu um erro, status:", resposta.status_code)
                else:
                    for dado_img in resposta.iter_content(1024):
                        if not dado_img:
                            break
                        imagem.write(dado_img)

            tipo = Tipo.objects.filter(nome=str(dado["type_line"]).upper()).first()
            Card.objects.create(
                nome=dado["name"],
                imagem='%s/%s.%s' % ('cards', namefile.lower(), 'jpg'),
                tipo=tipo,
                descricao=dado["oracle_text"],
                ataque=dado["power"],
                defesa=dado["toughness"]
            )
            count += 1
    except:
        pass

    print(count)
