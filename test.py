import unittest
import app

class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.app.Testing= True
        self.app = app.app.test_client()

    def test_math(self):
        response = self.app.get('/math/3/*/2')
        self.assertEqual(response._status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
