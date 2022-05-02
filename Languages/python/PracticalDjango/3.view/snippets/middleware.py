# from django.http import HttpRequest, HttpResponse
import timeit

from django.db import connections


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"{request.method} {request.path}")
        response = self.get_response(request)
        return response


class QueryCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.queries = []

    def _count_query(self):
        for c in connections.all():
            for q in c.queries:
                if q.get("sql"):
                    self.queries.append(q.get("sql"))

    def __call__(self, request):
        start_time = timeit.default_timer()
        response = self.get_response(request)
        elapsed = timeit.default_timer() - start_time
        self._count_query()
        print("Queries: ", f"{elapsed:0.4f}", self.queries)
        return response
