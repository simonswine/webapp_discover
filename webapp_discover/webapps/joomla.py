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

    def get_version(self,path):
        # Joomla
        for conf in [
            'libraries/cms/version/version.php',    # Joomla 1.5+
            'libraries/joomla/version.php',         # Joomla 1.5
            'includes/version.php'                  # Joomla 1.0
        ]:
            conf_path = os.path.join(path,conf)
            if os.path.exists(conf_path):
                content = open(conf_path,'r').read()
                m_release = RE_RELEASE.search(content)
                m_dev_level = RE_DEV_LEVEL.search(content)

                if m_release is not None and m_dev_level is not None:
                    return m_release.group(1) + '.' + m_dev_level.group(1)
