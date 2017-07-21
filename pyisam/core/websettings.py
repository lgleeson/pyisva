"""
@copyright: IBM
"""

from .web.dscadmin import DSCAdmin
from .web.policyadmin import PolicyAdmin
from .web.reverseproxy import ReverseProxy
from .web.runtimecomponent import RuntimeComponent


class WebSettings9020(object):

    def __init__(self, base_url, username, password, docker):
        super(WebSettings9020, self).__init__()
        self.dsc_admin = DSCAdmin(base_url, username, password)
        self.policy_administration = PolicyAdmin(base_url, username, password)
        self.reverse_proxy = ReverseProxy(base_url, username, password)
        self.runtime_component = RuntimeComponent(base_url, username, password)


class WebSettings9021(WebSettings9020):

    def __init__(self, base_url, username, password, docker):
        super(WebSettings9021, self).__init__(base_url, username, password, docker)


class WebSettings9030(WebSettings9021):

    def __init__(self, base_url, username, password, docker):
        super(WebSettings9030, self).__init__(base_url, username, password, docker)


class WebSettings9040(WebSettings9030):

    def __init__(self, base_url, username, password, docker):
        super(WebSettings9040, self).__init__(base_url, username, password, docker)
