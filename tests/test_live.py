"""
Test with a live instance
"""

from flask_testing import LiveServerTestCase

from knowhow import create_app, db


class LiveServerBase(LiveServerTestCase):
    def create_app(self):
        app = create_app('testing')
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.rollback()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
