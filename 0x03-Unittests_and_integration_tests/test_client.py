#!/usr/bin/env python3
"""
client testing
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Any, Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    testing GithubOrgClient class
    """

    @parameterized.expand([
        ('google', 'https://api.github.com/orgs/google', {"payload": True}),
        ('abc', 'https://api.github.com/orgs/abc', {"payload": True})
    ])
    @patch('client.get_json')
    def test_org(
            self, org: str, url: str,
            ret: dict, mock_method: MagicMock) -> Any:
        """testing method org
        """
        inst = GithubOrgClient(org)
        mock_method.return_value = {"payload": True}
        self.assertEqual(inst.org, ret)
        mock_method.assert_called_once()
        mock_method.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
