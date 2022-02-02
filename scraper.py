from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL ='https://www.youtube.com/feed/trending'

# Setting some options for the virtual browser and get driver
def getDriver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def getVideos():
  driver.get(YOUTUBE_TRENDING_URL)
  videos=driver.find_elements(By. TAG_NAME, 'ytd-video-renderer')
  return videos


if __name__ == "__main__":

  # Getting the data from webpage
  driver = getDriver()
  print('Fetching trending vidoes')
  videos = getVideos()
  print(f'Fetched {len(videos)} videos')

  