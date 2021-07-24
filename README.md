# Website Search

Website Indexing and Search Engine.
## Installation

The project consists of 4 parts
- Backend
- Apache Airflow
- Search Engine
- [Web Crawler](./dags/README.md)


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

And finally 
```bash
docker-compose up
```

### Apache Airflow
The `docker-compose.yml` file will setup `Apache Airflow` along with required dependencies.

Put any `Python` setup code you have into `airflow/envsetup.py`. This will run during the build stage

## Support

- [Ubuntu docker-compose invalid file](https://github.com/apache/airflow/discussions/14362)
- [MeiliSearch Typo Tolerance](https://docs.meilisearch.com/reference/under_the_hood/typotolerance.html#typo-tolerance-rules)
- [Facet Search / Categorization](https://docs.meilisearch.com/reference/features/faceted_search.html#setting-up-facets)
- [Ranking Rules](https://docs.meilisearch.com/reference/features/settings.html#ranking-rules)