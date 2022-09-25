import pytest

# test case code must be written inside a method
# method name must be started with test
# a =101
actual_result = "testing"


# @pytest.mark.skipif(a > 100, reason="skipping as this functionality is not working... developer will fix it in new "
#                                   "build")
@pytest.mark.TopPriority
def test_tc_001_login_logout_testing():
    print("this is our smoke test case code .....")
    print("this is end of my test cases")
    assert actual_result != "testing", "These two values must not be same"


@pytest.mark.TopPriority
def test_tc_003_login_logout_invalid_credentials():
    print("this is our 3 rd sanity test case code .....")
    print("this is end of my test case")

# print statement o/p in console -s
# verbose mode - display all test cases name with status -v
# if we want to pass a particular testcase use -k
# this is for test in git
