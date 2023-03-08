# Website Search

This project was developed for the Bajaj HackRx2.0 hackathon according to a problem statement. Its features are - 

- Typo resistant search engine
- Real time searches
- Breadth First Search web crawler
- Scheduling with Apache Airflow
- Container first approach

## Demonstration

[![Demonstration video](https://img.youtube.com/vi/BCukys9cff4/0.jpg)](https://www.youtube.com/watch?v=BCukys9cff4)

## Installation

The project consists of 4 parts
- Apache Airflow
- Search Engine
- [Web Crawlers](./dags/README.md)
- Backend (incomplete, exists to serve the static HTML file in the `website` folder)

The project can be started with `docker-compose`.


To get started, clone the repo and cd into it 
```bash
git clone https://github.com/HackRx2-0/ps1_drop_table.git && cd ps1_drop_table
```

Create an `.env` file 
```bash
mkdir ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

Run the initial setup. This will create the required databases
```bash
docker-compose up airflow-init
```

Then lets start the services
```bash
docker-compose up
```

And finally, install dependencies
```bash
pip install meilisearch newspaper3k tld
```
> Refer to the [newspaper3k documentation](https://github.com/codelucas/newspaper) if you face errors

### Skipping Apache Airflow

Apache Airflow is used for scheduling the web-crawlers through the DAGs provided. However, you can skip its setup and follow the steps mentioned here.

#### Step 1: 
Start an instance of Meilisearch using docker or through other ways as given in the [documentation](https://docs.meilisearch.com/learn/getting_started/quick_start.html)

```bash
docker run -it --rm \
  -p 7700:7700 \
  -v $(pwd)/meili_data:/meili_data \
  getmeili/meilisearch:v1.0

```

#### Step 2: 

Using your webcrawler of choice, replace the `SCRAPE_URL`, the client host URL and the client index. Once this is done, use `python3` to run the scraper

#### Step 3:

Install dependencies
```bash
pip install meilisearch newspaper3k tld
```
> Refer to the [newspaper3k documentation](https://github.com/codelucas/newspaper) if you face errors

### Using Apache Airflow
The `docker-compose.yml` file will setup `Apache Airflow` along with required dependencies.

Put any `Python` setup code you have into `airflow/envsetup.py`. This will run during the build stage

Using your webcrawler of choice, replace the `SCRAPE_URL`, the client host URL and the client index. Once this is done, use `python3` to run the scraper

## Support

- [Ubuntu docker-compose invalid file](https://github.com/apache/airflow/discussions/14362)
- [MeiliSearch Typo Tolerance](https://docs.meilisearch.com/reference/under_the_hood/typotolerance.html#typo-tolerance-rules)
- [Facet Search / Categorization](https://docs.meilisearch.com/reference/features/faceted_search.html#setting-up-facets)
- [Ranking Rules](https://docs.meilisearch.com/reference/features/settings.html#ranking-rules)
