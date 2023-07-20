# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

'''
class MerojobScrapePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self, spider):
        # Set the name of the database file
        db_name = f"{spider.name}.db"
        self.conn = sqlite3.connect(db_name)
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists jobs_table""")

        self.curr.execute(
            """
            create table jobs_table (
                title text,
                company text,
                location text,
                skills text
            )
            """
        )

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(
            """
            insert into jobs_table values (?, ?, ?, ?)
            """,
            (item["title"], item["company"], item["location"], str(item["skills"])),
        )
        self.conn.commit()

'''

"""
class MerojobScrapePipeline:
    def open_spider(self, spider):
        # Set the name of the database file
        db_name = f"{spider.name}.db"
        # Create a new database file and connection
        self.conn = sqlite3.connect(db_name)
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
"""
