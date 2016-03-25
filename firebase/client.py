""" firebase HTTP client """

import json
import urllib

from firebase_token_generator import create_token

import httplib2


class Firebase(object):
    """ Firebase helper class to work with the Firebase REST API """
    token = None

    def __init__(self, firebase_url, timeout=30):
        """ initialize a firebase instance """
        self.base_url = firebase_url
        try:
            from google.appengine.api import memcache
        except ImportError:
            memcache = None
        self.http = httplib2.Http(memcache, timeout=timeout)

    def set_token(self, token):
        """ set the authentication token """
        self.token = token

    def authenticate(self, uid, secret, auth_payload={}):
        """ authenticate using custom auth """
        auth_payload = auth_payload if auth_payload is not None else {}
        auth_payload["uid"] = uid
        token = create_token(secret, auth_payload)
        self.set_token(token)

    def url(self, url=None, params={}):
        """ generate the url for a request """
        return '{}.json?{}'.format(
            '{}/{}'.format(self.base_url, url if url else '').rstrip('/'),
            urllib.urlencode(params if params else {}))

    def get(self, url=None, params={}):
        """ execute an HTTP REST GET """
        return self.method('GET', url=url, data=None, params=params)

    def put(self, url=None, data=None, params={}):
        """ execute an HTTP REST PUT """
        return self.method('PUT', url=url, data=data, params=params)

    def post(self, url=None, data=None, params={}):
        """ execute an HTTP REST POST """
        return self.method('POST', url=url, data=data, params=params)

    def delete(self, url=None, params={}):
        """ execute an HTTP REST DELETE """
        return self.method('DELETE', url=url, params=params)

    def method(self, method="GET", url=None, data=None, params={}):
        """ execute an HTTP REST call"""
        params = params if params is not None else {}
        if self.token is not None:
            params['auth'] = self.token
        resp, content = self.http.request(self.url(url, params), method, json.dumps(data) if data else None)
        return json.loads(content)
