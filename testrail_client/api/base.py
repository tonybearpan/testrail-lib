#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

import requests
from error import TesRailAPIError, TestRailAuthError


def check_execption(func):
    def _check(*arg, **kws):
        resp = func(*arg, **kws)
        if resp.status >= 400:
            if resp.status == 403:
                raise TestRailAuthError(403, 'No permission')
            elif resp.status == 401:
                raise TestRailAuthError(401, 'Not authorized')
            else:
                raise TesRailAPIError(resp)
        try:
            return resp.json()
        except Exception:
            return resp.content
    return _check


class TestRailAPIBase(object):

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.header = {
            'Content-Type': 'application/json'
        }

    def __repr__(self):
        return '<TestRailAPI Base>'

    @check_execption
    def _get(self, url, **opts):
        return requests.get(url,
                            auth=(self.user, self.password),
                            headers=self.header,
                            **opts)

    @check_execption
    def _post(self, url, **opts):
        return requests.post(url,
                             auth=(self.user, self.password),
                             headers=self.headerm,
                             **opts)
