#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for REST API call wrappers."""

import unittest
from requests.rest_requests import Request


class TestRequests(unittest.TestCase):
    """Test class for REST API wrappers."""

    def test_set_content_type(self) -> None:
        """Test the set_content_type method."""
        content_type: str = "text/html"
        request = Request()
        request.set_content_type(content_type)
        self.assertEqual(content_type, request.content_type)


if __name__ == '__main__':
    unittest.main()
