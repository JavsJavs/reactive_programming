import asyncio
import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup

def sincrono():
    urls = [
        'https://www.imdb.com/',
        'https://www.amazon.es/',
    ]
    for url in urls:
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        for img in soup.find_all('img'):
            img_url = img['src']
            try:
                img_response = requests.get(img_url)
                try:
                    with open (f'downloaded_images/{img_url.split("/")[-1]}', 'wb') as f:
                        f.write(img_response.content)
                except OSError:
                    pass
                except IOError:
                    pass
            except:
                pass


async def main():
    urls = [
        'https://www.imdb.com/',
        'https://www.amazon.es/',
    ]
    pass

if __name__ == '__main__':
    #asyncio.run(main())
    sincrono()
