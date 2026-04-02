
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Browser language")
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Browser name: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    language = request.config.getoption("--language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()
