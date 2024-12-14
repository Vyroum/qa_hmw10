from selene import by, be, browser
from selene.support.shared.jquery_style import s


def test_issue_name():
    browser.open("")
    s("[data-target='qbsearch-input.inputButtonText']").click()
    s("#query-builder-test").click().type("Vyroum/qa_hmw10").press_enter()
    s(by.link_text("Vyroum/qa_hmw10")).click()
    s("#issues-tab").click()
    s(by.partial_text("homework")).should(be.visible)
