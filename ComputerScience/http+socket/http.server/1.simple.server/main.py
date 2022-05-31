from http import server

from settings import get_setting


class ServerHandler(server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(b"Hello World :^)")


def main():
    setting = get_setting("setting.yml")
    handler_class = (setting["bind"], setting["port"])
    serve = server.HTTPServer(handler_class, ServerHandler)
    serve.serve_forever()


if __name__ == "__main__":
    main()
