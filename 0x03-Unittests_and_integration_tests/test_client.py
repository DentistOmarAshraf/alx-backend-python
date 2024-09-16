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

    def mock_get_json(self, url: str):
        """mocking response object
        """
        return {"test": "value"}

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google', {"test":"value"}),
        ('abc', 'https://api.github.com/orgs/abc', {"test":"value"})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, url: str, ret: dict, mock_method: MagicMock):
        """testing method org
        """
        inst = GithubOrgClient(org)
        mock_method.side_effect = self.mock_get_json
        self.assertEqual(inst.org, ret)
        mock_method.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
