#!/usr/bin/env python3
"""
client testing
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    testing GithubOrgClient class
    """

    def mock_get(self, url: str):
        """mocking response object
        """
        mock_response = MagicMock()
        mock_response.json.return_value = None
        return mock_response

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google'),
        ('abc', 'https://api.github.com/orgs/abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, url: str, mock_method: MagicMock):
        """testing method org
        """
        inst = GithubOrgClient(org)
        inst.org
        inst.org
        mock_method.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
