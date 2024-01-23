from rest_framework import status

from vehicle.models import Car
from rest_framework.test import APITestCase


class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_car(self):
        """Тестирование создания машины"""
        data = {
            'title': 'test',
            'description': 'desc test'
        }
        response = self.client.post(
            path='/cars/',
            data=data
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            first=response.json(),
            second={'id': 1, 'milage': [], 'title': 'test', 'description': 'desc test', 'owner': None}
        )

        self.assertTrue(Car.objects.all().exists())

    def test_list_car(self):
        """Тестирование вывода списка машин"""
        Car.objects.create(
            title='list_test',
            description='list desc test'
        )
        response = self.client.get('/cars/', )
        self.assertEqual(first=response.status_code, second=status.HTTP_200_OK)

        self.assertEqual(
            first=response.json(),
            second=[{'id': 2, 'milage': [], 'title': 'list_test', 'description': 'list desc test', 'owner': None}])
