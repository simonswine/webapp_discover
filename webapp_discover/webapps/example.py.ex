from webapp_discover.php_webapp import PhpWebApp


class ExampleWebApp(PhpWebApp):
    webapp_name = "Example"

    # Get a file list that is typical for your application
    # You can use find_matching_files.py from the tools directory
    webapp_files = [

    ]

    # Release Versions
    versions = {
        '0.2': {'date': '2014-01-26'},
        '0.1': {'date': '2014-01-17'},
    }

    pass
