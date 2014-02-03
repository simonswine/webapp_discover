from webapp_discover.php_webapp import PhpWebApp

class ExampleWebApp(PhpWebApp):
    webapp_name = "Example"
    webapp_files = [
        # Get a file list that is typical for your application
        # You can use find_matching_files.py from the tools directory
    ]

    pass
