#from pyramid.config import Configurator
#
#
#def main(global_config, **settings):
#    """ This function returns a Pyramid WSGI application.
#    """
#    config = Configurator(settings=settings)
#    config.include('pyramid_jinja2')
#    config.include('pyramid_chameleon')
#    config.add_static_view('static', 'static', cache_max_age=3600)
#    config.add_route('home', '/')
#    config.scan()
#    return config.make_wsgi_app()
#

import os

from pyramid.config import Configurator

from wi2py.models import Directory
from wi2py.models import Filesystem

def main(global_config, **settings):
    root = settings.pop('root', None)
    if root is None:
        raise ValueError('wi2py requires a root')
    fs = Filesystem(os.path.abspath(os.path.normpath(root)))
    def get_root(environ):
        return Directory(fs, root)
    config = Configurator(root_factory=get_root, settings=settings)
    config.scan()
    return config.make_wsgi_app()

