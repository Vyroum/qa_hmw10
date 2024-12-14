from selene import by, be, browser
from selene.support.shared.jquery_style import s
import allure


def test_issue_name():
    with allure.step("Открываем github"):
        browser.open("")

    with allure.step("Ищем репозиторий"):
        s("[data-target='qbsearch-input.inputButtonText']").click()
        s("#query-builder-test").click().type("Vyroum/qa_hmw10").press_enter()

    with allure.step("Открываем репозиторий"):
        s(by.link_text("Vyroum/qa_hmw10")).click()

    with allure.step("Открываем вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue содержащего homework в названии"):
        s(by.partial_text("homework")).should(be.visible)
