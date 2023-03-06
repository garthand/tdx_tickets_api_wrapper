#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Team Dynamix Ticket Operations."""

from __future__ import annotations
import configparser
import json
from requests.rest_requests import Request


class TicketInterface:
    """Simplified interface for interacting with Team Dynamix."""

    def __init__(self) -> None:
        """Initialize class variables."""
        # Read the config file for later use
        self.config = configparser.ConfigParser()
        self.config.read("/home/aml4540/teamdynamix_api_wrappers/config.ini")
        # Create the request object
        self.request = Request()
        # Get the authorization token
        self.authorization_token: str = self.get_authorization_token()
        # Set the authorization token for the request
        self.request.set_authorization_token(self.authorization_token)

    def get_authorization_token(self) -> str:
        """Get an authorization token from Team Dynamix."""
        # This is the URI used for getting an authorization token
        uri: str = self.config["URI"]["auth"]
        # The Team Dynamix API username
        username: str = self.config["Authentication"]["username"]
        # The Team Dynamix API password
        password: str = self.config.get("Authentication",
                                        "password", raw=True)
        # The type of request to send
        request_type: str = "POST"
        # The authorization token used for all other Team Dynamix API calls
        token: str = self.request.send(uri, request_type, username=username,
                                       password=password)
        # Return the token as a string for use in other API calls
        return token

    def get_ticket(self, ticket_id: str) -> dict[str, str]:
        """Get a ticket from Team Dynamix."""
        # Create the URI for the request
        uri: str = self.config["URI"]["get_ticket"] + ticket_id
        # Set the request type for the request
        request_type: str = "GET"
        # Send the request for the ticket information
        raw_response: str = self.request.send(uri, request_type)
        # Format the response into a dictionary for later processing
        response: dict[str, str] = json.loads(raw_response)
        return response
