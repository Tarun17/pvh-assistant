#!/usr/bin/env python3

"""Tests for Sample API"""

import pytest
import json
import unittest
from pvh_digital import app


class TestSampleItemAPI(unittest.TestCase):
    """Tests with DB."""

    def setUp(self):
        """Stuff to do before every test."""
        print(app.app)
        self.client = app.app.test_client()

    def tearDown(self):
        """Do at end of every test."""
        pass

    def test_get_sample_item(self):
        """Test retrieving sample item from db"""

        result = self.client.get("/sample/items/1")
        self.assertEqual(result.status_code, 404)

    def test_put_sample_item(self):
        """Test retrieving todo item from db"""

        result = self.client.get("/sample/1")
        self.assertEqual(result.status_code, 404)

    def test_delete_sample_item(self):
        """Test posting a todo item"""

        result = self.client.post("/sample/item/1",
                                  data=json.dumps({
                                    "name": "Clean apartment",
                                    "description": "Sweep, do dishes"
                                  }),
                                  content_type='application/json')

        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
