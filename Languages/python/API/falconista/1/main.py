from wsgiref.simple_server import make_server

import falcon


class ThingsResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = (
            "\nTwo things awe me most, the starry sky "
            "above me and the moral law within me.\n"
            "\n"
            "    ~ Immanuel Kant\n\n"
        )


app = falcon.App()

things = ThingsResource()


app.add_route("/things", things)


def main():
    PORT = 8888
    with make_server("", PORT, app) as httpd:
        print(f"Serving on port {PORT} ...")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
