import os
import requests
import shutil
from bs4 import BeautifulSoup
from termcolor import colored

output_dir = 'output'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def createOutputFolderIfNotExist():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def welcomePage():
    url_to_grab = input("Enter your URL, where you want to grab the images:\t")
    user_dir = input('In Which directory, you want to put the images?\t')
    start_num = int(input('From which page to grab START? (default: 0):\t') or '0')
    end_num = int(input('Till which page to grab: END?\t'))
    per_page_item = int(input('Page Per Items count (default: 10):\t') or '10')

    directory = f'{output_dir}/{user_dir}'

    if not os.path.exists(directory):
        os.makedirs(directory)

    pages = []

    for i in range(start_num, end_num, per_page_item):
        pages.append(i + per_page_item)

    for page in pages:
        url = f'{url_to_grab}&start=' + str(page)
        print(f' + {colored("Getting", "green")} this URL: {colored(url, "blue")}')
        spider(url, directory)


def spider(url, directory):
    image_count = 1

    # while page <= max_pages:
    # url = 'https://www.inssia.com/viewtopic.php?f=35&t=23XXX&start=' + str(page)
    sourcecode = requests.get(url, headers=headers)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext, "lxml")

    for tag in soup.findAll('img', {"class": "postimage"}):
        link = tag.get('src')  # get the link

        # Check if the tag is in expect format
        # del tag['src']
        # if tag.attrs != {';': '', 'alt': '', 'border': '0'}:
        #     continue

        filename = link.strip('/').rsplit('/', 1)[-1]  # to get the correct file name

        res = requests.get(link, headers=headers, stream=True)  # use requests to get the content of the images

        if res.status_code == 200:
            with open(f'{directory}/{filename}', 'wb') as f:
                shutil.copyfileobj(res.raw, f)
                # f.write(image)  # write the image into a file
                print(
                    f'{colored(f"    ---#{image_count} SUCCESS:", "green")}'
                    f' - Image successfully Downloaded: {colored(filename, "blue")}')

            image_count += 1
        else:
            print(f'{colored("    ---ERROR:", "red")} - Image Could not be retrieved: {colored(filename, "blue")}')

    print(colored(f"Total Images found on {url} is: {image_count}", "yellow"))


if __name__ == '__main__':
    createOutputFolderIfNotExist()
    welcomePage()
