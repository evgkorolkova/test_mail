import re
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class MailLocators:

    LOCATOR_BUTTON_LOGIN = (By.CSS_SELECTOR, "[data-reactid='22']")
    LOCATOR_INPUT_LOGIN = (By.ID, "passp-field-login")
    LOCATOR_BUTTON_LOGIN2 = (By.CSS_SELECTOR, "[class='passp-button passp-sign-in-button']")
    LOCATOR_INPUT_PASSWORD = (By.ID, "passp-field-passwd")
    LOCATOR_BUTTON_LOGIN3 = (By.CSS_SELECTOR, "[class='passp-button passp-sign-in-button']")
    LOCATOR_SEARCH_MAIL = (By.CLASS_NAME, "textinput__control")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, "[class='mail-SuggestItem-Rocks mail-SuggestItem-Rocks-AllResults']")
    LOCATOR_SEARCH_TEXT = (By.CSS_SELECTOR, "[class='mail-MessagesSearchInfo-Title_misc nb-with-xs-left-gap']")
    LOCATOR_BUTTON_CREATE_LETTER = (By.CSS_SELECTOR, "[class='mail-ComposeButton js-main-action-compose']")
    LOCATOR_INPUT_SENDER_EMAIL = (By.CSS_SELECTOR, ".tst-field-to .composeYabbles")
    LOCATOR_SUBJECT_EMAIL = (By.NAME,"subject")
    LOCATOR_BODY_EMAIL = (By.CSS_SELECTOR, ".cke_wysiwyg_div")
    LOCATOR_BUTTON_SEND_EMAIL = (By.CSS_SELECTOR, 
    "[class='ComposeControlPanelButton ComposeControlPanel-Button ComposeControlPanel-SendButton ComposeSendButton ComposeSendButton_desktop']")

class MailLogin(BasePage):
    def login_click(self):
        return self.find_element(MailLocators.LOCATOR_BUTTON_LOGIN).click()


    def login_sign_in(self, login):
        input_login = self.find_element(MailLocators.LOCATOR_INPUT_LOGIN)
        input_login.send_keys(login)
        button_login = self.find_element(MailLocators.LOCATOR_BUTTON_LOGIN2).click()
        return input_login


    def password_sign_in(self, password):
        input_password = self.find_element(MailLocators.LOCATOR_INPUT_PASSWORD)
        input_password.send_keys(password)
        button_password = self.find_element(MailLocators.LOCATOR_BUTTON_LOGIN3).click()
        return button_password


class MailAccount(BasePage):
    def enter_search_email(self, email):
        search_field = self.find_element(MailLocators.LOCATOR_SEARCH_MAIL)
        search_field.send_keys(email)
        search_button = self.find_element(MailLocators.LOCATOR_SEARCH_BUTTON).click()
        search_text = self.find_element(MailLocators.LOCATOR_SEARCH_TEXT).text
        result_text = re.findall(r'\d+', search_text)
        return result_text


    def click_create_letter(self):
        return self.find_element(MailLocators.LOCATOR_BUTTON_CREATE_LETTER).click()


class CreateLetter(BasePage):
    def input_recipient_email(self, email):
        recipient_email = self.find_element(MailLocators.LOCATOR_INPUT_SENDER_EMAIL)
        recipient_email.send_keys(email)
        return recipient_email


    def input_letter_subject(self, subject):
        letter_subject = self.find_element(MailLocators.LOCATOR_SUBJECT_EMAIL)
        letter_subject.send_keys(subject)
        return letter_subject


    def input_letter_body(self):
        search_text = self.find_element(MailLocators.LOCATOR_SEARCH_TEXT).text
        result_text = result_text = re.findall(r'\d+', search_text)
        letter_body = self.find_element(MailLocators.LOCATOR_BODY_EMAIL)
        letter_body.send_keys(f"Количество найденных писем: {result_text}")
        return letter_body


    def send_email(self):
        return self.find_element(MailLocators.LOCATOR_BUTTON_SEND_EMAIL).click()

