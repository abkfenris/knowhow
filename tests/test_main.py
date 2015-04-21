from test_basics import BasicTestCase


class MainViews(BasicTestCase):
    def test_index(self):
        """
        View the index page (test_main.MainViews)
        """
        rv = self.client.get('/')
        print(rv.data)
        self.assertIn('Hello World', rv.data)
