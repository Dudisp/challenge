import json
from http.server import BaseHTTPRequestHandler
from urllib import parse

PATH_COUNT_BY_EVENT_TYPE = "/events/countByEventType"
PATH_COUNT_WORDS = "/events/countWords"
STATISTICS_MANAGER = None


class Server:
    statistics_manager = None

    class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_path = parse.urlparse(self.path)
            data = "request unknown"
            response = 200

            if parsed_path.path == PATH_COUNT_BY_EVENT_TYPE:
                data = json.dumps(Server.statistics_manager.types_to_counter)
            elif parsed_path.path == PATH_COUNT_WORDS:
                data = json.dumps(Server.statistics_manager.data_words_to_counter)
            else:
                response = 400

            self.send_response(response)
            self.send_header('Content-Type',
                             'application/json')
            self.end_headers()
            self.wfile.write(data.encode('utf-8'))


def start_server(*args):
    Server.statistics_manager = args[0]
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), Server.GetHandler)
    print('Starting server')
    server.serve_forever()

