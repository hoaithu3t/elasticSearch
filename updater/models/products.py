# coding=utf-8
import logging

__author__ = 'LongHB'
_logger = logging.getLogger(__name__)

product_details = {
    "attributes": {
        "type": "nested",
        "dynamic": "strict",
        "properties": {
            "id": {
                "type": "integer",
                "index": False
            },
            "type": {
                "type": "keyword"
            },
            "name": {
                "type": "keyword",
                "index": False
            },
            "values": {
                "type": "nested",
                "dynamic": "strict",
                "properties": {
                    "option_id": {
                        "type": "integer",
                        "index": False,
                    },
                    "value": {
                        "type": "text",
                    }
                }
            },
        }
    },
    "categories": {
        "type": "nested",
        "dynamic": "strict",
        "properties": {
            "id": {
                "type": "integer",
                "index": False
            },
            "type": {
                "type": "keyword"
            },
            "name": {
                "type": "keyword",
                "index": False,
                "fields": {
                    "searchable": {
                        "type": "text",
                        "analyzer": "synonym_analyzer"
                    }
                }
            },
            "parent_id": {
                "type": "integer",
                "index": False
            },
            "level": {
                "type": "integer",
                "index": False
            }
        }
    },
    "description": {
        "type": "text",
        "index": False
    },
    "rating": {
        "type": "double",
        "index": False
    },
    "name": {
        "type": "text",
        "analyzer": "synonym_analyzer"
    },
    "author": {
        "type": "nested",
        "dynamic": "strict",
        "properties": {
            "id": {
                "type": "text",
                "index": True,
            },
            "name": {
                "type": "text",
                "index": False
            }
        }
    },
    "number_of_pages": {
        "type": "integer",
        "index": False
    },
    "publisher": {
        "type": "text",
        "index": False
    },
}

business_details = {
    "quantity_in_stock": {
        "type": "integer"
    },
    "channels": {
        "type": "nested",
        "dynamic": "strict",
        "properties": {
            "id": {
                "type": "integer"
            },
            "type": {
                "type": "keyword"
            },
            "name": {
                "type": "keyword",
                "index": False
            }
        }
    },
    "quantity": {
        "dynamic": "strict",
        "properties": {
            "last_1_week": {
                "type": "integer"
            },
            "last_2_week": {
                "type": "integer"
            },
            "last_3_week": {
                "type": "integer"
            },
            "last_1_month": {
                "type": "integer"
            },
            "last_2_month": {
                "type": "integer"
            },
            "last_3_month": {
                "type": "integer"
            },
            "last_1_year": {
                "type": "integer"
            }

        }
    }
}

price_details = {
    "import_price": {
        "type": "double"
    },
    "final_price": {
        "type": "double"
    },
    "promotion_price": {
        "type": "double"
    },
    "discount": {
        "type": "double"
    },
    "discount_percent": {
        "type": "double"
    }
}

mappings = {
    "dynamic": "strict",
    "properties": {
        "sku": {
            "type": "text",
            "fields": {
                "raw": {
                    "type": "keyword"
                }
            }
        },
        **product_details,
        **business_details,
        **price_details
    }
}

settings = {
    "index": {
        "max_result_window": 500000,
        "number_of_shards": "1",
        "analysis": {
            "filter": {
                "synonym_filter": {
                    "type": "synonym",
                    "synonyms": []
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
}

synonyms_default = [
    "Sách => sach"
]
