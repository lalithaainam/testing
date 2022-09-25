import pytest
# test case code must be written inside a method
# method name must be started with test
#this p/g shows how to use test fixtures


@pytest.fixture(scope='session')
def fixture_code():
    print("This is our fixture code will execute before the test case")
    print("===========================================================")
    yield
    print("close db connection after the test case")
    print("===========================================================")



@pytest.mark.smoke
@pytest.mark.regression
def test_tc_001_login_logout_testing(fixture_code):
    print("this is our smoke test case code .....")
    print("this is end of my test cases")


@pytest.mark.sanity
@pytest.mark.regression
def test_tc_003_login_logout_invalid_credentials(fixture_code):
    print("this is our 3 rd sanity test case code .....")
    print("this is end of my test case")

# print statement o/p in console -s
# verbose mode - display all test cases name with status -v
# if we want to pass a particular testcase use -k
