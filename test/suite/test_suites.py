import unittest
import sys
sys.path.append("../..")
from test.case.user.test_user_login import TestUserLogin
from test.case.user.test_user_reg import TestUserReg

smoke_suite = unittest.TestSuite()  # 自定义的TestSuite
smoke_suite.addTests([TestUserLogin('test_user_login_normal'), TestUserReg('test_user_reg_normal')])

def get_suite(suite_name):    # 获取TestSuite方法
    return globals().get(suite_name)