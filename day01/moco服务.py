import unittest
import requests

class MockLoginTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:12306'

    def tearDown(self):
        pass

    def getUrl(self, path):
        return self.url + path

    def getToken(self):
        """获取token"""
        data = {
            "username": "admin",
            "password": "admin",
            "roleID": 22
        }
        r = requests.post(self.getUrl('/login'), json=data)
        return r.json()['token']

    def test_login(self):
        """验证登录接口"""
        data = {
            "username": "admin",
            "password": "admin",
            "roleID": 22
        }
        r = requests.post(self.getUrl('/login'), json=data)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main(verbosity=2)