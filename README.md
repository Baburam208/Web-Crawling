
# Documentation
The following is the documentation for the web crawling using Scrapy library of Python.

## Web crawling using Scrapy
We are going to scrapy [merojob.com](merojob.com) and IT & Communication category. We will be extracting data like title of job, company, location and skills set required. This is totally a educational purpose project. It is requested to reader to respect the website's terms of service and the robots.txt file while scraping.



## Introduction & quick start 

Scrapy is a powerful web crawling and scraping framework in Python. It allows us to extract data from websites and save it in various formats. Below, we will provide a brief guide on how to use Scrapy for web crawling and scraping, along with some essential concepts and code examples.

1. Install Scrapy:
Make sure you have Python and pip installed, then open your terminal and run the following command to install Scrapy.
```bash
  pip install scrapy
```

2. Create a new Scrapy project:
Navigate to the directory where you want to create your Scrapy project and run the following command.

```bash
  scrapy startproject project_name 
```

3. Define the Spider:
A Spider is the core component of Scrapy that defines how to crawl a website and how to extract data from it. You need to create a new Python file within the "spiders" folder of your project and define your Spider class.

For example, let's create a Spider to extract quotes from http://quotes.toscrape.com

```Python
# Save this as quotes_spider.py in your "spiders" folder 
import scrapy 

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

4. Running the Spider:
To run the Spider and start crawling the website, use the following commnd in your project's root directory.
```bash
  scrapy crawl quotes
```

5. Saving the Data:
By default, Scrapy outputs the scraped data to the console. However, you can save the data to a file or a database. For example, to save the data to a JSON file, use the following command.
```bash
  scrapy crawl quotes -o quotes.json 
```
This will save the extracted data in JSON format in a file named "quotes.json" in root directory.

Scrapy provides many other features like handling cookies, user-agents, handling HTTP errors, using middlewares, etc. Check the official Scrapy documentation: https://docs.scrapy.org/

## Documentation of our Implementation
1. Installation and project setup
First we install Scrapy.

```bash
  pip install scrapy 
```
and in desired folder start project. 
```bash
  scrapy startproject merojob_scrape
```
We change the directory as 
```bash
  cd merojob_scrape
``` 
and enter inside root directory of our project. You can open your favourite code editor here, we use vscode.

2. Create temporary container:
We visit the desired website and look for what data to extract such as title, product name, price, etc. In our case we extract data like job title, company name, location and desired skills.

In the `items.py` file we create temporary containers (items)
Inside `items.py` file it look like this.

```python 
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MerojobScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
```

Here each variables is assigned with scrapy.Field().

3. Define a Spider:
Navigate inside `spiders` folder and create a file named `merojob_spider.py` in it. This is the main part where we crawl a website and define how to extract data from it. 
First import scrapy and MerojobScrapeItem for items.py file 
```python 
import scrapy 
from ..items import MerojobScrapeItem
```

Create class MerojobSpiderSpider inherited from scrapy.Scrapy. 
```python
class MerojobSpiderSpider(scrapy.Spider):
```
Inside class we have following:

Give name of the spider: 
```python 
  name = 'merojpb' 
```
Since we are going crawl merojob.com and its IT & Commumication category, keep its url inside start_urls variable.
```python 
  start_urls = ["https://merojob.com/category/it-telecommunication/"]
