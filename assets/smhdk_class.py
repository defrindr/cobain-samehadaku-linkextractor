import requests, re
from bs4 import BeautifulSoup
import time

def link(link2extract):
    linkAdsre1 = requests.get(link2extract)
    ads1 = BeautifulSoup(linkAdsre1.content, 'html.parser')
    for linkRe in ads1.find_all('a', attrs={'rel': 'nofollow'}):
        linkAds1 = linkRe.get('href')

    linkAdsre2 = requests.get(linkAds1)
    ads2 = BeautifulSoup(linkAdsre2.content, 'html.parser')
    link = ('').join(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ads2.text))
    link = link.split('https://www.greget.space/geological')
    return str(('').join((linkExract for linkExract in link)))


def main():
    print('\n======================================\n\n     Defri I M * GreyXploiter\n\n=====\n=\n===== amehadaku\n    =     Link\n=====     Extractor\n\n======================================\n\t')
    try:
        choose = int(input('1. Single Link\n2. Mass Link\n\n[?] Choose : '))
        if choose == 1:
            link2extract = input('Enter Link : ')
            print(f'''[+] Extracted => {(link(link2extract))}''')
        else:
            if choose == 2:
                fileName = input('Enter path to txt : ')
                with open(fileName) as (file):
                    data = file.read()
                    i = 1
                    for link2extract in data.split('\n'):
                        print(f'''[{i}] => {(link(link2extract))}''')
                        i += 1

                    print('\n[+] Complete Extracted Link')
            else:
                print('Number Not Found !!! ')
                exit()
    except Exception as e:
        print(f'''Error : {e}''')
        exit()

