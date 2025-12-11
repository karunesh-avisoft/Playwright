import pytest
from utilities import pick_date,load_data
import logging

# logging object
logger = logging.getLogger(__name__)

@pytest.mark.parametrize('data', load_data())
def test_practice_form(form_page, data):
    logging.info('Filling form.')
    form_page.fill_personal_info(data)
    form_page.select_gender(data["gender"])

    pick_date(form_page.page, 2, 5, 2000)

    form_page.select_subjects(data["subjects"])
    form_page.select_hobbies(data["hobby"])

    form_page.upload_picture(data["file_path"])
    form_page.enter_address(data["address"])
    form_page.select_state_city(data["state"], data["city"])

    form_page.submit_form()
    logger.info("Form Submitted")
    
    logger.info('Verifying first user name in modal data.')
    first_name_cell = form_page.get_first_name_from_modal()
    assert data["first_name"] in first_name_cell.inner_text(), "Data does not match with entered!"
    logger.info('Vrification Done.')
