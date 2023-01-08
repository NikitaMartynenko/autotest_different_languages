import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: 'ar','ca','cs','da','de',"
                          "'en-gb','el','es','fi','fr','it','ko',"
                          "'nl','pl','pt','pt-br','ro','ru','sk','uk','zh-cn'")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print(f'user_language = {user_language}')

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()

@pytest.fixture(scope="function")
def user_language(request):
    return request.config.getoption("language")
