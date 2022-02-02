import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL ='https://www.youtube.com/feed/trending'

# Scrappig from the link
response = requests.get(YOUTUBE_TRENDING_URL)
print("Status Code:", response.status_code)

# save the scraped file into a html file
with open("trending.html",'w') as f:
  f.write(response.text)

# let's do Scrappig
doc =BeautifulSoup(response.text, 'html.parser')
print(doc.title)

# FInd all the video divs
video_divs = doc.find_all('div', class_='ytd-video-renderer')
print(f"Found {len(video_divs)} videos")