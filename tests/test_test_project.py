#!/usr/bin/env python3

"""Tests for `test_project`"""

import pytest

from test_project import test_project


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/engineervix/cookiecutter-pyproject')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


class TestTest_project():
    """Tests the test_project module"""

    @staticmethod
    def test_addition():
        """tests for addition"""
        assert test_project.add(2, 2) == 4  # nosec

    @staticmethod
    def test_subtraction():
        """tests for subtraction"""
        assert test_project.subtract(4, 2) == 2  # nosec
