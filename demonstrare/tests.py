import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_index(self):
        from .views.core import index
        request = testing.DummyRequest()
        info = index(request)
        self.assertEqual(info['year'], 2015)
