# coding=utf-8
import datetime
import logging
import time

from updater.faker.products import Faker
from updater.repository.product import EsProductRepository

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    faker = Faker()
    es = EsProductRepository()
    es.create_index_if_not_exist()
    start = time.time()
    for bash in range(10):
        products = [faker.product() for i in range(10)]
        es.save_all(products, chunk_size=10000)
        print("Insert completely {} products in {} seconds".format((bash + 1) * 1000, time.time() - start))
