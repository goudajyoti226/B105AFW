from generic.base_class import BaseClass
from page.login_page import LoginPage
import pytest

class Test_InvalidLogin(BaseClass):
    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        # 1. enter invalid username
        login_page = LoginPage(self.driver)
        login_page.set_username("abcd")

        # 2. enter invalid password
        login_page.set_password("xyz")

        # 3. click on go button
        login_page.click_go()

        # 4. verify error msg is displayed
        result=login_page.verify_errmsg_is_displayed(self.wait)
        assert result
