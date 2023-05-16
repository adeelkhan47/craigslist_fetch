import logging
import math
import os
import time
from io import BytesIO

import pandas as pd
import requests
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Create a new instance of the Firefox driver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
logging.basicConfig(level=logging.INFO)
wait = WebDriverWait(driver, 20)
state_to_url = states_urls = {
    "Alabama": "https://geo.craigslist.org/iso/us/al",
    "Alaska": "https://geo.craigslist.org/iso/us/ak",
    "Arizona": "https://geo.craigslist.org/iso/us/az",
    "Arkansas": "https://geo.craigslist.org/iso/us/ar",
    "California": "https://geo.craigslist.org/iso/us/ca",
    "Colorado": "https://geo.craigslist.org/iso/us/co",
    "Connecticut": "https://geo.craigslist.org/iso/us/ct",
    "Delaware": "https://geo.craigslist.org/iso/us/de",
    "Florida": "https://geo.craigslist.org/iso/us/fl",
    "Georgia": "https://geo.craigslist.org/iso/us/ga",
    "Hawaii": "https://geo.craigslist.org/iso/us/hi",
    "Idaho": "https://geo.craigslist.org/iso/us/id",
    "Illinois": "https://geo.craigslist.org/iso/us/il",
    "Indiana": "https://geo.craigslist.org/iso/us/in",
    "Iowa": "https://geo.craigslist.org/iso/us/ia",
    "Kansas": "https://geo.craigslist.org/iso/us/ks",
    "Kentucky": "https://geo.craigslist.org/iso/us/ky",
    "Louisiana": "https://geo.craigslist.org/iso/us/la",
    "Maine": "https://geo.craigslist.org/iso/us/me",
    "Maryland": "https://geo.craigslist.org/iso/us/md",
    "Massachusetts": "https://geo.craigslist.org/iso/us/ma",
    "Michigan": "https://geo.craigslist.org/iso/us/mi",
    "Minnesota": "https://geo.craigslist.org/iso/us/mn",
    "Mississippi": "https://geo.craigslist.org/iso/us/ms",
    "Missouri": "https://geo.craigslist.org/iso/us/mo",
    "Montana": "https://geo.craigslist.org/iso/us/mt",
    "Nebraska": "https://geo.craigslist.org/iso/us/ne",
    "Nevada": "https://geo.craigslist.org/iso/us/nv",
    "New Hampshire": "https://geo.craigslist.org/iso/us/nh",
    "New Jersey": "https://geo.craigslist.org/iso/us/nj",
    "New Mexico": "https://geo.craigslist.org/iso/us/nm",
    "New York": "https://geo.craigslist.org/iso/us/ny",
    "North Carolina": "https://geo.craigslist.org/iso/us/nc",
    "North Dakota": "https://geo.craigslist.org/iso/us/nd",
    "Ohio": "https://geo.craigslist.org/iso/us/oh",
    "Oklahoma": "https://geo.craigslist.org/iso/us/ok",
    "Oregon": "https://geo.craigslist.org/iso/us/or",
    "Pennsylvania": "https://geo.craigslist.org/iso/us/pa",
    "Rhode Island": "https://geo.craigslist.org/iso/us/ri",
    "South Carolina": "https://geo.craigslist.org/iso/us/sc",
    "South Dakota": "https://geo.craigslist.org/iso/us/sd",
    "Tennessee": "https://geo.craigslist.org/iso/us/tn",
    "Texas": "https://geo.craigslist.org/iso/us/tx",
    "Utah": "https://geo.craigslist.org/iso/us/ut",
    "Vermont": "https://geo.craigslist.org/iso/us/vt",
    "Virginia": "https://geo.craigslist.org/iso/us/va",
    "Washington": "https://geo.craigslist.org/iso/us/wa",
    "West Virginia": "https://geo.craigslist.org/iso/us/wv",
    "Wisconsin": "https://geo.craigslist.org/iso/us/wi",
    "Wyoming": "https://geo.craigslist.org/iso/us/wy"
}
numbers_to_states = {
    "0": "All",
    "1": "Alabama",
    "2": "Alaska",
    "3": "Arizona",
    "4": "Arkansas",
    "5": "California",
    "6": "Colorado",
    "7": "Connecticut",
    "8": "Delaware",
    "9": "Florida",
    "10": "Georgia",
    "11": "Hawaii",
    "12": "Idaho",
    "13": "Illinois",
    "14": "Indiana",
    "15": "Iowa",
    "16": "Kansas",
    "17": "Kentucky",
    "18": "Louisiana",
    "19": "Maine",
    "20": "Maryland",
    "21": "Massachusetts",
    "22": "Michigan",
    "23": "Minnesota",
    "24": "Mississippi",
    "25": "Missouri",
    "26": "Montana",
    "27": "Nebraska",
    "28": "Nevada",
    "29": "New Hampshire",
    "30": "New Jersey",
    "31": "New Mexico",
    "32": "New York",
    "33": "North Carolina",
    "34": "North Dakota",
    "35": "Ohio",
    "36": "Oklahoma",
    "37": "Oregon",
    "38": "Pennsylvania",
    "39": "Rhode Island",
    "40": "South Carolina",
    "41": "South Dakota",
    "42": "Tennessee",
    "43": "Texas",
    "44": "Utah",
    "45": "Vermont",
    "46": "Virginia",
    "47": "Washington",
    "48": "West Virginia",
    "49": "Wisconsin",
    "50": "Wyoming"
}


def load_excel_images(directory, state_data):
    for each_row in state_data:
        if each_row["Image"]:
            img_url = each_row['Image']
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            each_row['Image'] = img
    df = pd.DataFrame(state_data)
    with pd.ExcelWriter(os.path.join(directory, location)) as writer:
        df.to_excel(writer, index=False)


