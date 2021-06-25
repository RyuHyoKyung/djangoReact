# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# class Chicago():
#
#     url = 'https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
#     driver_path = 'C:\Program Files\Google\Chrome\chromedriver'
#     rank = []
#     cafe_name =[]
#     food = []
#
#
#
#
#     def scrap(self):
#         driver = webdriver.Chrome(self.driver_path)
#         # webdriver.Chrome('C:\Program Files\Google\Chrome\chromedriver').get('https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/')
#         driver.get(self.url)
#         soup = BeautifulSoup(driver.page_source, 'lxml')
#         all_td = soup.find_all('div', 'sammy')
#         for item in all_td:
#             self.rank.append(item.find(class_='sammyRank').text)
#             temp = item.find(class_='sammyListing').text)
#             self.cafe_name.append()
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     c = Chicago()
#     c.scrap()
