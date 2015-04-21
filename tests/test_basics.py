import unittest
from flask import current_app

from knowhow import create_app, db


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        self.app_context.pop()


class AppTest(BasicTestCase):

    def test_app_exists(self):
        """
        App exists (test_basics.AppTest)
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        App is in testing config (test_basics.AppTest)
        """
        self.assertTrue(current_app.config['TESTING'])
