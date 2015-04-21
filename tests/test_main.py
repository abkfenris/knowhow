from test_basics import BasicTestCase


class MainViews(BasicTestCase):
    def test_index(self):
        """
        View the index page (test_main.MainViews)
        """
        rv = self.client.get('/')
        self.assertIn('Hello World', rv.data)

    def test_404(self):
        """
        Test for 404 errors (test_main.MainViews)
        """
        rv = self.client.get('/404')
        self.assertIn('Page Not Found', rv.data)
