__author__ = 'christian'


from webapp_discover.webapp import WebApp
from webapp_discover import utils
import subprocess

class PhpWebApp(WebApp):
    webapp_language="PHP"

    # This method executes php code and returns the output
    def exec_php_code(self,code):

        php_path = utils.which('php')

        # Check if php executable exists
        if php_path == None:
            return None

        # Call php
        proc = subprocess.Popen([php_path], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # Send code
        proc.stdin.write(code)
        proc.stdin.close()
        # Receive output
        script_response = proc.stdout.read()

        # wait for php
        proc.wait()

        # check for returncode
        if proc.returncode == 0:
            return script_response
        else:
            return None


    # This method modfies php code input, with prepends and appends
    def php_change_code(self,code,prepend="",append=""):

        # Insert php code at the start
        code=code.replace("<?php","<?php\n%s\n" % prepend)

        # Add php code in the end
        code=code.replace("?>","%s\n?>" % append)

        return code
