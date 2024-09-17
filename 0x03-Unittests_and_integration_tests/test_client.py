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
        """test public repos url
        """
        mock_prop.return_value = {"repos_url": True}
        inst = GithubOrgClient(org_tst)
        self.assertEqual(inst.org["repos_url"], inst._public_repos_url)

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, org, m_public_repos_url, m_get_json):
        """testing _public_repos
        """
        json_payload = [{"name": "oamr"}, {"name": "nada"}]
        m_get_json.return_value = json_payload
        m_public_repos_url.return_value = "http:req"
        to_check = [x["name"] for x in json_payload]
        inst = GithubOrgClient(org)
        self.assertEqual(inst.public_repos(), to_check)
        m_get_json.assert_called_once()
        m_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, dic_lic, lic, ret_bool):
        """Testing has_license method
        """
        inst = GithubOrgClient('google')
        check = inst.has_license(dic_lic, lic)
        self.assertEqual(check, ret_bool)


if __name__ == "__main__":
    unittest.main()
