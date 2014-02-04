__author__ = 'Christian Simon'


from webapp_discover.file_tree import FileTree
from datetime import date

class WebApp(object):

    webapp_name = "Unknown"
    webapp_language = "Unknown"
    webapp_files = []
    versions = {}

    def __init__(self):

        self.webapp_filetree = FileTree(self.webapp_files)


    def get_version(self,path):
        return None

    def get_plugins(self, path):
        return None

    def get_release(self, version):
        for vers in self.versions.keys():
            if vers == version:
                date_split = self.versions[vers]['date'].split('-')
                return date(int(date_split[0]),int(date_split[1]),int(date_split[2]))
        else:
            return None


    pass
