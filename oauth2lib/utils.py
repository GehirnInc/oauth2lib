import string
from urllib.parse import (
    parse_qsl,
    urlencode,
    urlparse,
    urlunparse,
)
from random import SystemRandom

UNICODE_ASCII_CHARACTERS = (string.ascii_letters + string.digits)


def random_ascii_string(length):
    random = SystemRandom()
    return ''.join([
        random.choice(UNICODE_ASCII_CHARACTERS) for x in range(length)
    ])


def url_query_params(url):
    """Return query parameters as a dict from the specified URL.

    :param url: URL.
    :type url: str
    :rtype: dict
    """
    return dict(parse_qsl(urlparse(url).query, True))


def url_dequery(url):
    """Return a URL with the query component removed.

    :param url: URL to dequery.
    :type url: str
    :rtype: str
    """
    url = urlparse(url)
    return urlunparse(url[:4] + ('', url[5]))


def build_url(base, additional_params=None):
    """Construct a URL based off of base containing all parameters in
    the query portion of base plus any additional parameters.

    :param base: Base URL
    :type base: str
    ::param additional_params: Additional query parameters to include.
    :type additional_params: dict
    :rtype: str
    """
    url = urlparse(base)
    query_params = {}
    query_params.update(parse_qsl(url.query, True))
    if additional_params is not None:
        query_params.update(additional_params)
        for k, v in additional_params.items():
            if v is None:
                query_params.pop(k)

    return urlunparse(url[:4] + (urlencode(query_params), url[5]))
