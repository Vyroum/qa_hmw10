import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.step("Открытие браузера и переход на github.com")
def open_browser():
    browser.open("")


@allure.step("Поиск репозитория Vyroum/qa_hmw10")
def searching_repository():
    s("[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").click().type("Vyroum/qa_hmw10").press_enter()


@allure.step("Открытие репозитория Vyroum/qa_hmw10")
def open_repository():
    s(by.link_text("Vyroum/qa_hmw10")).click()


@allure.step("Открытие вкладки Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверка наличия Issue с 'homework' в названии")
def check_homework_issue():
    s(by.partial_text("homework")).should(be.visible)
