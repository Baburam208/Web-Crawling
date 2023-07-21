# Documentation

## Introduction

Scrapy is a powerful web crawling and scraping framework in Python. It allows you to extract data from websites and save it in various formats such as .json, .csv or .db file. Below, I'll provide a brief guide on how to use Scrapy for web crawling and scraping, along with essential code snippets.

I am going to scrape merojob.com, IT & Communication category. I am going to extract job title, company, location and skills. More data are scraped with pagination. This is fully an educational purpose web scraping project, and I always suggest to follow robots.txt.

1. Install Scrapy:
   Make sure you have Python and pip installed. Open command prompt (windows) and run the following command to install Scrapy.

   `pip install scrapy`

2. Create a new Scrapy project.
   Navigate to the directory where you want to create your Scrapy project and run the following command
   `scrapy startproject project_name`

   `(scrapy startproject merojob_scrape)`
   This will create a new folder with the name `merojob_scrape`, containing the necessary files and folder structure.

3. Define the Spider
   A Spider is the core component of Scrapy that defines how to crawl a website and how to extract data from it. You need to create a new Python file within the 'spiders' folder of your project and define your Spider class.

4. Running the Spider
   To run the Spider and start crawling the website, use the following command in your project's root directory.
   `scrapy crawl merojob` # `merojob` is name of Spider
