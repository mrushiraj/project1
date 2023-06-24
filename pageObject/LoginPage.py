from selenium.webdriver.common.by import By


class UserLoginClass:
    Text_username = (By.ID, 'username')
    Text_Password = (By.ID, 'password')
    Submit_Button = (By.ID, 'submit')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*UserLoginClass.Text_username).send_keys(username)

    def enter_Password(self, password):
        self.driver.find_element(*UserLoginClass.Text_Password).send_keys(password)

    def submit_Button(self):
        self.driver.find_element(*UserLoginClass.Submit_Button).click()
