from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:

    inputbox_xpath = "//input[@class='gLFyf gsfi']"
    inputbox_name = "q"
    pageNumber_xpath = "//a[@aria-label='Page 2']"
    pageResult_id = "result-stats"

    def __init__(self,driver):
        self.driver = driver

    def setSearchItem(self,itemName):
        self.driver.find_element(By.XPATH, self.inputbox_xpath).clear()
        self.driver.find_element(By.NAME, self.inputbox_name).send_keys(itemName)

    def clickSearch(self):
        self.driver.find_element(By.NAME, self.inputbox_name).send_keys(Keys.ENTER)

    def clickPage(self,numberOfPage):
        wait = WebDriverWait(self.driver, 10)
        accept = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Page "+str(numberOfPage)+"']")))

        actions = ActionChains(self.driver)
        actions.move_to_element(accept).click().perform()



