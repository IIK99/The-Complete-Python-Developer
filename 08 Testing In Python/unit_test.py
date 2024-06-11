import unittest

import script


class TestMain(unittest.TestCase):
    """Test Hallooo..."""

    def setUp(self):
        print("Setup, about to test a function")

    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "shkshks"
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def test_do_stuff4(self):
        test_param = ""
        result = script.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        print("tearDown, done testing a function")


if __name__ == "__main__":
    unittest.main()
