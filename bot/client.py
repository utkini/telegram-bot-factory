import json

import requests as r
from requests.adapters import HTTPAdapter, Retry
from bot_logging import LOG


class BaseClient:
    def __init__(self, login, password, base_url):
        self.login = login
        self.password = password
        self.base_url = base_url
        self._init_session()

    def _init_session(self, retries=5, backoff_factor=0.4, status_forcelist=(429, 500, 502, 504)) -> None:
        """
        initialize session with retries

        with this retry we can increase sleep between failed requests
        sleep = {backoff factor} * (2 ^ ({number of total retries} - 1))
        for default parameters sleep1 = 0, sleep2 = 0.6, sleep3 = 1.2
        """
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session = r.Session()
        self.session.auth = (self.login, self.password)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def get(self, url, **url_params) -> r.Response:
        """ GET request

        :param url: full url
        :param url_params: params for GET not supported
        :return: request.Response object
        """
        LOG.info(f'GET request on {url}')
        response = self.session.request(method='GET', url=url)
        LOG.info(f'finished with {response}')

        return response

    def post(self, url, body=None, file=None) -> r.Response:
        """ POST request

        :param url: full url
        :param body: request body
        :param file: file for sending
        :return: requests.Response object
        """
        files_data = {}
        if file is not None:
            files_data['file'] = file
        if body is not None:
            files_data['data'] = json.dumps(body)
        LOG.info(f'POST request on {url}, with files data {files_data}')
        response = self.session.request(method='POST', url=url, files=files_data)
        LOG.info(f'finished with {response}')

        return response
