#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

from base import TestRailAPIBase


class Result(TestRailAPIBase):
    """
    Use the following API methods to request details
    about test results and to add new test results.
    """
    def __repr__(self):
        return '<TestRailAPI result>'

    def get(self, test_id):
        """
        Returns a list of test results for a test.
        :param test_id:The ID of the test
        """
        return self._get('get_results/{}'.format(test_id))

    def for_case(self, run_id, case_id):
        """
        Returns a list of test results for a test run and case combination.
        :param run_id:The ID of the test run
        :param case_id:The ID of the test case
        """
        return self._get('get_results_for_case/{run_id}/{case_id}'
                         .format(run_id=run_id,
                                 case_id=case_id)
                         )

    def for_run(self, run_id):
        """
        Returns a list of test results for a test run.
        :param run_id:The ID of the test run
        """
        return self._get('get_results_for_run/{}'.format({run_id}))

    def add(self, test_id, status_id=None, comment=None,
            vesion=None, elapsed=None, defects=None,
            assignedto_id=None, **kwargs):
        """
        Adds a new test result, comment or assigns a test.
        It's recommended to use add_results instead
        if you plan to add results for multiple tests.
        :param test_id:The ID of the test the result should be added to
        :param status_id:The ID of the test status.
        :param comment:The comment / description for the test result
        :param vesion:The version or build you tested against
        :param elapsed:The time it took to execute the test, e.g. "30s" or "1m 45s"
        :param defects:A comma-separated list of defects to link to the test result
        :param assignedto_id:The ID of a user the test should be assigned to
        """
        return self._post('add_result/{}'.format(test_id),
                          json=locals().pop('test_id'))

    def add_for_case(self, run_id, case_id, status_id=None,
                     comment=None, vesion=None, elapsed=None,
                     defects=None, assignedto_id=None, **kwargs):
        """
        Adds a new test result, comment or assigns a test
        (for a test run and case combination).
        :param run_id:The ID of the test run
        :param case_id:The ID of the test case
        :param status_id:The ID of the test status.
        :param comment:The comment / description for the test result
        :param vesion:The version or build you tested against
        :param elapsed:The time it took to execute the test, e.g. "30s" or "1m 45s"
        :param defects:A comma-separated list of defects to link to the test result
        :param assignedto_id:The ID of a user the test should be assigned to
        """
        run_id = locals().pop('run_id')
        case_id = locals().pop('case_id')
        return self._post('add_result_for_case/{run_id}/{case_id}'
                          .format(run_id=run_id, case_id=case_id),
                          json=locals())

    def add_multiple(self, run_id, status_id=None, comment=None,
                     vesion=None, elapsed=None, defects=None,
                     assignedto_id=None, **kwargs):
        """
        Adds one or more new test results, comments or assigns one or more tests.
        Ideal for test automation to bulk-add multiple test results in one step.
        :param status_id:The ID of the test status.
        :param comment:The comment / description for the test result
        :param vesion:The version or build you tested against
        :param elapsed:The time it took to execute the test, e.g. "30s" or "1m 45s"
        :param defects:A comma-separated list of defects to link to the test result
        :param assignedto_id:The ID of a user the test should be assigned to
        """
        return self._post('add_results/{}'.format(run_id),
                          json=locals().pop('run_id'))

    def field(self):
        """
        Returns a list of available test result custom fields.
        """
        return self._get('get_result_fields')
