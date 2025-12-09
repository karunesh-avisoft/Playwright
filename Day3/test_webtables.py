from playwright.sync_api import Page,expect

def test_add(table_page):
    table_page.locator('#addNewRecordButton').click()
    expect(table_page.locator('.modal-content')).to_be_visible()
    # empty submit
    table_page.locator('#submit').click()
    expect(table_page.locator('.modal-content')).to_be_visible()
    
    table_page.locator("#firstName").fill("John")
    table_page.locator("#lastName").fill("Doe")
    table_page.locator("#userEmail").fill("john.doe")
    table_page.locator("#age").fill("30")
    table_page.locator("#salary").fill("50000")
    table_page.locator("#department").fill("Engineering")

    table_page.locator("#submit").click()
    expect(table_page.locator('.modal-content')).to_be_visible()
    # valid email
    table_page.locator("#userEmail").fill("john.doe@example.com")
    table_page.click("#submit")
    expect(table_page.locator('.modal-content')).to_be_visible()
    # Check new row exists
    # assert "John" in table_page.inner_text(".rt-tbody")
    expect(table_page.locator('.rt-tbody')).to_contain_text('John')
    
def test_edit(table_page):
    table_page.locator('#edit-record-1').click()
    
    table_page.locator('#firstName').fill('Michel')
    table_page.locator("#submit").click()
    
    # expect the data update
    expect(table_page.locator('.rt-tbody')).to_contain_text('Michel') 
    
def test_delete(table_page):
    rows = row_list(table_page)
    rows_first_name = rows[1].get_by_role('gridcell').nth(1).inner_text()
    table_page.locator('#delete-record-2').click()
    
    # check delete
    expect(table_page.locator('.rt-tbody')).not_to_contain_text(rows_first_name)
    
def test_search(table_page):
    table_page.locator('#searchBox').fill('Cierra')
    # expect the data existance
    expect(table_page.locator('.rt-tbody')).to_contain_text('Cierra')
    
    table_page.locator('#searchBox').fill('Alden')
    # expect the data existance
    expect(table_page.locator('.rt-tbody')).to_contain_text('Alden')
    
    
def row_list(page):
    row_locator = page.locator(".rt-tr-group")
    count = row_locator.count()
    rows = [row_locator.nth(i) for i in range(count)]
    return rows