import os
import requests
from bs4 import BeautifulSoup
from termcolor import colored
from urllib3.exceptions import InsecureRequestWarning
import concurrent.futures
import subprocess

global directory
output_dir = 'output'
finalimages = []
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def createOutputFolderIfNotExist():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def welcomePage():
    global user_dir

    url_to_grab = input("Enter your URL, where you want to grab the images:\t")
    user_dir = input('In Which directory, you want to put the images?\t')
    start_num = int(input('From which page to grab START? (default: 0):\t') or '0')
    end_num = int(input('Till which page to grab: END?\t'))
    per_page_item = int(input('Page Per Items count (default: 10):\t') or '10')

    directory = f'{output_dir}/{user_dir}'

    if not os.path.exists(directory):
        os.makedirs(directory)

    pages = []
    urls = []
    for i in range(start_num, end_num, per_page_item):
        pages.append(i + per_page_item)

    for page in pages:
        url = f'{url_to_grab}&start=' + str(page)
        urls.append(url)

    with concurrent.futures.ThreadPoolExecutor(100) as executor: # Adjust Threads as per your network and PC config
        executor.map(spider, urls)
    

def spider(links):
    # url = 'https://www.inssia.com/viewtopic.php?f=35&t=23XXX&start=' + str(page)
    sourcecode = requests.get(links, headers=headers, verify=False, timeout=None)
    plaintext = sourcecode.text
    soup = BeautifulSoup(plaintext, "lxml")

    img_count = 0
    for tag in soup.findAll('img', {"class": "postimage"}):
        img_count += 1
        link = tag.get('src')  # get the link
        finalimages.append(link)
    print(colored(f"Current working on {links} and found {img_count}", "yellow"))

def imgdownloader():
    cmd = ".\\aria2c.exe -x 16 -i actress.txt -d output\\"+ user_dir +"\\"
    subprocess.call(cmd, shell=True) 

if __name__ == '__main__':
    file = open('actress.txt','w')
    createOutputFolderIfNotExist()
    welcomePage()
    for img in finalimages:
        file.write(img+'\n')
    file.close()
    imgdownloader()
    