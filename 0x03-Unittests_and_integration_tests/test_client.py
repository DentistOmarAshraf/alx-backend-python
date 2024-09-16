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
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_method: MagicMock) -> Any:
        """testing method org
        """
        inst = GithubOrgClient(org)
        mock_method.return_value = org
        self.assertEqual(inst.org, inst._org_name)
        string_to_test = f'https://api.github.com/orgs/{org}'
        mock_method.assert_called_once_with(string_to_test)


if __name__ == "__main__":
    unittest.main()
