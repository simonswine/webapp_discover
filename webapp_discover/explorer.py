# -*- coding: utf-8 -*
__author__ = 'christian'

import pyclbr
import os
import json

from webapp_discover.webapp import WebApp


class Explorer(object):
    webapps_directory = './webapps'

    @classmethod
    def walk_dirs(cls, path, level=None):

        if level > 0:
            next_level = level - 1
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
                    ret_val += Explorer.walk_dirs(npath, next_level)

            ret_val.append(path)
        except OSError:
            pass

        return ret_val

    def __init__(self):

        # Initialize webapp classes
        self.webapps = self.__init_webapps()

    # Lade Definitionen von Webapps
    def __init_webapps(self):

        # Return value
        webapp_classes = []

        # Root dir of module
        root_dir = os.path.dirname(os.path.realpath(__file__))

        # Verzeichnis für Module
        webapps_dir = os.path.abspath(
            os.path.join(
                root_dir,
                Explorer.webapps_directory,
            )
        )

        # Lese Definitionen für Webapp-Module
        for f in os.listdir(os.path.abspath(webapps_dir)):

            # Trenne in Name und Erweiterung
            module_name, ext = os.path.splitext(f)

            # Nur *.py Dateien als Module lesen
            if ext == '.py' and not module_name.startswith("__"):
                # Lese Modul
                module_classes = pyclbr.readmodule(
                    module_name,
                    path=[webapps_dir]
                )

                # Schleife über Klassen
                for module_class in module_classes.keys():
                    # Prüfe ob Klasse vom entsprechende Modul ist
                    if module_classes[module_class].module == module_name:

                        # Lade Modul
                        module_webapps = __import__(
                            'webapp_discover.webapps',
                            fromlist=[module_name],
                            level=0
                        )

                        # Hole Modul-Instanz
                        module_instance = getattr(module_webapps, module_name)

                        # Hole Klassen-Instanz
                        class_instance = getattr(module_instance, module_class)

                        # Prüfe ob die jeweilige Klasse Unterklasse von
                        # Webapp ist
                        if issubclass(class_instance, WebApp):
                            webapp_classes.append(class_instance())

        return webapp_classes

    # Durchsuche Pfad  path bis zur Tiefe level mit dem Schwellwert ratio
    def detect(self, path, level, ratio):

        # Schleife über Verzeichnisse
        for root in Explorer.walk_dirs(path, level):
            for webapp in self.webapps:
                # Schleife über Webanwendungen
                val = webapp.webapp_filetree.check(root)

                # Nur wenn Schwellwert überschritten
                if val >= ratio:
                    yield {
                        'path': root,
                        'name': webapp.webapp_name,
                        # Bestimme Version
                        'version': webapp.get_version(root),
                        # Finde Plugins der Webapp
                        'plugins': webapp.get_plugins(root),
                        'score': val
                    }

    def get_webapp_per_name(self, name):
        for webapp in self.webapps:
            if webapp.webapp_name.lower() == name.lower():
                return webapp
        return None

    def run(self, path, level=5, ratio=0.8):

        ret_val = {'webapps': []}

        for result in self.detect(path, level=level, ratio=ratio):
            ret_val['webapps'].append(result)

        print(json.dumps(ret_val, indent=4))
