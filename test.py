import telegram

from bs4 import BeautifulSoup # html분석
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

req = requests.get("http://ncov.mohw.go.kr/")
# print(req.text)

soup = BeautifulSoup(req.text, "html.parser") # 파싱

국내, 해외 = soup.find("div", class_="liveNum_today_new").find_all("span", class_="data")
국내, 해외 = str(국내.text), str(해외.text)
if "," in 국내:
국내 = 국내.replace(",", "")
if "," in 해외:
해외 = 해외.replace(",", "")
합계 = int(국내) + int(해외)

# print(합계)


ads = soup.find("div", class_="t_dp_n m_dp_n").find_all("img")
for i in ads:
print(i.get_text())


코로나 = "국내발생 : " + 국내 + "\n해외발생 : " + 해외 + "\n 합계 : " + str(합계)
print(코로나)
