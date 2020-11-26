# coding=utf-8
import logging

from updater.repository.product import EsProductRepository
from updater.service import EsUpdaterInterface

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)


class EsUpdater(EsUpdaterInterface):
    def __init__(self):
        es_repository = EsProductRepository()
        super().__init__(es_repository)

    # def save_data(self, data, update_by_code=False, get_body_query_func=None):
    #     super().save_data(data, update_by_code, get_body_query_func)
