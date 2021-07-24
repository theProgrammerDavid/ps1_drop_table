# centos: libxslt-devel python-devel
# debian: 
import re
import time
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from tld import get_tld

SCRAPE_URL = 'https://www.bajajfinservmarkets.in/sitemap.xml'
CRAWL_URL_MATCH = get_tld(SCRAPE_URL, as_object=True)

class SiteMapCrawler:
    def __init__(self, start_page):
        self.visited_url = {}
        self.queue_url = [start_page]
        self.summary = {}
        self.keywords = {}
        self.CRAWL_URL_MATCH = get_tld(CRAWL_URL, as_object=True)

    
    def get_url_list(self, url):
        print('crawling: %s'%(url))
        try:
            url = url.lower()
            url = url[:len(url)-11]
            
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

           
            response = requests.get(url, timeout=10.0)
            raw_html = response.text
            soup = BeautifulSoup(raw_html)
            heading = soup.findAll("div", class_="paragraph-rte")
            title = heading.select("div > h2").get_text(strip=True)
            print(title)
            parsed_html = html.fromstring(raw_html)
        except:
            return
        
        url_title_item = parsed_html.xpath('//title')
        url_title = '(NO TITLE)'
        try:
            url_title = url_title_item[0].text
        except:
            url_title = '(ERROR TITLE)'
        self.visited_url[url] = url_title
        self.summary[url] = article.summary
        self.keywords[url] = article.keywords
    
        for a in parsed_html.xpath('//a'):
            raw_url = a.get('href')
            if raw_url is None:
                continue
            
            parsed_url = urljoin(url, raw_url)
            if parsed_url not in list(self.visited_url.keys()) and parsed_url not in self.queue_url:
                self.queue_url.append(parsed_url)
    
    
        
    def start_crawling(self, threshold=-1):
        while threshold != 0:
            print(len(self.queue_url))
            this_url = self.queue_url[0]
            
            try:
                if get_tld(this_url, as_object=True).fld != CRAWL_URL_MATCH.fld:
                    self.queue_url = self.queue_url[1:]
                else:
                    
                    page = requests.get(this_url)
                    sitemap_index = BeautifulSoup(page.content, 'html.parser')
                    urls = [element.text for element in sitemap_index.findAll('loc')]
                    for x in urls:
                        self.queue_url.append(x)

                    self.get_url_list(this_url)
            except Exception as e: 
                self.queue_url = self.queue_url[1:]
                print(e)
            
            if len(self.queue_url) == 1:
                break
            else:
                self.queue_url = self.queue_url[1:]
                
            threshold -= 1
        
        print('DONE!')
        
 

c = SiteMapCrawler(SCRAPE_URL)
c.start_crawling(threshold=10)