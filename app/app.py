import requests
import re


def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    url = formaturl(hostname)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return False
    else:
        return 100 <= response.status_code < 400


def formaturl(url):
    return url if re.match('(?:http|ftp|https)://', url) else 'http://{}'.format(url)


