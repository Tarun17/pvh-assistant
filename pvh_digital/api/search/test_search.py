"""
Testcases for Search
"""

import os
import tempfile
import unittest

from pvh_digital.app import app

class SearchTestCase(unittest.TestCase):
    """
    Test cases for search api
    """

    def setUp(self):
        """
        setup db and test client for test cases
        :return:
        """
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['Testing'] = True
        self.client = app.test_client()


    def test_search(self):
        """
        Ensures that search api is working fine
        :return:
        """
        url = "/api/search/items?q=underwear"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_search_nodata(self):
        """
        Ensures that when result not found response should be 404
        :return:
        """
        url = "/api/search/items?q=no_data"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_search_no_query(self):
        """
        Ensures that q is essesntial parameter
        :return:
        """
        url = "/api/search/items"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 400)

    def test_search_parameters(self):
        """
        Ensures that there could be following search parameters
        :return:
        """
        url = "/api/search/items?q=underwear,page=1,offset=10,sort_by=size,filter=red"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_search_wrong_parameters(self):
        """
        Ensures that parameter key name should be correct
        :return:
        """
        url = "/api/search/items?q_wrong=underwear,page=1,offset=10,sort_by=size,filter=red"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 400)



    def tearDown(self):
        """
        teardown database created in setup
        :return:
        """
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

if __name__ == "__main__":
    unittest.main()

