import json
from requests import Response
from utils.checking import Checking
from utils.api import Google_maps_api

"""Создание.Изменние.Удаление новой локации"""

class Test_create_place():

    def test_create_new_place(self):

        print("Метод POST")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()   #для получения place_id для метода GET
        place_id = check_post.get("place_id")  #для получения place_id для метода GET

        """Проверка статус кода для метода POST"""
        Checking.check_status_code(result_post, 200)   #для проверки статусов ответов, метод Post
        print(result_post.status_code)
        """Проверка наличия полей в ответе для метода POST"""
        token = json.loads(result_post.text) #получение полей в ответе для основной проверки
        print(list(token)) #получение полей в ответе для основной проверки
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id']) #основная проверка наличия полей после получения полей из двух строк выше.
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = Google_maps_api.get_new_place(place_id)  # получение данных о созданной локации
        """Проверка статус кода для метода GET"""
        Checking.check_status_code(result_get, 200) #для проверки статусов ответов, метод Get
        print(result_get.status_code)
        """Проверка наличия полей в ответе для метода GET POST"""
        token = json.loads(result_get.text) #получение полей в ответе для основной проверки
        print(list(token)) #получение полей в ответе для основной проверки
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
) #основная проверка наличия полей после получения полей из двух строк выше.
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Метод PUT")
        result_put = Google_maps_api.put_new_place(place_id)  # изменение данных о созданной локации
        """Проверка статус кода для метода PUT"""
        Checking.check_status_code(result_put, 200)  # для проверки статусов ответов, метод Get
        print(result_put.status_code)
        """Проверка наличия полей в ответе для метода PUT"""
        Checking.check_json_token(result_put,['msg'])
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get = Google_maps_api.get_new_place(place_id)  # получение данных об обновленной локации
        """Проверка статус кода для метода GET"""
        Checking.check_status_code(result_get, 200)  # для проверки статусов ответов, метод Get
        print(result_get.status_code)
        """Проверка наличия полей в ответе для метода GET PUT"""
        token = json.loads(result_get.text) #получение полей в ответе для основной проверки
        print(list(token)) #получение полей в ответе для основной проверки
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])  # основная проверка наличия полей после получения полей из двух строк выше.
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("Метод DELETE")
        result_delete = Google_maps_api.delete_new_place(place_id)  # удаление данных о созданной локации
        """Проверка статус кода для метода DELETE"""
        Checking.check_status_code(result_delete, 200)  # для проверки статусов ответов, метод DELETE
        # print(result_delete.status_code)
        """Проверка наличия полей в ответе для метода DELETE"""
        Checking.check_json_token(result_delete,['status'])
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_delete, 'status', '200')

        print("Метод GET DELETED")
        result_get = Google_maps_api.get_new_place(place_id)  # получение данных о удаленной локации
        """Проверка статус кода для метода GET"""
        Checking.check_status_code(result_get, 404)  # для проверки статусов ответов, метод Get
        print(result_get.status_code)
        """Проверка наличия полей в ответе для метода GET"""
        Checking.check_json_token(result_get,['msg'])
        """Проверка значений обязательных полей в ответе запроса"""
        Checking.check_json_value(result_get, 'msg', "Delete operation failed, looks like the data doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Тестирование прошло успешно")
