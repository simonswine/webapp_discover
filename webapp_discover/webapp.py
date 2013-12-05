__author__ = 'christian'

from webapp_discover.file_tree import FileTree

class WebApp(object):

    webapp_name = "Unknown"
    webapp_language = "Unknown"
    webapp_files = []

    def __init__(self):

        self.webapp_filetree = FileTree(self.webapp_files)


    def get_version(self,path):
        return None

    pass
