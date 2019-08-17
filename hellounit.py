import unittest
# Could use Nose instead of unittest
# from numpy.testing import assert_almost_equal
# from numpy.testing import assert_array_equal
# from numpy.testing import assert_array_almost_equal
# from numpy.testing import assert_array_less
# from numpy.testing import assert_approx_equal


import numpy as np


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_np_array_equal(self):
        a = np.array([1, 2, 3])
        b = np.array([1, 2, 3])
        try:
            np.testing.assert_array_equal(a, b)
            res = True
        except AssertionError as err:
            res = False
            print(err)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
