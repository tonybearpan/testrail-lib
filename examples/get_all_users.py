#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

from testrail_client import TestRailClient

if __name__ == '__main__':
    # host may not needed to start with 'http://'
    client = TestRailClient('host', 'user@example.com', 'password')
    print client.user.all()
