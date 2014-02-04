__author__ = 'christian'

import pyclbr
import os
import sys
import json

from webapp_discover.webapp import WebApp


class Explorer(object):

    webapps_directory = './webapps'


    @classmethod
    def walk_dirs(cls,path,level=None):

        if level > 0:
            next_level = level -1
        elif level <= 0:
            return []
        else:
            next_level = None


        ret_val = []

        try:
            for name in os.listdir(path):
                # build path
                npath = os.path.join(path, name)

                # am i a dir?
                if os.path.isdir(npath):
                    ret_val += Explorer.walk_dirs(npath,next_level)

            ret_val.append(path)
        except OSError:
            pass


        return ret_val


    def __init__(self):

        # Initialize webapp classes
        self.webapps = self.__init_webapps()

    def __init_webapps(self):

        # Webapp class store
        webapp_classes = []

        # Root dir of module
        root_dir = os.path.dirname(os.path.realpath(__file__))

        # Dir for webapp modules
        webapps_dir = os.path.abspath(
            os.path.join(
                root_dir,
                Explorer.webapps_directory,
            )
        )

        # Load webapps definition
        for f in os.listdir(os.path.abspath(webapps_dir)):

            # split extension
            module_name, ext = os.path.splitext(f)  # Handles no-extension files, etc.

            # only not hidden python files
            if ext == '.py' and not module_name.startswith("__"):  # Important, ignore .pyc/other files.
                #TODO LOG print('imported module: %s' % (module_name))
                module_classes = pyclbr.readmodule(
                    module_name,
                    path=[webapps_dir]
                )

                # loop through classes
                for module_class in module_classes.keys():
                    # check if class from module
                    if module_classes[module_class].module == module_name:

                        # Get module webapps
                        module_webapps = __import__('webapp_discover.webapps', fromlist=[module_name], level=0)

                        # Get module instance
                        module_instance = getattr(module_webapps, module_name)

                        # Get class instance
                        class_instance = getattr(module_instance, module_class)

                        # check if class is subclass of Webapp
                        if issubclass(class_instance, WebApp):
                            webapp_classes.append(class_instance())

        return webapp_classes

    def detect(self,path,level,ratio):

        for root in Explorer.walk_dirs(path,level):
            for webapp in self.webapps:
                val = webapp.webapp_filetree.check(root)
                if val >= ratio:
                    yield {
                        'path': root,
                        'name': webapp.webapp_name,
                        'version': webapp.get_version(root),
                        'plugins': webapp.get_plugins(root),
                        'score': val
                    }

    def get_webapp_per_name(self,name):
        for webapp in self.webapps:
            if webapp.webapp_name.lower() == name.lower():
                return webapp
        return None


    def run(self, path,level=5,ratio=0.8):

        ret_val={'webapps':[]}

        for result in self.detect(path,level=level,ratio=ratio):
            ret_val['webapps'].append(result)

        print (json.dumps(ret_val,indent=4))
