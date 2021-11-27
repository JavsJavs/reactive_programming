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
                    print(f'{err=}')
                except IOError as err:
                    print(f'{IOError}')
            except:
                print('get error')

async def getImage(image_url):
    async with aiohttp.ClientSession() as imgsession:
        async with imgsession.get(image_url) as imgresp:
            try:
                async with aiofiles.open(f'downloaded_images/{image_url.split("/")}'):
                    await f.write(await imgresp.read())
            except OSError as err:
                print(f'{err=}')
            except IOError as err:
                print(f'{IOError}')


async def main():
    urls = [
        'https://www.imdb.com/',
        'https://www.amazon.es/',
    ]
    t = []
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                soup = BeautifulSoup(await resp.text(), 'html.parser')
                for img in soup.find_all('img'):
                    task = asyncio.create_task(getImage(img_url))
                    t.append(task)
    await asyncio.gather(*t)

if __name__ == '__main__':
    asyncio.run(main())
    sincrono()
