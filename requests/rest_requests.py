#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""REST API call wrappers."""

from __future__ import annotations
import json
import urllib.request


class Request:
    """Class for handling REST requests."""

    def __init__(self) -> None:
        """Set default class variable values from a passed dictionary."""
        # Set the default content type for sent and received requests
        self.content_type: str = "application/json"
        # Set the default encoding for sent and received requests
        self.encoding: str = "utf-8"
        # Set the default authorization token
        self.authorization_token: str = ""

    def set_content_type(self, content_type: str) -> None:
        """Set the content_type for requests."""
        self.content_type = content_type

    def set_encoding(self, encoding: str) -> None:
        """Set the encoding for requests."""
        self.encoding = encoding

    def set_authorization_token(self, authorization_token: str) -> None:
        """Set an authorization token to use in requests."""
        self.authorization_token = authorization_token

    def send(self, uri: str, request_type: str,
             **raw_data: str) -> str:
        """
        Perform a REST request using the specified parameters.

        uri: This is the URI the REST request will perform
        its operation against.

        request_type: This is the type of request. Valid options are
        GET, DELETE, POST, PUT and PATCH.

        raw_data: This is the data you want to include in the request.
        Note that data may not be included in GET or DELETE requests,
        and must be included in POST, PUT and PATCH requests.
        """
        # Create a request object
        request: urllib.request.Request = urllib.request.Request(
            uri, method=request_type)
        # If an authorization token has been set, add a header
        # including the authorization token
        if self.authorization_token != "":
            request.add_header("Authorization", "Bearer " +
                               self.authorization_token)
        # Add a header with the expected content type and encoding
        request.add_header("Accept", self.content_type + "; " + self.encoding)
        # If the request has data to send, add a header
        # with the content type and encoding
        if raw_data:
            request.add_header("Content-Type", self.content_type +
                               "; " + self.encoding)
            # Convert the raw data dictionary to a string
            data_string: str = json.dumps(raw_data)
            # Convert the data string to bytes
            data: bytes = data_string.encode()
            # Submit the request and get a response,
            # reading the data into bytes
            with urllib.request.urlopen(request, data=data) as raw_response:
                html: bytes = raw_response.read()
        else:
            with urllib.request.urlopen(request) as raw_response:
                html = raw_response.read()
        # Convert the response into a string
        response: str = str(html.decode())
        # Return the response as a string for further processing
        return response
