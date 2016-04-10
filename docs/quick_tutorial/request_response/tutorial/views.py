from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


class TutorialViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return HTTPFound(location='/plain')

    @view_config(route_name='plain')
    def plain(self):
        name = self.request.params.get('name', 'No Name Provided')

        body = 'URL {0!s} with name: {1!s}'.format(self.request.url, name)
        return Response(
            content_type='text/plain',
            body=body
        )
