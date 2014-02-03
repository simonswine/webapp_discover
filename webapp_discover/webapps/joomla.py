from webapp_discover.php_webapp import PhpWebApp

import os
import re

RE_RELEASE = re.compile("""\$RELEASE\s*=\s*['"](\d+(\.\d+)*)['"]""")
RE_DEV_LEVEL = re.compile("""\$DEV_LEVEL\s*=\s*['"](\d+(\.\d+)*)['"]""")


class JoomlaWebApp(PhpWebApp):
    webapp_name = "Joomla"
    webapp_files = [
        'administrator/components/com_admin/index.html',
        'administrator/components/com_banners/banners.xml',
        'administrator/components/com_banners/index.html',
        'administrator/components/com_categories/index.html',
        'administrator/components/com_checkin/index.html',
        'administrator/components/com_config/index.html',
        'administrator/components/com_contact/contact.xml',
        'administrator/components/com_contact/index.html',
        'administrator/components/com_content/content.xml',
        'administrator/components/com_content/index.html',
        'administrator/components/com_installer/index.html',
        'administrator/components/com_languages/index.html',
        'administrator/components/com_login/index.html',
        'administrator/components/com_login/login.xml',
        'administrator/components/com_media/index.html',
        'administrator/components/com_media/media.xml',
        'administrator/components/com_menus/index.html',
        'administrator/components/com_messages/index.html',
        'administrator/components/com_modules/index.html',
        'administrator/components/com_newsfeeds/index.html',
        'administrator/components/com_newsfeeds/newsfeeds.xml',
        'administrator/components/com_search/index.html',
        'administrator/components/com_search/search.xml',
        'administrator/components/com_templates/index.html',
        'administrator/components/com_users/index.html',
        'administrator/components/com_users/users.xml',
        'administrator/components/com_weblinks/index.html',
        'administrator/components/com_weblinks/weblinks.xml',
        'administrator/components/index.html',
        'administrator/includes/index.html',
        'administrator/index.php',
        'administrator/modules/index.html',
        'administrator/templates/index.html',
        'cache/index.html',
        'components/com_banners/banners.php',
        'components/com_banners/index.html',
        'components/com_contact/contact.php',
        'components/com_contact/index.html',
        'components/com_content/content.php',
        'components/com_content/index.html',
        'components/com_newsfeeds/index.html',
        'components/com_newsfeeds/newsfeeds.php',
        'components/com_search/index.html',
        'components/com_search/search.php',
        'components/com_weblinks/index.html',
        'components/com_weblinks/weblinks.php',
        'components/com_wrapper/index.html',
        'components/com_wrapper/wrapper.php',
        'components/index.html',
        'htaccess.txt',
        'images/banners/index.html',
        'images/banners/osmbanner1.png',
        'images/banners/osmbanner2.png',
        'images/index.html',
        'images/joomla_logo_black.jpg',
        'images/powered_by.png',
        'includes/index.html',
        'index.php',
        'installation/index.php',
        'installation/sql/index.html',
        'language/index.html',
        'media/index.html',
        'modules/index.html',
        'templates/index.html'
    ] # Version 1.0.15, 2.5.17, 3.2.1

    # Source
    ## curl -s www.joomlaos.de/joomla-versions-history.html | perl -n -e'/(\d+\.\d+\.\d+)<\/td><td >(Security\/Bugfix|Stable)<\/td><td >(\d\d\d\d-\d\d-\d\d)/ && print ' \'$1\': { \'date\': \'$3\'},\n''

    versions = {
        '1.0.15': {'date': '2008-02-22'},
        '1.0.14': {'date': '2008-02-12'},
        '1.0.13': {'date': '2007-07-22'},
        '1.0.12': {'date': '2006-12-25'},
        '1.0.11': {'date': '2006-08-28'},
        '1.0.10': {'date': '2006-06-26'},
        '1.0.9': {'date': '2006-06-05'},
        '1.0.8': {'date': '2006-02-25'},
        '1.0.7': {'date': '2006-01-15'},
        '1.0.6': {'date': '2006-01-15'},
        '1.0.5': {'date': '2005-12-24'},
        '1.0.4': {'date': '2005-11-21'},
        '1.0.3': {'date': '2005-10-14'},
        '1.0.2': {'date': '2005-10-02'},
        '1.0.1': {'date': '2005-09-21'},
        '1.0.0': {'date': '2005-09-17'},
        '1.5.26': {'date': '2012-03-28'},
        '1.5.25': {'date': '2011-11-14'},
        '1.5.24': {'date': '2011-10-17'},
        '1.5.23': {'date': '2011-04-05'},
        '1.5.22': {'date': '2010-11-03'},
        '1.5.21': {'date': '2010-10-08'},
        '1.5.20': {'date': '2010-07-18'},
        '1.5.19': {'date': '2010-07-15'},
        '1.5.18': {'date': '2010-05-29'},
        '1.5.17': {'date': '2010-04-28'},
        '1.5.16': {'date': '2010-04-24'},
        '1.5.15': {'date': '2009-11-05'},
        '1.5.14': {'date': '2009-07-30'},
        '1.5.13': {'date': '2009-07-22'},
        '1.5.12': {'date': '2009-07-01'},
        '1.5.11': {'date': '2009-06-03'},
        '1.5.10': {'date': '2009-03-28'},
        '1.5.9': {'date': '2009-01-10'},
        '1.5.8': {'date': '2008-11-10'},
        '1.5.7': {'date': '2008-09-09'},
        '1.5.6': {'date': '2008-08-12'},
        '1.5.5': {'date': '2008-07-27'},
        '1.5.4': {'date': '2008-07-08'},
        '1.5.3': {'date': '2008-04-24'},
        '1.5.2': {'date': '2008-03-24'},
        '1.5.1': {'date': '2008-02-08'},
        '1.6.5': {'date': '2011-07-11'},
        '1.6.4': {'date': '2011-06-27'},
        '1.6.3': {'date': '2011-04-18'},
        '1.6.2': {'date': '2011-04-14'},
        '1.6.1': {'date': '2011-03-07'},
        '1.7.4': {'date': '2012-01-24'},
        '1.7.3': {'date': '2011-11-14'},
        '1.7.2': {'date': '2011-10-17'},
        '1.7.1': {'date': '2011-09-26'},
        '1.7.0': {'date': '2011-07-19'},
        '2.5.10': {'date': '2013-04-24'},
        '2.5.9': {'date': '2013-02-04'},
        '2.5.8': {'date': '2012-11-08'},
        '2.5.7': {'date': '2012-09-13'},
        '2.5.6': {'date': '2012-06-20'},
        '2.5.5': {'date': '2012-06-18'},
        '2.5.4': {'date': '2012-04-02'},
        '2.5.3': {'date': '2012-03-15'},
        '2.5.2': {'date': '2012-03-05'},
        '2.5.1': {'date': '2012-02-02'},
        '3.1.0': {'date': '2013-04-24'},
        '3.0.3': {'date': '2013-02-04'},
        '3.0.2': {'date': '2012-11-08'},
        '3.0.1': {'date': '2012-10-09'},
        '3.0.0': {'date': '2012-09-27'},
    }


    def get_version(self, path):
        # Joomla
        for conf in [
            'libraries/cms/version/version.php', # Joomla 1.5+
            'libraries/joomla/version.php', # Joomla 1.5
            'includes/version.php'                  # Joomla 1.0
        ]:
            conf_path = os.path.join(path, conf)
            if os.path.exists(conf_path):
                content = open(conf_path, 'r').read()
                m_release = RE_RELEASE.search(content)
                m_dev_level = RE_DEV_LEVEL.search(content)

                if m_release is not None and m_dev_level is not None:
                    return m_release.group(1) + '.' + m_dev_level.group(1)