def scrape_url(url):
    data = []
    try:
        driver.get(url + "#search=1~gallery~0~0")
        print(url + "#search=1~gallery~0~0")
        time.sleep(1.5)
        try:
            no_results = driver.find_element("css selector", "p.no-results")
        except NoSuchElementException as nse:
            no_results = None
        if (no_results is None) or (no_results and no_results.text):
            span_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cl-page-number")))
            span_text = span_element.text
            if span_text and "of" in span_text:
                total_pages = span_text.split(" of ")[1]
                page = math.ceil(int(total_pages) / 120)
                for each in range(0, page):
                    driver.get(url + f"#search=1~gallery~{each}~0")
                    time.sleep(1.5)
                    span_element = wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cl-page-number")))
                    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img")))
                    list_of_items = driver.find_elements("css selector", "li.cl-search-result")
                    for item in list_of_items:
                        if item.text:
                            price = item.find_element("css selector", "span.priceinfo").text
                            title = item.find_element("css selector", "a.titlestring").text
                            link = item.find_element("css selector", "a.titlestring").get_attribute("href")
                            image = item.find_element("css selector", "img").get_attribute("src")
                            data.append((title, price, link, image))

        return data
    except Exception as e:
        logging.exception(e)
    except TimeoutException as te:
        no_result = driver.find_elements("css selector", "li.cl-search-result")
        return data


def fetch_for_sale_categories(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    sub_categories = {}
    count = 1
    sub_categories["0"] = ["all", "sss"]

    ul_element1 = soup.find("ul", id="sss0").find_all("li")
    for each in ul_element1:
        a_element = each.find("a")
        sub_categories[str(count)] = [a_element.text, a_element["href"]]
        count += 1
    ul_element2 = soup.find("ul", id="sss1").find_all("li")
    for each in ul_element2:
        a_element = each.find("a")
        sub_categories[str(count)] = [a_element.text, a_element["href"]]
        count += 1
    ###
    for number, value in sub_categories.items():
        print(f"{number} => {value[0]}")
    choose_category = input("\nChoose Category number : ")
    # choose_category = "0"
    if choose_category == "0":
        return ("0", "/search/sss")
    elif choose_category in sub_categories.keys():
        return (sub_categories[choose_category], sub_categories[choose_category][1])
    else:
        return None


def select_state():
    for a, b in numbers_to_states.items():
        print(f"{a} => {b}")
    choose_state = input("Choose state number : ")
    # choose_state = "2"

    if choose_state in numbers_to_states.keys():
        all_states = {}
        if choose_state == "0":
            for state, state_url in state_to_url.items():
                if state not in all_states.keys():
                    all_states[state] = []
                response = requests.get(state_url)
                soup = BeautifulSoup(response.content, "html.parser")
                ul_element_cities = soup.find("ul", class_="geo-site-list")
                if ul_element_cities:
                    ul_element_cities = ul_element_cities.find_all("li")
                else:
                    ul_element_cities = []
                for each in ul_element_cities:
                    link = each.find("a")["href"]
                    text = each.find("a").text
                    all_states[state].append((text, link))
            return all_states
        else:
            selected_state = numbers_to_states[choose_state]
            selected_state_url = state_to_url[selected_state]
            response = requests.get(selected_state_url)
            soup = BeautifulSoup(response.content, "html.parser")
            ul_element_cities = soup.find("ul", class_="geo-site-list").find_all("li")
            for each in ul_element_cities:
                if selected_state not in all_states.keys():
                    all_states[selected_state] = []
                link = each.find("a")["href"]
                text = each.find("a").text
                all_states[selected_state].append((text, link))
        return all_states
    else:
        return None


def get_directory():
    base_directory = "Result"
    counter = 0
    directory_name = base_directory
    if os.path.exists(directory_name):
        while os.path.exists(directory_name):
            counter += 1
            directory_name = f"{base_directory}_{counter}"

    os.makedirs(directory_name)
    return directory_name


if __name__ == '__main__':
    print("Craigslist Bot is Here.\n\n")
    keyword = input("Enter Keyword => ")
    min_price = int(input("Enter min price =>"))
    max_price = int(input("Enter max price =>"))
    print(max_price)
    program = True
    directory = get_directory()
    while program:
        all_subcategory = False
        selected_subcategory = None
        selected_states = select_state()
        if selected_states is None:
            print("\nInvalid State Number Chosen.")
        else:
            for state, state_cities in selected_states.items():
                state_data = []
                for each in state_cities:
                    if not all_subcategory:
                        selected_subcategory = fetch_for_sale_categories(each[1])
                        all_subcategory = True
                    if selected_subcategory is None:
                        print("\nInvalid SubCategory Number Chosen.")
                    else:
                        generated_url = each[1] + selected_subcategory[1]

                        generated_url += f"?max_price={max_price}&min_price={min_price}"
                        # generated_url += f"?hasPic=1&max_price={max_price}&min_price={min_price}"
                        if keyword:
                            generated_url += f"&query={keyword}"
                        scraped_data = scrape_url(generated_url)
                        for each_row in scraped_data:
                            state_data.append(
                                {"State": state, "City": each[0], "Image": f'=HYPERLINK("{each_row[3]}")',
                                 "Title": each_row[0],
                                 "Price": each_row[1], "Link": f'=HYPERLINK("{each_row[2]}")'})
                        print(f"{each[0]} city is processed.")

                df = pd.DataFrame(data=state_data)

                location = f"{state}.xlsx"
                df.to_excel(os.path.join(directory, location), index=False)
                # load_excel_images(directory, state_data)
                print(f"{state} Record Generated Successfully at {location}")

            all_subcategory = False
            selected_subcategory = None
            program = False
