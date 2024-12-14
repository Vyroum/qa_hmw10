import allure
from allure_commons.types import Severity
from allure_steps.allure_steps_for_test import open_browser, searching_repository, open_repository, open_issue_tab, \
    check_homework_issue


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "aimonichev")
@allure.feature("Задачи")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing purpose")
def test_issue_name():
    open_browser()
    searching_repository()
    open_repository()
    open_issue_tab()
    check_homework_issue()


