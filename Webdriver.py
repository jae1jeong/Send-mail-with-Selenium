from selenium import webdriver
import config
import time
from selenium.webdriver.common.keys import Keys





class N_D:


    def __init__(self):
        self.driver = webdriver.Chrome(path)
        self.login(id,pw)


    def login(self,id,pw):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.execute_script("document.getElementsByName('id')[0].value=\'" + id+ "\'")
        self.driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw+ "\'")
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        time.sleep(1)
        print('login')



    def write_email(self,who,title,content,reserve = True):
        self.driver.get('https://mail.naver.com/')
        self.driver.find_element_by_xpath('//*[@id="nav_snb"]/div[1]/a[1]').click()
        time.sleep(2)
        # To
        self.driver.find_element_by_xpath('//*[@id="toInput"]').send_keys(who)
        # title
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys(title)
        # content(iframe)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath('//*[@id="se2_iframe"]'))
        elem = self.driver.find_element_by_xpath('/html/body')
        elem.send_keys(content)
        self.driver.switch_to_default_content()



        if reserve:
            hour = config.hour
            minute = config.minute
            print('reserve activated')
            self.driver.find_element_by_xpath('//*[@id="addReserve"]/a').click()
            self.driver.find_element_by_xpath(hour)
            self.driver.find_element_by_xpath(minute)
            self.driver.find_element_by_xpath('//*[@id="directReserve"]/div[2]/span[1]/button').click()
            self.driver.find_element_by_xpath('//*[@id="sendBtn"]').click()



        else:
            self.driver.find_element_by_xpath('//*[@id="sendBtn"]').click()

    def clean(self):
        self.driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
        self.driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        self.driver.get('https://mail.naver.com/')
        self.driver.find_element_by_xpath('//*[@id="searchKeyWord"]').send_keys("(광고)")
        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="searchKeyWord"]').send_keys(Keys.ENTER)

        for i in range(500):
            self.driver.find_element_by_xpath('//*[@id="mailCheckAll"]').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="listBtnMenu"]/div[1]/span[2]/button[2]').click()
            time.sleep(2)



    def __del__(self):
        self.driver.quit()
        print('Terminated')



if __name__ == '__main__':
    # ------------------------
    id = config.id
    pw = config.pw
    path = config.path
    title = config.title
    content = config.content
    to = config.to
    # ------------------------


    a = N_D()
    #a.write_email(to,title,content,False)



