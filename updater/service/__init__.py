# coding=utf-8
import logging
from typing import List

import elasticsearch

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)


class EsUpdaterInterface:
    def __init__(self, es_repository=None):
        self.es_repository = es_repository

    def save_data(self, data, update_by_code=False, get_body_query_func=None):
        try:
            if isinstance(data, list):
                self._save_all_data(data, update_by_code, get_body_query_func)
            else:
                self._save_data(data, update_by_code, get_body_query_func)
        except Exception as e:
            _logger.error(e)
            raise e

    def _save_data(self, data: dict, update_by_code=False, get_body_query_func=None):
        if update_by_code:
            self.es_repository.save(data, get_body_query_func=get_body_query_func)
        else:
            self.es_repository.save(data)

    def _save_all_data(self, list_data: List[dict], update_by_code=False, get_body_query_func=None):
        if update_by_code:
            self.es_repository.save_all(list_data, get_body_query_func=get_body_query_func)
        else:
            self.es_repository.save_all(list_data)
