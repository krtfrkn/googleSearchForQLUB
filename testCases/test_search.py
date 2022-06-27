from pageObjects.SearchPage import SearchPage
from selenium.webdriver.common.by import By

class Test_Search:

    baseURL = "https://www.google.com/"
    searchItem = "Hello World"
    numberOfPage = 2

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Google":
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            assert False

    def test_search_function(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.sp = SearchPage(self.driver)
        self.sp.setSearchItem(self.searchItem)
        self.sp.clickSearch()
        act_title = self.driver.title
        pageResult = self.driver.find_element(By.ID,self.sp.pageResult_id).text
        result = pageResult.__contains__("Sayfa ")

        if act_title=="Hello World - Google'da Ara":
            self.driver.quit()
            assert True
        else:
             self.driver.quit()
             assert False

        if result==False:
            self.driver.quit()
            assert True

        else:
             self.driver.quit()
             assert False

    def test_selected_page(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.sp = SearchPage(self.driver)
        self.sp.setSearchItem(self.searchItem)
        self.sp.clickSearch()
        self.sp.clickPage(self.numberOfPage)
        act_title = self.driver.title
        pageResult = self.driver.find_element(By.ID,self.sp.pageResult_id).text
        result = pageResult.__contains__("Sayfa "+str(self.numberOfPage))

        if act_title=="Hello World - Google'da Ara":
            self.driver.quit()
            assert True
        else:
             self.driver.quit()
             assert False

        if result==True:
            self.driver.quit()
            assert True
        else:
             self.driver.quit()
             assert False

