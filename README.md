# Selenium을 이용한 네이버 이메일 보내기(+Pyautogui)
---
###  사용법

#### * 라이브러리 설치
    pip install selenium
    pip install pyautogui(첨부파일 보낼때 사용)
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

     # Attachment Section
     filename = 'file name here'

     # Reserve Send Section
     # r_time = [시,분]
     r_time = [17,1] # 분 -> 정각(1), 15분(2), 30분(3), 45분(4)

     # //*[@id="direct_hour"]/option[18] 5시
     # //*[@id="direct_minute"]/option[1] 정각

     p_time = r_time[0]+1
     hour = '//*[@id="direct_hour"]/option['+str(p_time)+']'
     minute = '//*[@id="direct_minute"]/option['+ str(r_time[1]) +']'





#### 3. Methods


+ #### write_email
      write_email(self,who,title,content,reserve = True,attach = True)
      예약 발송한다면 reserve=True, 첨부파일을 전송한다면 attach=True

+ #### clean
   재미로 만든 광고 메일 삭제하기입니다.(엄청 간단하게 만든 거라 허술합니다)


#### __첨부파일 관련__

Selenium으로 네이버 이메일 첨부파일을 할려고 시도하였으나 태그가 input 태그가 아니라서 pyautogui를 사용했습니다.
제 노트북 기준으로 코드를 만든 거라 윈도우나 맥은 첨부파일을 첨부하는게 되지 않습니다.(리눅스 우분투만 가능)
이점 참고하여 사용해주시면 감사하겠습니다.
