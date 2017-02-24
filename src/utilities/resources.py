from os.path import dirname, abspath, join
from os import pardir
from PyQt4 import uic


def resource(*args):
    """Get the path to a resource.

    :param args: List of path in the resources folder.
    :type args: str
    """
    path = abspath(join(dirname(__file__), pardir, 'resources'))

    for item in args:
        path = abspath(join(path, item))

    return path


def get_ui_class(*args):
    """Get UI Python class from .ui file.

    :param args: List of path in the UI folder.
    :type args: str
    """
    ui_file_path = abspath(join(dirname(__file__), pardir, 'ui'))

    for item in args:
        ui_file_path = abspath(join(ui_file_path, item))

    return uic.loadUiType(ui_file_path)[0]
