# coding=utf-8
import logging

from updater.models.products import settings, mappings, synonyms_default
from updater.repository import EsRepositoryInterface

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)


class EsProductRepository(EsRepositoryInterface):
    def __init__(self):
        super().__init__()
        self._index = 'products'
        self.id_key = 'sku'
        self.settings = settings
        self.mappings = mappings

    def create_index_if_not_exist(self, synonyms=synonyms_default):
        """
        :param synonyms: mang synonyms khoi tao cung index, analyzer: synonym_analyzer
        :return:
        """
        super().create_index_if_not_exist()
        self.update_synonyms(synonyms)

    def update_synonyms(self, synonyms=synonyms_default):

        self.es.indices.close(self._index)
        self.es.indices.put_settings(body={
            "index": {
                "analysis": {
                    "filter": {
                        "synonym_filter": {
                            "type": "synonym",
                            "synonyms": synonyms
                        }
                    },
                    "analyzer": {
                        "synonym_analyzer": {
                            "filter": [
                                "lowercase",
                                "synonym_filter"
                            ],
                            "tokenizer": "standard"
                        }
                    }
                }
            }
        }, index=self._index)
        self.es.indices.open(self._index)
