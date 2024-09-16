#!/usr/bin/env python3
"""
utils testing
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from utils import access_nested_map, get_json
from utils import memoize
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               output: Any) -> None:
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> Any:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Testing get_json
    """

    def mock_get(self, url: str):
        mock_response = MagicMock()
        if url == "http://example.com":
            mock_response.json.return_value = {"payload": True}
        if url == "http://holberton.io":
            mock_response.json.return_value = {"payload": False}
        return mock_response

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self,
                      url: str,
                      output: dict,
                      mock_request: MagicMock):
        mock_request.get.side_effect = self.mock_get
        self.assertEqual(get_json(url), output)


class TestMemoize(unittest.TestCase):
    """
    Testing memoize
    """

    def test_memoize(self):
        class TestClass:
            """
            test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method
        with patch.object(
                        TestClass,
                        'a_method',
                        return_value=None) as mock_method:
            mock_inst = TestClass()
            mock_inst.a_method()
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
