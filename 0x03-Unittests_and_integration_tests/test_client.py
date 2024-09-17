#!/usr/bin/env python3
"""
client testing
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Any, Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    testing GithubOrgClient class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_method: MagicMock) -> Any:
        """testing method org
        """
        mock_method.return_value = {"payload": True}
        inst = GithubOrgClient(org)
        self.assertEqual(inst.org, {"payload": True})
        string_to_test = f'https://api.github.com/orgs/{org}'
        mock_method.assert_called_once_with(string_to_test)

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, org_tst: str, mock_prop: MagicMock):
        mock_prop.return_value = {"repos_url": True}
        inst = GithubOrgClient(org_tst)
        self.assertEqual(inst.org["repos_url"], inst._public_repos_url)


if __name__ == "__main__":
    unittest.main()
