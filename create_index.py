# coding=utf-8
import logging

from updater.repository.product import EsProductRepository

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    es = EsProductRepository()
    es.create_index_if_not_exist()
