def pick_date(page, day, month, year):
    page.click("#dateOfBirthInput")

    # select year
    page.locator(".react-datepicker__year-select").select_option(str(year))

    # select month (0 = Jan)
    page.locator(".react-datepicker__month-select").select_option(str(month))

    # click valid day only
    page.locator(
        f"//div[contains(@class,'react-datepicker__day') and not(contains(@class,'outside-month')) and text()='{day}']"

    ).click()