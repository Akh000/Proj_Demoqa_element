import time

import pytest
from pageObject.Object_element import Demo_Qa_Element
from utilities.Logger import LogGenerator


class Test_Element:
    log = LogGenerator.loggen()

    def test_element_001(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        # self.log.info('Opening Browser')
        # self.log.info("comparing page title")
        if self.driver.title == 'DEMOQA':
            assert True
        else:
            assert False

    # @pytest.mark.skip
    def test_element_002(self, setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.el = Demo_Qa_Element(self.driver)
        self.log.info("Click on Element Button")
        self.el.click_on_element_button()
        self.log.info("Click on text box button")
        self.el.click_on_text_box()
        self.log.info("Enter the Fullname")
        self.el.enter_full_name("Ram Lakhan")
        self.log.info("Entering Email Address")
        self.el.enter_email_address("ram@gmail.com")
        self.log.info("Entering Current Addresss")
        self.el.enter_current_address("Ab Tak 56, Gandhi Road, Jhingalala, USA.")
        self.log.info("Entering Permanent Address")
        self.el.enter_permanent_address("23A, kali colony,England.")
        self.log.info("Scrolling window downside")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.log.info("Click on Submit Button")
        self.el.click_on_submit()
        self.log.info("Return The values In text box\n")
        self.el.return_text_value()
        # if self.el.return_text_value() == True:
        #     print("Data is " + self.data)
        #     assert True
        # else:
        #     print("Data is not found.")
        #     assert False
