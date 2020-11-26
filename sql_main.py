# coding=utf-8
import datetime
import logging
import time

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from updater.faker.products import Faker

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)

# connect
db_config = read_db_config()
conn = MySQLConnection(**db_config)
cursor = conn.cursor()


def close_connection():
    cursor.close()
    conn.close()


def insert_books(sku, name, description, rating, quantity_in_stock,
                 import_price, final_price, discount, discount_percent,
                 promotion_price, publisher, number_of_pages):
    query = "INSERT INTO books(sku, name, description, rating, quantity_in_stock, import_price, final_price, discount, discount_percent, promotion_price, publisher, number_of_pages) " \
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (sku, name, description, rating, quantity_in_stock,
            import_price, final_price, discount, discount_percent,
            promotion_price, publisher, number_of_pages)
    cursor.execute(query, args)


def insert_attributes(sku, id, type, name, value_id):
    query = "INSERT INTO attributes(sku, id, type, name, value_id) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (sku, id, type, name, value_id)
    cursor.execute(query, args)


def insert_category(sku, id, type, name, parent_id, level):
    query = "INSERT INTO categories(sku, id, type, name, parent_id, level) " \
            "VALUES(%s,%s,%s,%s,%s, %s)"
    args = (sku, id, type, name, parent_id, level)
    cursor.execute(query, args)


def insert_channels(sku, id, type, name):
    query = "INSERT INTO channels(sku, id, type, name) " \
            "VALUES(%s,%s,%s,%s)"
    args = (sku, id, type, name)
    cursor.execute(query, args)


def insert_quantity(sku, last_1_week, last_2_week, last_3_week,
                    last_1_month, last_2_month, last_3_month,
                    last_1_year):
    query = "INSERT INTO quantity(sku, last_1_week, last_2_week, last_3_week, last_1_month, last_2_month, last_3_month, last_1_year) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    args = (sku, last_1_week, last_2_week, last_3_week,
            last_1_month, last_2_month, last_3_month,
            last_1_year)
    cursor.execute(query, args)


def insert_values(sku, id, option_id, value):
    query = "INSERT INTO value_books(sku,id, option_id, value) " \
            "VALUES(%s,%s,%s,%s)"
    args = (sku, id, option_id, value)
    cursor.execute(query, args)


def insert_author(id, name):
    query = "INSERT INTO authors(id, name) " \
            "VALUES(%s,%s)"
    args = (id, name)
    cursor.execute(query, args)


def insert_book_authors(sku, author_id):
    query = "INSERT INTO book_authors(sku, author_id) " \
            "VALUES(%s,%s)"
    args = (sku, author_id)
    cursor.execute(query, args)


def write(p):
    insert_books(p["sku"], p["name"], p["description"], p["rating"], p["quantity_in_stock"], p["import_price"],
                 p["final_price"], p["discount"], p["discount_percent"], p["promotion_price"], p["publisher"],
                 p["number_of_pages"])
    for att in p["attributes"]:
        insert_attributes(p["sku"], att["id"], att["type"], att["name"], att["id"])
        for v in att["values"]:
            insert_values(p["sku"], att["id"], v["option_id"], v["value"])
    for cat in p["categories"]:
        insert_category(p["sku"], cat["id"], cat["type"], cat["name"], cat['parent_id'], cat['level'])
    for chan in p["channels"]:
        insert_channels(p["sku"], chan["id"], chan["type"], chan["name"])
    quan = p["quantity"]
    insert_quantity(p["sku"], quan["last_1_week"], quan["last_2_week"], quan["last_3_week"],
                    quan["last_1_month"], quan["last_2_month"], quan["last_3_month"],
                    quan["last_1_year"])
    insert_author(p["author"]["id"], p["author"]["name"])
    insert_book_authors(p["sku"], p["author"]["id"])


if __name__ == "__main__":
    faker = Faker()
    start = time.time()
    for bash in range(1):
        products = [faker.product() for i in range(1000)]
        for p in products:
            write(p)
        print("Insert completely {} products in {} seconds".format((bash + 1) * 1000, time.time() - start))
        conn.commit()
