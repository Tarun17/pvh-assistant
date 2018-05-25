"""
Settings and mappings for the Elasticsearch Index
"""

ES_HOST = 'https://search-pvh-es-z2ixprcdbukbt7rfrgzcrrzj6m.us-east-1.es.amazonaws.com/'

product_settings = {
        "settings": {
            "number_of_shards" : 1,
            "number_of_replicas": 0,
            "analysis": {
                "filter": {
                    "autocomplete_filter": {
                        "type":     "edge_ngram",
                        "min_gram": 2,
                        "max_gram": 15
                    }
                },
                "analyzer": {
                    "autocomplete": {
                        "type":      "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "lowercase",
                            "autocomplete_filter"
                        ]
                    }
                }
            }
        }
    }

product_mapping = {
        "dynamic": False,
        "properties": {
            "GTIN/EAN/UPC": {
                "type": "keyword"
            },
            "STYLE_DESCRIPTION": {
                "type": "text"
            },
            "DIVISION_CODE": {
                "type": "text"
            },
            "DIVISION_NAME": {
                "type": "text"
            },
            "DEPARTMENT_CODE": {
                "type": "keyword"
            },
            "DEPARTMENT_NAME": {
                "type": "keyword"
            },
            "CLASS_CODE": {
                "type": "keyword"
            },
            "CLASS_NAME": {
                "type": "keyword"
            },
            "VENDOR_CODE": {
                "type": "keyword"
            },
            "VENDOR_NAME": {
                "type": "text"
            },
            "STYLE_CODE": {
                "type": "keyword"
            },
            "COLOR_CODE": {
                "type": "keyword"
            },
            "COLOR_NAME": {
                "type": "keyword"
            },
            "SIZ_CODE": {
                "type": "keyword"
            },
            "SIZE_NAME": {
                "type": "keyword"
            }
        }
    }
