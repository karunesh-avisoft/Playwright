from playwright.sync_api import expect
from utilities import *
import re,pytest,json

def load_data():
    with open('test_data.json', 'r') as f:
        try:
            return json.load(f)
        except Exception as e:
            print('Unknown Error: ',e)
            
@pytest.mark.parametrize('data', load_data())
def test_practice_form(practice_form,data):
    # print('DATA: ',data)
    # element locators
    firstname = practice_form.locator("#firstName")
    lastname = practice_form.locator("#lastName")
    email = practice_form.get_by_placeholder("name@example.com")
    mobile = practice_form.get_by_placeholder("Mobile Number")
    subject = practice_form.locator("#subjectsInput")
    picture = practice_form.locator("#uploadPicture")
    current_add = practice_form.get_by_placeholder("Current Address")
    select_state = practice_form.get_by_text("Select State")
    select_city = practice_form.get_by_text("Select City")
    submit = practice_form.locator("#submit")
    modal = practice_form.locator(".modal-content")

    # # form filling
    firstname.type(data["first_name"],delay=100)
    lastname.type(data["last_name"])
    email.press_sequentially(data["email"], delay=50)
    practice_form.get_by_text(re.compile("^"+ data["gender"] +"$", re.IGNORECASE)).click()
    mobile.press_sequentially(data["mobile"], delay=50)
    # DOB 02/05/2000
    pick_date(practice_form, 2,5,2000)
    # subjects
    for sub in data['subjects']:
        subject.type(sub)
        practice_form.keyboard.press('Enter')
    # hobbies
    for hob in data["hobby"]:
        # practice_form.get_by_text(hob, exact=True).check()
        practice_form.locator("div").filter(has_text=re.compile(r"^"+hob+"$")).click()
    # picture upload
    file_path = data['file_path']
    picture.set_input_files(file_path)
    # address
    current_add.type(data["address"],delay=50)
    select_state.click()
    select_state.type(data["state"], delay=50)
    practice_form.keyboard.press('Enter')
    select_city.click()
    select_city.type(data["city"], delay=50)
    practice_form.keyboard.press('Enter')
    
    submit.click()
    
    expect(modal).to_be_attached()
    rows = modal.locator(".table-dark > tbody > tr")
    first_name_cell = rows.nth(0).locator("td").nth(1)

    expect(first_name_cell).to_contain_text(data["first_name"])
