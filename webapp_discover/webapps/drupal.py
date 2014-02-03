from webapp_discover.php_webapp import PhpWebApp
import re
import os

RE_VERSION = re.compile("""["']VERSION["']\s*,\s*['"](\d+(\.\d+)+)['"]""")
RE_VERSION_CHANGELOG = re.compile("""drupal\s+(\d+(\.\d+)+),""")


class DrupalWebApp(PhpWebApp):
    webapp_name = "Drupal"
    webapp_files = [
        '.htaccess',
        'cron.php',
        'includes/common.inc',
        'includes/module.inc',
        'includes/theme.inc',
        'includes/xmlrpc.inc',
        'includes/xmlrpcs.inc',
        'index.php',
        'misc/druplicon.png',
        'scripts/code-clean.sh',
        'scripts/cron-lynx.sh',
        'update.php',
        'xmlrpc.php'
    ] # Versions 4.0 and 7.2

    def get_version(self,path):

        # Versions >= 6.0
        for conf in [
            'includes/bootstrap.inc',
            'modules/system/system.module',
            ]:
            conf_path = os.path.join(path,conf)
            if os.path.exists(conf_path):
                cont = open(conf_path).read()
                m = RE_VERSION.search(cont)
                if m is not None:
                    return (m.group(1))

        # Older Versions from changelog
        conf_path = os.path.join(path,'CHANGELOG')
        if os.path.exists(conf_path):
            cont = open(conf_path).read()
            m = RE_VERSION_CHANGELOG.search(cont)
            if m is not None:
                return (m.group(1))

