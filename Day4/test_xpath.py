from playwright.sync_api import expect,Page

def test_maxSalary(x_path):
    x_path.locator('#table1').scroll_into_view_if_needed()
    max_srno = filter_data(x_path)
    target_row = x_path.locator("#table1").get_by_role("cell", name=str(max_srno), exact=True)
    read_more = target_row.locator('xpath=following-sibling::*[4]')
    read_more.locator('a').click()
    
def filter_data(page):
    table_locator = page.locator('#table1 > tbody')
    srno = 0
    max_sal = 0
    rows = table_locator.locator("tr").all()

    for row in rows:
        row_data = []
        cells = row.locator("td").all() # For data cells
        # If need headers, we can also use:
        # headers = row.locator("th").all() 

        for i in range(len(cells)):
            content = cells[i].text_content().strip()
            if i==2 and float(content)>max_sal:
                srno = int(cells[0].text_content().strip())
                max_sal = float(content)
            row_data.append(content)
    print("Srno: ",srno)
    print('Max Salary: ',max_sal)
    return srno
        