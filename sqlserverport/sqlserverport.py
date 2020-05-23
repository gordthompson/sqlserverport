# Copyright 2020 Gordon D. Thompson, gord@gordthompson.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket

"""sqlserverport

A module to query the SQL Browser service for the port number of a SQL Server instance.
"""


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class BrowserError(Error):
    """Problem communicating with the SQL Browser service.
    """

    def __init__(self, message):
        self.message = message


class NoTcpError(Error):
    """Instance not configured for TCP/IP connections.
    """

    def __init__(self, message):
        self.message = message


def lookup(server, instance):
    """Query the SQL Browser service and extract the port number

    :type server: str
    :type instance: str
    """
    udp_port = 1434
    # message type per SQL Server Resolution Protocol
    udp_message_type = b"\x04"  # CLNT_UCAST_INST (client, unicast, instance)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    udp_message = udp_message_type + instance.encode()
    try:
        sock.sendto(udp_message, (server, udp_port))
        response = sock.recv(1024)  # max 1024 bytes for CLNT_UCAST_INST

        # response_type = response[0]  # \x05
        # response_length = response[1:3]  # 2 bytes, little-endian
        response_list = response[3:].decode().split(";")
        response_dict = {
            response_list[i]: response_list[i + 1]
            for i in range(0, len(response_list), 2)
        }

        return int(response_dict["tcp"])

    except KeyError as no_tcp:
        raise NoTcpError(
            r"Instance \{} is not configured to accept TCP/IP connections.".format(
                instance
            )
        )
    except socket.timeout as no_response:
        raise BrowserError(
            r"No response from the SQL Browser service. "
            r"Verify that the service is available on "
            r"{0} and \{1} is a valid instance name on it.".format(
                server, instance
            )
        )
    except ConnectionResetError as no_connect:
        raise BrowserError(
            "Cannot connect to the SQL Browser service on {} .".format(server)
        )
