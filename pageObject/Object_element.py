import time

from selenium.webdriver.common.by import By


class Demo_Qa_Element:
    element_xpath = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]")
    text_box_xpath = (By.XPATH, "//span[normalize-space()='Text Box']")
    full_name_xpath = (By.XPATH, "//input[@id='userName']")
    email_xpath = (By.XPATH, "//input[@id='userEmail']")
    current_address_xpath = (By.XPATH, "//textarea[@id='currentAddress']")
    permanent_address_xpath = (By.XPATH, "//textarea[@id='permanentAddress']")
    click_submit_button_xpath = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div["
                                           "5]/div[1]/button[1]")
    return_text_xpath = (By.XPATH, "//div[@class='border col-md-12 col-sm-12']")

    def __init__(self, driver):
        time.sleep(2)
        self.driver = driver

    def click_on_element_button(self):
        self.driver.find_element(*Demo_Qa_Element.element_xpath).click()

    def click_on_text_box(self):
        self.driver.find_element(*Demo_Qa_Element.text_box_xpath).click()

    def enter_full_name(self, full_name):
        self.driver.find_element(*Demo_Qa_Element.full_name_xpath).send_keys(full_name)

    def enter_email_address(self, email):
        self.driver.find_element(*Demo_Qa_Element.email_xpath).send_keys(email)

    def enter_current_address(self, curr_add):
        self.driver.find_element(*Demo_Qa_Element.current_address_xpath).send_keys(curr_add)

    def enter_permanent_address(self, per_add):
        self.driver.find_element(*Demo_Qa_Element.permanent_address_xpath).send_keys(per_add)

    def click_on_submit(self):
        self.driver.find_element(*Demo_Qa_Element.click_submit_button_xpath).click()

    def return_text_value(self):
        data = self.driver.find_element(*Demo_Qa_Element.return_text_xpath).text
        print(data)
