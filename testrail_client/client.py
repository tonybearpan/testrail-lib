#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

from api import TestRailAPI


class TestRailClient(TestRailAPI):

    def __init__(self, base_url, user, password):
        self.user = user
        self.password = password
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    def __repr__(self):
        return '<TestRailClient>'

    @property
    def test_rail_url(self):
        return self.__url


