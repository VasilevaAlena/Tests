import unittest
from yandex_created_folder import created_folder, info_folder


class TestYandexCreatedFolder(unittest.TestCase):

    def test_created_folder_Test(self):
        result = created_folder(new_folder="Test")
        self.assertTrue(result == 201)
        print(f'Сервер ответил: {result}')


    def test_created_folder_Test2(self):
        result = created_folder(new_folder="Test2")
        self.assertTrue(result == 201)
        print(f'Сервер ответил: {result}')

    def test_created_folder_test_Test_negativ(self):
        result = created_folder(new_folder="Test")
        self.assertTrue(result != 201)
        print(f'Сервер ответил: {result}')

    def test_created_folder_test_mistake409(self):
        result = created_folder(new_folder="Test")
        self.assertTrue(result == 409)
        print(f'Сервер ответил: {result}')

    def test_info_folder_Test(self):
        result = info_folder(new_folder="Test")
        self.assertTrue(result == 200)
        print(f'Сервер ответил: {result}')

    def test_info_folder_search_Test3(self):
        result = info_folder(new_folder="Test3")
        self.assertTrue(result != 200)
        print(f'Сервер ответил: {result}')

    def test_info_folder_mistake404(self):
        result = info_folder(new_folder="Test3")
        self.assertTrue(result == 404)
        print(f'Сервер ответил: {result}')


if __name__ == '__main__':
    unittest.main()
