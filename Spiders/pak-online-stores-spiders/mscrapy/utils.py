from urllib import urlencode
from urlparse import urlsplit, parse_qs, urlunsplit


def get_extracted(items_list, index=0):
    try:
        return items_list[index]
    except:
        return ""

def get_striped(items_list):
    try:
        return [item.strip() for item in items_list if item.strip()]
    except:
        return []

def add_query_parameters(url, key, value):
    scheme, netloc, path, query, fragment = urlsplit(url)
    query = parse_qs(query)
    query[key] = [value]
    query = urlencode(query, doseq=True)
    return urlunsplit((scheme, netloc, path, query, fragment))
