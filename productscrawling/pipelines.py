# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import mysql.connector


class NeuralcrawlingPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # connect to Connect to DB
        try:
            self.conn = mysql.connector.connect(
                user='root',
                password='wp2049GYZ!',
                host='localhost',
                port=3306,
                database='items_data'
            )
        except mysql.error as e:
            print(f"Error connecting to DB platform : {e}")
            sys.exit(1)

        self.curr = self.conn.cursor()


    #id INT AUTO_INCREMENT PRIMARY KEY,
    def create_table(self):
        #self.curr.execute("""DROP TABLE IF EXISTS quotes_tb1""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS ItemsTableTest(
            id MEDIUMINT NOT NULL AUTO_INCREMENT,
            site text,
            producer text,
            title text,
            price text,
            url text,
            availability text,
            PRIMARY KEY (id)
            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        self.curr.execute("""INSERT into ItemsTableTest values (NULL,%s,%s,%s,%s,%s,%s)""",(
            item.get('main_site'),
            item.get('producer'),
            item.get('title'),
            item.get('price'),
            item.get('url'),
            item.get('availability')
        ))

        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()




