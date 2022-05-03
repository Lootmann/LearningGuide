from django.http import HttpRequest, HttpResponse


_form_html = """
<html>
<head>
</head>

<body>
<div>
  <a href="/">Pages:Index</a>
</div>

<form method="get">
  <input type="text" name="q" placeholder="Search" value="">
  <button type="submit">Go</button>
</form>
</body>
</html>
"""


def xss_view(request: HttpRequest):
    if "q" in request.GET:
        return HttpResponse(f"Searched for : {request.GET['q']}")
    else:
        return HttpResponse(_form_html)
