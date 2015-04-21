import requests

from test_live import LiveServerBase


class MainHTMLLive(LiveServerBase):
    def test_server_running(self):
        """
        Server is alive (test_live_main.MainHTMLLive)
        """
        r = requests.get(self.get_server_url())
        self.assertEqual(r.status_code, 200)


class MainJsonLive(LiveServerBase):
    def test_404_json(self):
        """
        Test that 404 error will return json
        """
        headers = {'Accept': 'application/json'}
        r = requests.get('{server}/404'.format(server=self.get_server_url()),
                         headers=headers)
        self.assertEqual(r.status_code, 404)
        self.assertIn('error', r.json())
