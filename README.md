# Selenium을 이용한 네이버 이메일 보내기
---
###  사용법

#### * 라이브러리 설치
    pip install selenium
#### * 크롬 드라이버 설치 http://chromedriver.chromium.org/downloads

#### 1. Clone이나 다운로드

#### 2. config.py 수정하기
     # ---- Settings------

     # Naver Id,Password
     id = 'naver id'
     pw = 'naver password'



     path = '/home/jaewon/다운로드/chromedriver' # chromedriver path

     # mail_stuff
     title = 'this is test'
     to = 'test@gmail.com'
     content = 'this is content'

     ''' Reserve Send Section'''
     # r_time = [시,분]
     r_time = [17,1] # 분 -> 정각(1), 15분(2), 30분(3), 45분(4)

     # //*[@id="direct_hour"]/option[18] 5시
     # //*[@id="direct_minute"]/option[1] 정각

     p_time = r_time[0]+1
     hour = '//*[@id="direct_hour"]/option['+str(p_time)+']'
     minute = '//*[@id="direct_minute"]/option['+ str(r_time[1]) +']'





#### 3. Methods


+ #### write_email
      write_email(self,who,title,content,reserve = True) 예약 발송한다면 reserve = True

+ #### clean
   재미로 만든 광고 메일 삭제하기입니다.(엄청 간단하게 만든 거라 허술합니다)
