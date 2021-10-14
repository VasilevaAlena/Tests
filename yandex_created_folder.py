from yandex import token
import requests


url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + token}
new_folder = 'test'


def created_folder(new_folder):
    params = {'path': new_folder}
    result = requests.put(url, headers=headers, params=params)
    return result.status_code

def info_folder(new_folder):
    params = {'path': new_folder}
    result = requests.get(url, headers=headers, params=params)
    return result.status_code


if __name__ == '__main__':
    print(created_folder(new_folder))
    print(info_folder(new_folder))
