from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from PIL import Image

import datetime

x = datetime.datetime.now()

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = 'https://g1.ipcamlive.com/player/player.php?alias=607de7cf685fa'

driver.get(url)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)

driver.set_window_size(S('Width'), S('Height'))

driver.save_screenshot('web_screenshot.png')

image = Image.open('web_screenshot.png')

image.show()