# Web Scrapers

There are 2 web-scrapers in question 
- SiteMap based scraper
- BFS based scraper



Both of them are similar but work on a different principle. 

The `SiteMap` scraper uses the `sitemap.xml` file and does a BFS search on all of the URLs in it whereas the `BFS scraper` scrapes the webpage and visits all of the links using the `BFS`algorithm.

Both of the scrapers keep track of the URls visited

#### MeiliSearch bindings
MeiliSearch has [python bindings](https://github.com/meilisearch/meilisearch-python) which can be installed via pip

```bash
pip install meilisearch
```