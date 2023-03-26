#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import argparse

from messaging_app.messaging_app_config import password

import messaging_app

def main():
    parser = argparse.ArgumentParser(
        description="RSA based blockchain messaging app.")

    parser.add_argument("-pass",
                        "--password",
                        default="123",
                        type=str,
                        help="Give the naruno pass")


    parser.add_argument("-p",
                        "--port",
                        default=81,
                        type=int,
                        help="Give a port for api")

    parser.add_argument("-ip",
                        "--integrationport",
                        default=8000,
                        type=int,
                        help="Give a port for integratin")

    

    args = parser.parse_args()
    messaging_app.messaging_app_config.password = args.password

    from messaging_app.web.chat import start_messaging_app
    start_messaging_app(port=args.port, integration_port=args.integrationport, password=args.password)

