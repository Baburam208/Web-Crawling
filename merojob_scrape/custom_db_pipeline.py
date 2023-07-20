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
