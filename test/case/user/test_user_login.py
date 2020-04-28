from test.case.basecase import BaseCase


class TestUserLogin(BaseCase):   # 这里直接继承BaseCase
    def test_user_login_normal(self):
        """level1:正常登录"""
        case_data = self.get_case_data("test_user_login_normal")
        self.send_request(case_data)

    def test_user_login_password_wrong(self):
        """密码错误登录"""
        case_data = self.get_case_data("test_user_login_password_wrong")
        self.send_request(case_data)