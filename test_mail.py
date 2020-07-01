import time
from MailPages import MailLogin, MailAccount, CreateLetter

def test_sign_in(browser):   
    page = MailLogin(browser)
    page.open()
    page.login_click()
    page.login_sign_in("korolkova30")
    page.password_sign_in("Testqa123")
    account_page = MailAccount(browser)
    return account_page


def test_search_letters(browser):
    account_page = MailAccount(browser)
    account_page.enter_search_email("ev.korolkova73@gmail.com")
    account_page.click_create_letter()
    return account_page


def test_send_letter(browser):
    letter = CreateLetter(browser)
    letter.input_recipient_email("ev.korolkova73@gmail.com")
    letter.input_letter_subject("Тестовое задание. Королькова")
    letter.input_letter_body()
    letter.send_email()
    return letter
