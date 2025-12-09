from playwright.sync_api import expect

def test_upload(files):
    file_path = r"C:\Users\hp\Downloads\sampleFile.jpeg"
    files.locator('#uploadFile').set_input_files(file_path)
    
    expect(files.locator('#uploadedFilePath'), 'File not uploaded').to_contain_text('sampleFile.jpeg')

def test_dwnld(files):
    with files.expect_download() as download_info:
        files.locator('#downloadButton').click()
    
    download=download_info.value
    print('Values: ', download)
    download.save_as('downloadedfile.txt')
    