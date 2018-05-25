"""
query search module
"""

#This is a dummy function which is returning the mocked response.
#It will be changed and make Elasticserach Api get requests to get real data

from pvh_digital.api.product.business import ProductNotFound


def search_product(conn, query):
    """
    queries elastic search and return search results
    :param conn: elasticsearch connection
    :param query: query keyword
    :param sort_by: sort by
    :param filter_by: filter_by
    :param page: page number
    :param offset: offset
    :param page_size: page size
    :return: search response
    :rtype: json
    """

    body = {
        "size": 30,
        "_source": ["id", "description", "price"],
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["division_name", "department_name", "description", "class_name", "id"]
            }
        }
    }

    total = conn.search(
        index='products', doc_type='products_type', body=body)['hits']['total']


    if total < 1:
        message = 'Sorry! We are unable to find the items you are searching for.' \
              'Please alter your search and try again.'
        raise ProductNotFound(message)

    data = conn.search(
        index='products', doc_type='products_type', body=body, filter_path=['hits.hits._source']
    )['hits']['hits']

    resp = []
    for each in data:
        each["_source"]["image"] = "http://via.placeholder.com/80x80"
        resp.append(each["_source"])
    return resp
