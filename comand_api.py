import requests

#funcion para la solicitud de api para imagenes de patos
def get_duck_image():
    url = 'https://random-d.uk/api/random'
    res =  requests.get(url)
    data = res.json()
    return data['url']
#funcion de consulta API am¿nime
def get_anime_image(query):
    url = ' https://kitsu.io/api/edge/anime'
    params = {
        'filter[text]' : query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        print(f"Error: {response.status_code}")
        return None