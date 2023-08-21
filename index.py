import os
from datetime import datetime
os.system("pip3 install -r requirements.txt")
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import telegram_send_msg as tg
from selenium.webdriver.common.by import By
import random
from webdriver_manager.firefox import GeckoDriverManager
try:
    os.system("pip3 install PyVirtualDisplay==1.3.2")
except:
    pass
from pyvirtualdisplay import Display
import time
import random
import requests
options = webdriver.ChromeOptions()
options.add_argument("----start-maximized")
options.add_argument("--window-size=1440,789")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
autocontrol = 'yes'
if autocontrol == 'yes':
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1420,1080")
    display = Display(visible=0, size=(1420, 1080))
    display.start()
ip_address=requests.get('https://api.ipify.org').text

count = 0

while True:
    try:
        import random
        wait_time_arr = []
        for i in range(0,101):
            if (i<4):
                random_number = random.randint(0, 60)
                wait_time_arr.append(random_number)
            elif(i>4 and i<=7):
                random_number = random.randint(60, 120)
                wait_time_arr.append(random_number)
            elif(i>7 and i<=10):
                random_number = random.randint(120, 180)
                wait_time_arr.append(random_number)
            elif(i>10  and i<= 14) :
                random_number = random.randint(180, 240)
                wait_time_arr.append(random_number)
            elif(i>14  and i<= 47) :
                random_number = random.randint(240, 300)
                wait_time_arr.append(random_number)
            elif(i>47  and i<= 61) :
                random_number = random.randint(300, 360)
                wait_time_arr.append(random_number)
            elif(i>61  and i<= 100) :
                random_number = random.randint(360, 660)
                wait_time_arr.append(random_number)  
        random.shuffle(wait_time_arr)
        print(wait_time_arr)


        for time_wait in wait_time_arr:   
            try:   
                uas = []
                import csv
                with open("./DesktopUserAgent.csv", "r") as csvfile:
                    reader_variable = csv.reader(csvfile, delimiter=",")
                    for row in reader_variable:
                        uas.append(row)
                ua = random.choice(uas)
                print('ua', ua)
                print(f"user-agent={ua}")
                options.add_argument(f"user-agent={ua[0]}")
                driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install(), options=options)
                driver.implicitly_wait(30)
                driver.get('chrome://settings/')
                driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.50);') #keep # at begining to remove zoom settings
                driver.get("https://superadme.com/tracker/click.php?key=oiszj51gth6ie7jncx9z")        
                import random
                # random_number = random.randint(60, 180)
                print(f"Sleeping for {time_wait} seconds")
                time.sleep(time_wait)
                driver.get_screenshot_as_file("screenshot.png")
                time.sleep(2)
                if(count == 0):
                    tg.telegram_bot_sendimage('screenshot.png',2,'','ip_address::'+ip_address+"updated",'ip_address::'+ip_address+"updated",'')
                    count = count +1
                #watch one episode for 30 seconds
                time.sleep(10)
                driver.execute_script("location.reload();")
                print(f"Sleeping till {time.ctime(time.time()+30)}")
                time.sleep(10)
                ############################################
                driver.quit()
            except Exception as e:
                    print(e)
                    try:
                        driver.quit()
                    except:
                        pass            
    except Exception as e:
        print(e)
        try:
            driver.quit()
        except:
            pass