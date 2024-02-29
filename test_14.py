import unittest
from lab14 import read_file_content, get_password_from_json, try_open_bad_file  # Replace 'your_module' with the name of your Python file containing the function

class TestReadFileContent(unittest.TestCase):


    
    def test_read_content(self):
        result = read_file_content()   
        self.assertEqual(result, '"Hello There"')
    
    def test_get_password(self):
        result = get_password_from_json()
        self.assertEqual(result, "Pa$$W0rd!!")


    def test_file_unicode_decode_error(self):
        result = try_open_bad_file()
        self.assertEqual(result, "Error: Can't Read file")

    

    


if __name__ == '__main__':
    unittest.main()
