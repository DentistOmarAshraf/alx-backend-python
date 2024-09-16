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
    @patch('utils.requests')
    def test_org(self, org: str, url: str, mock_request: MagicMock):
        """testing method org
        """
        mock_request.get.side_effect = self.mock_get
        inst = GithubOrgClient(org)
        inst.org
        mock_request.get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
