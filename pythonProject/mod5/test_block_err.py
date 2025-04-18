import unittest
from mod5.Task3 import BlockErrors


class TestErrors(unittest.TestCase):
    def setUp(self):
        pass

    def test_subclass(self):
        errors_types = {ZeroDivisionError}
        try:
            with BlockErrors(errors_types):
                result = 1 / '0'
        except Exception:
            self.assertTrue(issubclass(*errors_types, Exception))

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            with BlockErrors({TypeError}):
                result = 1 / 0


if __name__ == '__main__':
    unittest.main()
