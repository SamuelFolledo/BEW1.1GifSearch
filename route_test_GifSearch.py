from app import app #import out app.py
import unittest

class AppTests(unittest.TestCase):
    def setUp(self): #must have to set up test environment
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/') #sends HTTP GET request to the application on the specified path
        self.assertEqual(result.status_code, 200) #assert the status code of the response

if __name__ == "__main__": #runs the test
    unittest.main()