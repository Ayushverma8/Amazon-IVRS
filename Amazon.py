

import requests
from bs4 import BeautifulSoup
from gi.repository import Notify
from time import sleep


url = "http://www.amazon.in/Kindle-Voyage-Wifi-High-Resolution-Built-/dp/B00IOY5AS6/ref=sr_1_3?ie=UTF8&qid=1457839469&sr=8-3&keywords=kindle"
min_value = 16499

print("Fetching rates..")
while True:
  try:
    r = requests.get(url)
    while r.status_code is not 200:
      sleep(2)
      r = requests.get(url)

    soup = BeautifulSoup(r.text)
    data = soup.find("span",{"style":"text-decoration: inherit; white-space: wrap;"}).contents[5]
    data_int = float(data.replace(',',''))
    
    if data_int < min_value:
    	Notify.init("Scorer")
    	scorer = Notify.Notification.new("Kindle-Voyage-Wifi-High-Resolution-Built ", data, "dialog-information")
    	scorer.show()
    
    sleep(600)

  except KeyboardInterrupt:
      break;
    
