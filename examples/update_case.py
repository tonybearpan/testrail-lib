#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-

import csv
import logging
from testrail_client import TestRailClient


class CsvManager(TestRailClient):
    """
    This class is an example where csv upload function is implemented by APIs.
    The primordial upload function is not so easy use, the cases
    """
    def __init__(self, base_url, user_name,
                 password, file_path):
        super(CsvManager, self).__init__(base_url, user_name, password)
        self.file = file_path
        self.project_id = None
        self.section_id = None

    def read(self):
        """
        read test cases in csv file.
        """
        with open(self.file, 'rb') as csv_file:
            csv_buffer = csv.DictReader(csv_file)
            for data in csv_buffer:
                yield data

    def upload(self, case):
        """
        check whether case is on test rail, if case is on test rail, 
        the case will be updated. If not, the case will be added as a
        new case.
        :param case: dict, case read from csv
        """
        steps = case['steps (Step)'].split('\n')
        results = case['steps (Expected Result)'].split('\n')

        param = {
            'title': case['Title'],
            'custom_preconds': case['Preconditions'],
            'custom_steps': [{'content': steps[i], 'expected': results[i]}
                             for i in range(len(steps))]
        }
        if len(case.get('ID')) == 0:
            if not self.section_id:
                if not self.project_id:
                    suite_id = ''.join(filter(lambda x: x.isdigit(), case.get('Suite ID')))
                    self.project_id = self.suite.get(suite_id)['project_id']
                self.section_id = filter(lambda x: x['name'] == case['Section'],
                                         self.section.for_suite(self.project_id)
                                         )[0]['id']
            self.case.add(self.section_id, **param)
        else:
            case_id = ''.join(filter(lambda x: x.isdigit(), case.get('ID')))
            self.case.update(case_id, **param)
        logging.info('[CsvManager] upload successfully!')
        return True


if __name__ == '__main__':
    a = CsvManager('host', 'user@example.com',
                   'password', 'csv file path')
    for case in a.read():
        a.upload(case)