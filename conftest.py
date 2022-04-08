import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Select browser and page's language
    """
    parser.addoption('--browser_name', action='store', default='firefox', help='Choose browser chrome or firefox')
    parser.addoption('--language', action='store', default='en', help='Choose language: es, fr, ..')


@pytest.fixture(scope="function")
def browser(request):
    """
    Open selected browser with selected language
    """
    browser_name = request.config.getoption("browser_name")
    page_language = request.config.getoption("language")
    if browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", page_language)
        print("\nFirefox started..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        option = Options()
        option.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        print("\nChrome started..")
        browser = webdriver.Chrome(options=option)
        browser.maximize_window()
    yield browser
    print("\nquit browser")
    browser.quit()
