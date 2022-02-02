# white space or empty string check
def name(self, value):
    if value.strip() == "":
        raise ValueError("error message")
    self._name = value


import unittest


# Основа на тестването
class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
