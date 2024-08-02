import time
from datetime import datetime
import webbrowser
from bs4 import BeautifulSoup
import requests
import random
import pickle
import shutil
import json
import schedule
import pyautogui
import keyboard
import pandas as pd

data_links = []
data_texts = []

source_input = input("\nEnter URL of website to scrape: ")
source1 = str(source_input)

def scheduled_scrape():

    response_code = requests.get(source1)

    if response_code.status_code == 200:
    # grabs the data from the sources (which can be modified)
        print('\nScraping Content...')
        time.sleep(2)
        r = requests.get(source1)
        soup = BeautifulSoup(r.content, 'html.parser')

        print('\nTEXT:\n ')
        lines = soup.find_all('p')

        for line in lines:
            show_data = print(line.text)
            data_texts.append(line.text)
            time.sleep(2)

        print('LINKS:\n ')
        for link in soup.find_all('a'):
            show_data2 = print(link.get('href'))
            data_links.append(link.get('href'))
            time.sleep(1)

        # Cleaning the scraped data

        print('Cleaning Data...')
        time.sleep(2)
        df = pd.DataFrame(data_texts)
        df_links = pd.DataFrame(data_links)

        df.drop_duplicates(inplace=True)
        df.fillna(method='ffill', inplace=True)


        # Storing data in JSON file

        print('Storing Data...')
        time.sleep(2)
        file_name = input("\nEnter file name to save text data: ")
        file_name2 = input('\nEnter file name to save link data: ')

        with open(f"{file_name}.json", 'w') as json_file:
            json.dump(df, json_file)

        with open(f"{file_name2}.json", 'w') as json_file:
            json.dump(df_links, json_file)

    else:
        pass

while True:
    scheduled_scrape()
    schedule.every(5).minutes.do(scheduled_scrape)


    