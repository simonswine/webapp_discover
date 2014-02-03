__author__ = 'christian'

import os
import re

from webapp_discover.php_webapp import PhpWebApp

RE_VERSION = re.compile("""\$wp_version\s*=\s*['"](\d+(\.\d+)+)['"]""")

RE_PLUGIN_VERSION = re.compile("""Version:\s+(\d+(\.\d+)+)""")


class WordpressWebApp(PhpWebApp):
    webapp_name = "Wordpress"
    webapp_files = [
        './index.php',
        './license.txt',
        './readme.html',
        './wp-admin/admin-footer.php',
        './wp-admin/admin-functions.php',
        './wp-admin/admin-header.php',
        './wp-admin/admin.php',
        './wp-admin/edit-comments.php',
        './wp-admin/edit-form-advanced.php',
        './wp-admin/edit-form-comment.php',
        './wp-admin/edit.php',
        './wp-admin/index.php',
        './wp-admin/install-helper.php',
        './wp-admin/install.php',
        './wp-admin/link-add.php',
        './wp-admin/link-manager.php',
        './wp-admin/link-parse-opml.php',
        './wp-admin/menu-header.php',
        './wp-admin/menu.php',
        './wp-admin/moderation.php',
        './wp-admin/options-discussion.php',
        './wp-admin/options-general.php',
        './wp-admin/options-head.php',
        './wp-admin/options-permalink.php',
        './wp-admin/options.php',
        './wp-admin/options-reading.php',
        './wp-admin/optiosns-writing.php',
        './wp-admin/plugin-editor.php',
        './wp-admin/plugins.php',
        './wp-admin/post.php',
        './wp-admin/profile.php',
        './wp-admin/setup-config.php',
        './wp-admin/theme-editor.php',
        './wp-admin/themes.php',
        './wp-admin/upgrade-functions.php',
        './wp-admin/upgrade.php',
        './wp-admin/upload.php',
        './wp-admin/user-edit.php',
        './wp-admin/users.php',
        './wp-blog-header.php',
        './wp-comments-post.php',
        './wp-config-sample.php',
        './wp-content/plugins/hello.php',
        './wp-includes/class-IXR.php',
        './wp-includes/class-pop3.php',
        './wp-includes/class-snoopy.php',
        './wp-includes/default-filters.php',
        './wp-includes/functions.php',
        './wp-includes/kses.php',
        './wp-includes/locale.php',
        './wp-includes/rss-functions.php',
        './wp-includes/vars.php',
        './wp-includes/version.php',
        './wp-includes/wp-db.php',
        './wp-links-opml.php',
        './wp-login.php',
        './wp-mail.php',
        './wp-settings.php',
        './wp-trackback.php',
        './xmlrpc.php',
    ]

    # Source
    #git log --tags --date-order --simplify-by-decoration --pretty="format:%ai %d" | perl -n -e'/(\d\d\d\d-\d\d-\d\d)[^\(]+\(([\.\d]+)(\)|,)/ && print " \"$2\": { \"date\": \"$1\"},\n"'

    versions = {
        '3.8.1': {'date': '2014-01-23'},
        '3.8': {'date': '2013-12-12'},
        '3.7.1': {'date': '2013-10-29'},
        '3.7': {'date': '2013-10-24'},
        '3.6.1': {'date': '2013-09-11'},
        '3.6': {'date': '2013-08-01'},
        '3.5.2': {'date': '2013-06-21'},
        '3.5.1': {'date': '2013-01-24'},
        '3.5': {'date': '2012-12-11'},
        '3.4.2': {'date': '2012-09-06'},
        '3.4.1': {'date': '2012-06-27'},
        '3.3.3': {'date': '2012-06-27'},
        '3.4': {'date': '2012-06-13'},
        '3.3.2': {'date': '2012-04-20'},
        '3.3.1': {'date': '2012-01-03'},
        '3.3': {'date': '2011-12-12'},
        '3.2.1': {'date': '2011-07-12'},
        '3.2': {'date': '2011-07-04'},
        '3.1.4': {'date': '2011-06-29'},
        '3.1.3': {'date': '2011-05-25'},
        '3.1.2': {'date': '2011-04-26'},
        '3.0.6': {'date': '2011-04-26'},
        '3.1.1': {'date': '2011-04-04'},
        '3.1': {'date': '2011-02-23'},
        '3.0.5': {'date': '2011-02-07'},
        '3.0.4': {'date': '2010-12-29'},
        '3.0.3': {'date': '2010-12-08'},
        '3.0.2': {'date': '2010-12-08'},
        '3.0.1': {'date': '2010-07-29'},
        '3.0': {'date': '2010-06-17'},
        '2.9.2': {'date': '2010-02-15'},
        '2.9.1': {'date': '2010-01-05'},
        '2.9': {'date': '2009-12-18'},
        '2.8.6': {'date': '2009-11-12'},
        '2.8.5': {'date': '2009-10-20'},
        '2.8.4': {'date': '2009-08-12'},
        '2.8.3': {'date': '2009-08-03'},
        '2.8.2': {'date': '2009-07-20'},
        '2.8.1': {'date': '2009-07-09'},
        '2.8': {'date': '2009-06-11'},
        '2.7.1': {'date': '2009-02-10'},
        '2.7': {'date': '2008-12-10'},
        '2.6.5': {'date': '2008-11-25'},
        '2.6.3': {'date': '2008-10-23'},
        '2.6.2': {'date': '2008-09-08'},
        '2.6.1': {'date': '2008-08-15'},
        '2.6': {'date': '2008-07-15'},
        '2.5.1': {'date': '2008-04-25'},
        '2.5': {'date': '2008-03-29'},
        '2.3.3': {'date': '2008-02-05'},
        '2.3.2': {'date': '2007-12-29'},
        '2.3.1': {'date': '2007-10-26'},
        '2.3': {'date': '2007-10-06'},
        '2.2.3': {'date': '2007-09-07'},
        '2.0.11': {'date': '2007-08-05'},
        '2.2.2': {'date': '2007-08-05'},
        '2.2.1': {'date': '2007-06-21'},
        '2.2': {'date': '2007-05-15'},
        '2.1.3': {'date': '2007-04-03'},
        '2.0.10': {'date': '2007-04-03'},
        '2.1.2': {'date': '2007-03-03'},
        '2.1.1': {'date': '2007-02-20'},
        '2.0.9': {'date': '2007-02-20'},
        '2.0.8': {'date': '2007-02-05'},
        '2.1': {'date': '2007-01-23'},
        '2.0.7': {'date': '2007-01-15'},
        '2.0.6': {'date': '2007-01-06'},
        '2.0.5': {'date': '2006-10-27'},
        '2.0.4': {'date': '2006-07-29'},
        '2.0.3': {'date': '2006-06-02'},
        '2.0.2': {'date': '2006-06-02'},
        '2.0.1': {'date': '2006-02-01'},
        '2.0': {'date': '2005-12-26'},
        '1.5.2': {'date': '2005-08-20'},
        '1.5.1.3': {'date': '2005-07-02'},
        '1.5.1.2': {'date': '2005-06-07'},
        '1.5.1.1': {'date': '2005-05-20'},
        '1.5.1': {'date': '2005-05-10'},
        '1.5': {'date': '2005-04-18'}
    }


    def get_version(self, path):

        conf_path = os.path.join(path, 'wp-includes/version.php')
        if os.path.exists(conf_path):
            cont = open(conf_path).read()
            m = RE_VERSION.search(cont)
            if m is not None:
                return (m.group(1))

    def get_plugins(self, path):

        return self.get_installed_plugins(path)

    def get_plugin_info(self, plugin_file):

        content = open(plugin_file).readlines()

        version = None

        for line in content:
            m = RE_PLUGIN_VERSION.search(line)
            if m is not None:
                version = m.group(1)
                break

        return {
            'name': os.path.basename(plugin_file).replace('.php', ''),
            'version': version,
        }
        pass

    def get_installed_plugins(self, path):

        plugins = []

        plugins_path = os.path.join(path, 'wp-content/plugins/')

        if os.path.isdir(plugins_path):
            for plugin in os.listdir(plugins_path):

                if plugin in ['index.php']:
                    continue

                try:
                    plugin_path = os.path.join(path, plugins_path, plugin)

                    # Plugin dir
                    if os.path.isdir(plugin_path):
                        plugin_file = os.path.join(plugin_path, '%s.php' % plugin)
                        if os.path.exists(plugin_file):
                            plugins.append(self.get_plugin_info(plugin_file))

                    # Plugin file
                    if plugin.endswith('.php'):
                        plugin_file = plugin_path
                        if os.path.isfile(plugin_file):
                            plugins.append(self.get_plugin_info(plugin_file))
                except IOError:
                    pass

        return plugins