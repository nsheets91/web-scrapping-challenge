# importing dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_from_all_mars_sites(): 
    # creating driver and browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of news page to be scraped and visit it with browser
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    # creating HTML object
    html = browser.html
    # initiating soup object for news scrape
    news_soup = BeautifulSoup(news_html, 'html.parser')
    # searching html for latest news
    latest_news = news_soup.select_one('ul.item_list li.slide')
    # getting title and paragraph for latest article
    title = latest_news.find('div', class_='content_title').text
    paragraph = latest_news.find('div', class_='article_teaser_body').text

    # URL of image page to be scraped and visit it with browser
    mars_url = 'https://spaceimages-mars.com'
    browser.visit(mars_url)

    # HTML object
    html = browser.html

    # instatiating beautiful soup object and parsing using lxml
    image_soup = BeautifulSoup(html, 'lxml')
    # accessing the image url
    image = image_soup.find('a', class_='showimg fancybox-thumbs')['href']
    # slicing the page url to attach image url in a string
    new_space_image_url = space_image_url[0:-10]
    # attaching the image url to sliced page url
    image_url = f"{new_space_image_url}{image}"

    # URL of facts page to be scraped and visit it with browser
    facts_url = 'https://galaxyfacts-mars.com'
    # parsing html using pandas
    facts_tables = pd.read_html(facts_url)


    # turning pandas parse into a dataframe
    facts_df = facts_tables[0]
    # cleaning up the table for printing
    facts_df = facts_df.rename(columns={0: " ", 1: "Mars"})
    facts_df.set_index(" ", inplace=True)
    # converting df to html with pandas
    facts_html = facts_df.to_html()

    # turning pandas parse into a dataframe
    facts_df = facts_tables[0]
    # cleaning up the table for printing
    facts_df = facts_df.rename(columns={0: " ", 1: "Mars"})
    facts_df.set_index(" ", inplace=True)
    # converting df to html with pandas
    facts_html = facts_df.to_html()

    # URL of image page to be scraped and visit it with browser
    hemi_image_url = 'https://marshemispheres.com/'
    browser.visit(hemi_image_url)

    # HTML object
    html = browser.html

    # instatiating beautiful soup object and parsing with html
    hemi_image_soup = BeautifulSoup(html, 'html.parser')

    # accessing the names of the links to click and storing in a list to iterate over
    hemi_names = hemi_image_soup.find_all('div', class_='description')
    hemi_name_list = []
    for name in hemi_names:
        hemi_name_list.append(name.a.h3.text)

    # creating list for dicts for return
    hemi_list = []

    # looping over the pages, scraping, creating dict, and adding to list
    for name in hemi_name_list:
            try:
                # clicking into the page to get the image url
                browser.links.find_by_partial_text(name).click()
                
                # getting image_url
                html = browser.html
                image_url_soup = BeautifulSoup(html, 'html.parser')
                dl_image_url = image_url_soup.find_all('dd')[1].a['href']
                image_url = f"{dl_image_url}/full.jpg"
                
                # getting title from name
                title = name[0:-9]
                # creating dict and adding to list
                entry = {'title': title, 'image_url': image_url, 'dl_image_url': dl_image_url}
                hemi_list.append(entry)
                # redirecting back to the main page to continue loop
                browser.visit(hemi_image_url)
                print("Scrape successful!")
            except:
                print("Scrape unsuccessful!")
    scraped_data = {
        ""
    }
    return scraped_data