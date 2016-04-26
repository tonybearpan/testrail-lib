#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

from testrail_client import TestRailClient

if __name__ == '__main__':
    # host may not needed to start with 'http://'
    client = TestRailClient('host', 'tester@example.com', 'password')
    client.user.all()
    client.case.add(1613, title='lalala, are you happy?')
    client.case.for_project(53, 251, 1171)

    # an example using filter
    client.plan.for_project(53, is_completed=1)

    # an example using filter with params in list
    print len(client.test.for_run(8155, status_id=1))
    print len(client.test.for_run(8155, status_id=5))
    print len(client.test.for_run(8155, status_id=[1, 5]))
