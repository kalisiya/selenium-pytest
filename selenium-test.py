from selenium import webdriver
import pytest

def test_google_search_contains_search_text():
    searchText = "What is the weather today?"

    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get("https://www.google.com")

    elem = driver.find_element_by_name("q")
    elem.send_keys(searchText)
    elem.submit()

    assert searchText in driver.title