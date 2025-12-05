import re
from playwright.sync_api import Page, expect


def test_checkbox(page: Page):
    page.goto("https://demoqa.com/elements")
    print(f"Title: {page.title()}")

    checkbox = page.get_by_text("Check Box")
    checkbox.click()
    # expect to land on checkbox page
    expect(page.locator(".text-center")).to_have_text("Check Box")
    print("Moved to checkbox...")

    main_toggle = page.get_by_role("button", name="Toggle")
    main_toggle.click()
    page.wait_for_timeout(3000)
    print("Clicked main toggle button...")

    documents_label = page.locator(".rct-title", has_text=("Documents"))
    documents_label.click()
    print("Clicked on the label 'Documents'")
    page.wait_for_timeout(3000)
    # locating checkbox
    checkbox_span = documents_label.locator("xpath=preceding-sibling::*[2]")
    checkbox = checkbox_span.locator(".rct-icon")
    # ecpect to be checked
    expect(checkbox).to_contain_class("rct-icon-check")
    print("Documents toggle is open...")
    page.wait_for_timeout(3000)
    # and result area visible with documents
    result_area = page.locator("#result")
    expect(result_area).to_be_visible()
    expect(result_area).to_contain_text("documents")
    print("Result area exists containing 'documents' in texts")
    page.wait_for_timeout(3000)

    documents_arrow = documents_label.locator("xpath=../preceding-sibling::*")
    documents_arrow.click()
    print("Clicked documents toggle...")
    # expecting documents to be expanded
    page.wait_for_timeout(3000)
    expect(documents_arrow.locator(".rct-icon")).to_contain_class(
        "rct-icon-expand-open"
    )
    page.pause()
