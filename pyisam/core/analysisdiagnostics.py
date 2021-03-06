"""
@copyright: IBM
"""

from .analysis.applicationlog import ApplicationLog


class AnalysisDiagnostics9020(object):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9020, self).__init__()
        self.application_log = ApplicationLog(base_url, username, password)


class AnalysisDiagnostics9021(AnalysisDiagnostics9020):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9021, self).__init__(base_url, username, password)


class AnalysisDiagnostics9030(AnalysisDiagnostics9021):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9030, self).__init__(base_url, username, password)


class AnalysisDiagnostics9040(AnalysisDiagnostics9030):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9040, self).__init__(base_url, username, password)


class AnalysisDiagnostics9050(AnalysisDiagnostics9040):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9050, self).__init__(base_url, username, password)


class AnalysisDiagnostics9060(AnalysisDiagnostics9050):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9060, self).__init__(base_url, username, password)


class AnalysisDiagnostics9070(AnalysisDiagnostics9060):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9070, self).__init__(base_url, username, password)


class AnalysisDiagnostics9071(AnalysisDiagnostics9070):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9071, self).__init__(base_url, username, password)


class AnalysisDiagnostics9080(AnalysisDiagnostics9071):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics9080, self).__init__(base_url, username, password)


class AnalysisDiagnostics10000(AnalysisDiagnostics9080):

    def __init__(self, base_url, username, password):
        super(AnalysisDiagnostics10000, self).__init__(base_url, username, password)