```
define a parse method to actually parse the data from the web.
In our case it looks like following.

```python 
    def parse(self, response):
        items = MerojobScrapeItem()

        for job in response.css("#search_job .text-left"):
            title = job.css(".h4 a::text").get()
            company = job.css(".text-dark::text").get()
            location = (
                job.css(".font-12 .media-body span.text-muted span").css("::text").get()
            )
            Skills = job.css(".text-muted+ span::text").getall()

            items["title"] = title
            items["company"] = company
            items["location"] = location
            items["skills"] = Skills

            yield items

        next_page = response.css(
            "li.page-item a.pagination-next.page-link::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
```

We instantiate the MerojobSpiderSpider class, which will be the placeholder for temporary storing of the scraped data. 

After scrapping we are placing data in items tempory container. Such as
```python
items["title"] = title 
```

And the data are yielded.

The crawler will scrape all pages with the help of the pagination too. 
Full code in `merojob_spider.py` file looks like following.

```python 
import scrapy
from ..items import MerojobScrapeItem


class MerojobSpiderSpider(scrapy.Spider):
    name = "merojob"
    allowed_domains = ["merojob.com"]
    start_urls = ["https://merojob.com/category/it-telecommunication/"]

    def parse(self, response):
        items = MerojobScrapeItem()

        for job in response.css("#search_job .text-left"):
            title = job.css(".h4 a::text").get()
            company = job.css(".text-dark::text").get()
            location = (
                job.css(".font-12 .media-body span.text-muted span").css("::text").get()
            )
            Skills = job.css(".text-muted+ span::text").getall()

            items["title"] = title
            items["company"] = company
            items["location"] = location
            items["skills"] = Skills

            yield items

        next_page = response.css(
            "li.page-item a.pagination-next.page-link::attr(href)"
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
```

3.1. Web crawling and Following links:
Get following links insice <a> anchor tag as follows.
```python 
  next_page = response.css("li.page-item a.pagination-next.page-link::attr(href)")
```
For every not None next_page we follow the links in next_page and callback the parse function as shown below.

```python
  if next_page is not None:
    yield response.follow(next_page, callback=self.parse)
```


4. Running scrapy 
you can run the scrapy with following command.
```bash
  scrapy crawl merojob 
```
This will scrape the web, you can see the output in the command while executing above command.

5. Saving into .db file using SQLite3 database:
For this we have develop pipeline, so that the crawled data will be saved as database.
All these steps like database connection, schema/table creatiion, insertion, commit and close of the database is done in the `pipeline.py` file. But in our case we have created separate file named `custom_db_pipeline.py` file where all these happens. 

To refer this custom pipeline we include following code in the `settings.py` file.
```python
  ITEM_PIPELINES = {
    "merojob_scrape.custom_db_pipeline.CustomDBPipeline": 300,
  }
```

and comment out default one:
```python
  # ITEM_PIPELINES = {
  #  "merojob_scrape.custom_db_pipeline.MerojobScrapePipeline": 300,
  # }
```

For database:
we have database name spider name (i.e., merojob)_timestamp (eg. merojob_20230721_014301.db), timestamp change every time `scrapy crawl merojob` command is executed.

Scrapy by default save the `.db` files inside root directory of the project, which may clutter the source file or root directory. So, we customize it, we are saving each scraped data in `.db` files inside the directory `database`. 
First we create include following line in settigs.py file 

```python 
  DB_FOLDER = "database"
```

Import following in the `custom_db_pipeline.py` file.

```python 
  import sqlite3
  import os
  from datetime import datetime
  from os import path
  from .settings import DB_FOLDER
```

Database schema is as follows:

Table Name: "jobs_table"

| Column | Data Type |
|--------|-----------|
|title   | TEXT      |
|company | TEXT |
|location| TEXT |
|skills  | TEXT |


The overall `custom_db_pipeline.py` file looks like this: 
```python 
import sqlite3
import os
from datetime import datetime
from os import path
from .settings import DB_FOLDER


class CustomDBPipeline:
    def open_spider(self, spider):
        # Generate a unique name for the .db file based on the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        db_name = f"{spider.name}_{timestamp}.db"
        db_path = path.abspath(os.path.join(DB_FOLDER, db_name))
        # Create a new database file and connection
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # Assuming your 'item' contains the scraped data and 'table_name' contains the table name
        table_name = "jobs_table"
        # Create a new table for each spider run
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} (title text, company text, location text, skills text);"
        )

        # Insert the scraped data into the table
        self.cursor.execute(
            f"INSERT INTO {table_name} VALUES (?, ?, ?, ?);",
            (item["title"], item["company"], item["location"], str(item["skills"])),
        )
        # Commit the changes to the database
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # Close the database connection when the spider is closed
        self.conn.close()

```
With each run of the scrapy, the program will create new .db file and save it to the database directory. 

6. Bypass restrictions using user-agent:
Usually website restricts to crawl it. To avoid restrictions we create user-agents and crawl the website. This can be done using scrapy-user-agents package.

First install `scrapy-user-agents` with following command.
```bash
  pip install scrapy-user-agents 
```

in the `settings.py` file include following piece of code.

```python 
  DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy_user_agents.middlewares.RandomUserAgentMiddleware": 400,
}
```

This take a little bit more time than previous to crawl web.
For more details visit https://pypi.org/project/scrapy-user-agents/

