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
