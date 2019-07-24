
# ---- Settings------

# Naver Id,Password
id = 'naver id'
pw = 'naver password'



path = '/home/jaewon/다운로드/chromedriver' # chromedriver path

# mail_stuff
title = 'this is test'
to = 'test@gmail.com'
content = 'this is content'
attachment = '/home/jaewon/다운로드/work.xlsx'

''' Reserve Send Section'''
# r_time = [시,분]
r_time = [17,1] # 분 -> 정각(1), 15분(2), 30분(3), 45분(4)

# //*[@id="direct_hour"]/option[18] 5시
# //*[@id="direct_minute"]/option[1] 정각

p_time = r_time[0]+1
hour = '//*[@id="direct_hour"]/option['+str(p_time)+']'
minute = '//*[@id="direct_minute"]/option['+ str(r_time[1]) +']'



#p_time = list(map(lambda x:x+1,a))
