from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

YOUTUBE_TRENDING_URL ='https://www.youtube.com/feed/trending'

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

def parseVideo(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title= title_tag.text
    url = title_tag.get_attribute('href')
    thumbnail_url = video.find_element(By.TAG_NAME, 'img').get_attribute('src')
    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text
    description = video.find_element(By.ID,'description-text').text

    return {
      "title": title,
      "url":url,
      "thumbnail_url":thumbnail_url,
      'channel': channel_name,
      'description': description
    }



if __name__ == "__main__":

  driver = getDriver()

  print('Fetching trending vidoes...')
  videos = getVideos()
  print(f'Fetched {len(videos)} videos')

  print("Parsing top ten videos...")
  videos_data = [parseVideo(video) for video in videos[0:10]]
  print(len(videos_data))

  print("Save the data to a CSV...")
  video_df = pd.DataFrame(videos_data)
  video_df.to_csv('trending.csv', index=None)
  