import unittest
from app import is_alive_host, formaturl


class TestStringMethods(unittest.TestCase):

    expected_hostname = 'http://yandex.ru'

    def test_live(self):
        self.assertTrue(is_alive_host('semrush.com'))

    def test_down(self):
        self.assertFalse(is_alive_host('invalid.domain.son'))

    def test_format_wrong(self):
        actual_hostname = formaturl('yandex.ru')
        self.assertEqual(TestStringMethods.expected_hostname, actual_hostname)

    def test_format_correct(self):
        actual_hostname = formaturl('http://yandex.ru')
        self.assertEqual(TestStringMethods.expected_hostname, actual_hostname)


if __name__ == '__main__':
    unittest.main()