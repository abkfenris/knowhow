from test_basics import BasicTestCase


class AdminViews(BasicTestCase):
    def test_index(self):
        """
        Test the admin index page (test_admin.AdminViews)
        """
        rv = self.client.get('/admin/')
        self.assertIn('Knowhow', rv.data)
