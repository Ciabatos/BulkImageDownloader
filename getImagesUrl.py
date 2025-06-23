import requests
import os
import sys
def download_images(image_urls, save_directory):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for url in image_urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:

                filename = os.path.join(save_directory, url.split('/')[-1]+".png")
                

                with open(filename, 'wb') as f:
                    f.write(response.content)
                    print(f"Downloaded: {filename +".png"}")
            else:
                print(f"Failed to download image from {url}: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")


image_urls = [

"https://0.allegroimg.com/original/012c65/1b2f422244dcb0fa2bde16a939b0",
"https://0.allegroimg.com/original/013b28/e48f79904fc7afc5587555c8cd90",


]

save_directory = '.\\downloaded_images'

download_images(image_urls, save_directory)
