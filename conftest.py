import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import allure
from termcolor import colored

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    return rep

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "locale": "ru-RU"
    }
    
# @pytest.fixture(scope="function", autouse=True)
# def page(request, page: Page):

#     request.cls.page = page
#     yield page
#     page.close()

@pytest.fixture(scope='session')
def page():
    with sync_playwright() as play:
        # if os.getenv('DOCKER_RUN') or os.getenv('GITHUB_RUN'):
        #     browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        # else:
        browser = play.chromium.launch(headless=True)
        context = browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0')
        page = context.new_page()
        yield page

        browser.close()
        
        
# capabilities = {
#     'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
#     'browserVersion': 'latest',
#     'LT:Options': {
#         'platform': 'Windows 10',
#         'build': 'Playwright Locators Demo Build',
#         'name': 'Playwright Locators Test For Windows 10 & Chrome',
#         'user': os.getenv('LT_USERNAME'),
#         'accessKey': os.getenv('LT_ACCESS_KEY'),
#         'network': True,
#         'video': True,
#         'visual': True,
#         'console': True,
#         'tunnel': False,   # Add tunnel configuration if testing locally hosted webpage
#         'tunnelName': '',  # Optional
#         'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
#     }
# }


# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     # request.node is an "item" because we use the default
#     # "function" scope
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             # driver = request.node.funcargs['selenium_driver']
#             # take_screenshot(nodeid=request.node.nodeid)
#             print("executing test failed", request.node.nodeid)

# make a screenshot with a name of the test, date and time
def take_screenshot(page: Page, nodeid):
    # time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
    page.screenshot(file_name)
    
    
def pytest_sessionstart(session):
    session.results = dict()

def pytest_sessionfinish(session, exitstatus):
    print(colored(f"FINISHED!!! {session.results}", "light_blue"))
    for item in session.items:
        print("!"*30,'{} {}'.format(item.name, item.rep_call.outcome))
    failed_amount = len([result for result in session.items if result.rep_call.outcome == "failed"])
    print(f'there are {failed_amount} failed out of {len(session.items)} tests')
    

@pytest.fixture(name="screenshot_on_failure")
def log_on_failure(request, page: Page):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(page.screenshot(full_page=True), name=f"Failure_{request.function.__name__}_{time.strftime('%y_%m_%d_%H_%M')}", attachment_type=allure.attachment_type.PNG)