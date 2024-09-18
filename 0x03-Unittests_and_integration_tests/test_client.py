#!/usr/bin/env python3
"""
client testing
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from typing import Any, Dict
from fixtures import TEST_PAYLOAD


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


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration Test
    """

    @classmethod
    def setUpClass(cls):
        """setting up get_patcher
           patching request.get
        """
        cls.get_patcher = patch('requests.get')
        cls.get_mock = cls.get_patcher.start()

        def get_side_effect(url):
            response_mock = MagicMock()
            if url == "https://api.github.com/orgs/google":
                response_mock.json.return_value = cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                response_mock.json.return_value = cls.repos_payload
            return response_mock
        cls.get_mock.side_effect = get_side_effect

    def test_public_repos(self):
        """Testing public_repo method
        """
        inst = GithubOrgClient('google')
        self.assertEqual(inst.org, self.org_payload)
        self.assertEqual(inst.repos_payload, self.repos_payload)
        self.assertEqual(inst.public_repos(), self.expected_repos)
        self.get_mock.assert_called()

    def test_public_repos_with_license(self):
        """Testing public_repo method
        """
        inst = GithubOrgClient('google')
        self.assertEqual(inst.public_repos("apache-2.0"), self.apache2_repos)
        self.assertEqual(inst.public_repos(), self.expected_repos)
        self.assertEqual(inst.public_repos("some"), [])
        self.get_mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down patcher
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    """
    Main
    """
    unittest.main()
