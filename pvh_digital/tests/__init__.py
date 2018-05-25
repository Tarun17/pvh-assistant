# -*- coding: utf-8 -*-
"""
    __init__

    Test Suite for pvh_digital


"""
import pytest
from pvh_digital.api.sample.endpoints.test.test_items import TestSampleItemAPI


def suite():
    """Create a test suite and return it for better manageability"""
    suite = pytest.TestSuite()
    suite.addTests([
        pytest.TestLoader().loadTestsFromTestCase(TestSampleItemAPI)
    ])
    return suite
