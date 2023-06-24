from pageObject.LoginPage import UserLoginClass


class Test_LoginClass:

    def test_login_001(self, setup):
        self.driver = setup
        self.lp = UserLoginClass(self.driver)

        self.lp.enter_username('student')
        self.lp.enter_Password('Password123')
        self.lp.submit_Button()




