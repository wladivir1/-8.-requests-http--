import requests

# В файл token нужно прописать свой токе яндекс диска    
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': 'OAuth ' + self.token}
        params = {'path': file_path}
        response = requests.get(url, headers=headers, params=params)
                
        if 200 <= response.status_code < 300:   
            date = response.json()
            url = date['href']
                       
            with open(file_path, 'rb') as f:
                responses = requests.post(url, files={'file': f})
                    
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'text4.txt'  # Прописываем название файла который нужно записать (файл должен находится в том же катологе)
    token = open('token', encoding='utf8').read() 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)