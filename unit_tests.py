'''
I have not implemented unit tests for this application yet as the connection logic is not
working but my intention was to use a combination of AssertHttpResponse() and AssertEquals()
calls to check that the correct response was given in each case.
'''


def test_http_calls():
    '''
    Checks that example calls return correct output
    '''
    pass

def test_http_404():
    '''
    Checks that non-existent organism returns 404 (name not in organism:name)
    '''
    pass

def test_no_parameter():
    '''
    Checks that no parameters returns 400
    '''
    pass

def test_name_length():
    '''
    Checks that name < 3 characters returns 400
    '''
    pass

def test_wrong_release():
    '''
    Checks that release is integer (else 400)
    '''
    pass

def test_non_get():
    '''
    Checks non-GET queries (POST/PUT/PATCH) return 405
    '''
    pass


def test_no_db():
    '''
    Checks that non-matching db type (dbtype not in database) returns empty list
    '''
    pass