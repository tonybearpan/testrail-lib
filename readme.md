# testrail-library

This is a Python wrapper of the test rail api according to 
[the official document](http://docs.gurock.com/testrail-api2/start)

## Install

    pip install testrail-library


## Example

    from testrail_client import TestRailClient
    
    client = TestRailClient('host', 'user@example.com', 'password')
    
    client.user.all()
    
    client.case.add(1613, title='lalala, are you happy?')

## TODO

add support for filter of APIs
 
## Version

* Version 0.0.1:    Implementation of basic all APIs

* Version 0.0.4:    All APIs test passed