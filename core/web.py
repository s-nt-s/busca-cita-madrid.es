import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

re_sp = re.compile(r"\s+")
re_emb = re.compile(r"^image/[^;]+;base64,.*", re.IGNORECASE)

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Expires": "Thu, 01 Jan 1970 00:00:00 GMT",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


def iterhref(soup):
    """Recorre los atriburos href o src de los tags"""
    for n in soup.findAll(["img", "form", "a", "iframe", "frame", "link", "script"]):
        attr = "href" if n.name in ("a", "link") else "src"
        if n.name == "form":
            attr = "action"
        val = n.attrs.get(attr)
        if val is None or re_emb.search(val):
            continue
        if not(val.startswith("#") or val.startswith("javascript:")):
            yield n, attr, val


def buildSoup(root, source, parser="lxml"):
    soup = BeautifulSoup(source, parser)
    for n, attr, val in iterhref(soup):
        val = urljoin(root, val)
        n.attrs[attr] = val
    return soup


class Web:
    def __init__(self, refer=None, verify=True):
        self.s = requests.Session()
        self.s.headers = default_headers
        self.response = None
        self.soup = None
        self.form = None
        self.refer = refer
        self.verify = verify

    def _get(self, url, allow_redirects=True, **kargv):
        if kargv:
            return self.s.post(url, data=kargv, allow_redirects=allow_redirects, verify=self.verify)
        return self.s.get(url, allow_redirects=allow_redirects, verify=self.verify)

    def get(self, url, **kargv):
        if self.refer:
            self.s.headers.update({'referer': self.refer})
        self.response = self._get(url, **kargv)
        self.refer = self.response.url
        self.soup = buildSoup(url, self.response.content)
        return self.soup

    def prepare_submit(self, slc, silent_in_fail=False, **kargv):
        data = {}
        self.form = self.soup.select_one(slc)
        if silent_in_fail and self.form is None:
            return None, None
        for i in self.form.select("input[name]"):
            name = i.attrs["name"]
            data[name] = i.attrs.get("value")
        for i in self.form.select("select[name]"):
            name = i.attrs["name"]
            slc = i.select_one("option[selected]")
            slc = slc.attrs.get("value") if slc else None
            data[name] = slc
        data = {**data, **kargv}
        action = self.form.attrs.get("action")
        action = action.rstrip() if action else None
        if action is None:
            action = self.response.url
        return action, data

    def submit(self, slc, silent_in_fail=False, **kargv):
        action, data = self.prepare_submit(
            slc, silent_in_fail=silent_in_fail, **kargv)
        if silent_in_fail and not action:
            return None
        return self.get(action, **data)

    def val(self, slc):
        n = self.soup.select_one(slc)
        if n is None:
            return None
        v = n.attrs.get("value", n.get_text())
        v = v.strip()
        return v if v else None

    @property
    def url(self):
        if self.response is None:
            return None
        return self.response.url

    def json(self, url, **kargv):
        r = self._get(url, **kargv)
        return r.json()

    def resolve(self, url, **kargv):
        if self.refer:
            self.s.headers.update({'referer': self.refer})
        r = self._get(url, allow_redirects=False, **kargv)
        if r.status_code in (302, 301):
            return r.headers['location']
