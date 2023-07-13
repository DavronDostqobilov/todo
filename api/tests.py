from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Category,Task
from rest_framework import status
# Create your tests here.
class TaskListTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="davron", password="1234")
        self.category=Category.objects.create(name="Working",user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        response=self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 1, 'username': 'davron', 'tasks':[]})

    def test_post(self):
        response=self.client.post('/api/tasks/',{ 'title': 'test task',"user": 1 ,"category":1}, format='json')
        self.assertEqual(response.status_code, 201)

class TaskDetailTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="davron", password="1234")
        self.category=Category.objects.create(name="Working",user=self.user)
        self.task = Task.objects.create(user=self.user, category=self.category,title='Ishlar',description='',completed=False)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        response = self.client.get('/api/tasks/1/')
        self.assertEqual(response.status_code,200)

    def test_put(self):
        response=self.client.put('/api/tasks/1/',{ 'title': 'test task',"user": 1,"category": 1}, format='json')
        self.assertEqual(response.status_code,200)

    def test_delete(self):
        response = self.client.get('/api/tasks/1/')
        self.assertEqual(response.status_code,200)

class CotegoryViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="davron", password="1234")
        self.category=Category.objects.create(name="Working",user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_get(self):
        response=self.client.get('/api/category/')
        self.assertEqual(response.status_code,200)

    def test_post(self):
        data=  {"id":1,"name": "Working","user": 1}
        response=self.client.post( '/api/category/' , data , format='json' )
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        data={"name": "Doimiy"}
        response=self.client.put('/api/category/1/',data,format='json')
        self.assertEqual(response.status_code,200)

    def test_delete(self):
        response=self.client.delete('/api/category/1/')
        self.assertEqual(response.status_code, 204)

