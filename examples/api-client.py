import requests
import json

url = 'http://127.0.0.1:5000/generateTTS'  # Убедитесь, что замените это на ваш реальный URL

data = {
    'message': 'Привет мир',
    'is_russian': True
}

response = requests.post(url, json=data)
if response.status_code == 200:
    with open('output.mp3', 'wb') as f:
        f.write(response.content)
    print('Файл успешно сохранен как output.mp3')
else:
    print(f'Ошибка: {response.status_code}, {response.json()}')
