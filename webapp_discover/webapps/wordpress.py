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

    def get_version(self, path):

        conf_path = os.path.join(path, 'wp-includes/version.php')
        if os.path.exists(conf_path):
            cont = open(conf_path).read()
            m = RE_VERSION.search(cont)
            if m is not None:
                return (m.group(1))

    def get_plugins(self, path):

        return self.get_installed_plugins(path)

    def get_plugin_info(self,plugin_file):

        content = open(plugin_file).readlines()

        version = None

        for line in content:
            m = RE_PLUGIN_VERSION.search(line)
            if m is not None:
                version = m.group(1)
                break


        return {
            'name' : os.path.basename(plugin_file).replace('.php',''),
            'version' : version,
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
                    plugin_path = os.path.join(path,plugins_path,plugin)

                    # Plugin dir
                    if os.path.isdir(plugin_path):
                        plugin_file = os.path.join(plugin_path,'%s.php' % plugin)
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