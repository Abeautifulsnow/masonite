from app.http.providers.request import Request

class Route():

    def __init__(self, environ):
        self.url = environ['PATH_INFO']

    def get(self, route, output):
        if (self.url == route):
            return output
        return None

class Get():

    def __init__(self):
        pass

    def route(self, route, output):
        self.output = output
        self.route = route
        return self
        