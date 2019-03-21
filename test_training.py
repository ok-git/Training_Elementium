from selenium import webdriver
from elementium.drivers.se import SeElements


def test_delete_addressbook_in_mh():
    browser = SeElements(webdriver.Firefox())
    #with se as browser:
    # open url
    browser.navigate('https://bulk.boomware.com/login')
    # login
    browser.find('email').write('test@svyazcom.ru')
    browser.find('password').write('123456Test')
    browser.find('button').click()
    # enter token
    browser.find('code').write('978896')
    browser.find('button').click()
    pass
    # open AB page
    # browser.click_link_by_partial_href('address_book')
    # waiting complete loading of the webpage
    # browser.is_text_present("Начните вводить название книги", wait_time=5)
    # open actions menu
    # browser.find_by_xpath("//button[@type='button']").click()
    # init deletion
    # browser.find_by_css("a.modal_delete").click()
    # submit deletion
    # browser.find_by_xpath("//button[@type='submit']").click()
    # logout
    # browser.find_by_css('li.dropdown.user').click()
    # browser.click_link_by_partial_href('logout')
