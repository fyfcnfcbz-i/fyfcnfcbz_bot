# добавление картинки

import requests  #pip install requests

def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url) #гет запрос на адресс
    if response.status_code: #если статус 200(все хорошо) то
        date = response.json()
        return date.get('image') #достали адрес изображения

if __name__ == '__main__':
    fox()