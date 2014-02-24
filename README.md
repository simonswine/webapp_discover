# Webapp_discover

## License

- GNU GPL v3.0  <http://www.gnu.org/licenses/gpl-3.0.txt>

## Testing @Travis

[![Build Status](https://travis-ci.org/simonswine/webapp_discover.png)](https://travis-ci.org/simonswine/webapp_discover)

## Help

```
usage: webapp_discover.py [-h] [--depth DEPTH] [--ratio RATIO] path

positional arguments:
  path                  specify path to scan

optional arguments:
  -h, --help            show this help message and exit
  --depth DEPTH, -d DEPTH
                        depth of directory recursion {1..inf}
  --ratio RATIO, -r RATIO
                        ratio for detection of a webapp {0..1}
```

## Example: Starting Scan in /var/www

 ```
$> ./webapp_discover.py /var/www
Running discovery in /var/www
{
    "webapps": [
        {
            "path": "/var/www/wordpress",
            "version": "3.7.1",
            "name": "Wordpress",
            "score": 0.98333333333333328,
            "plugins": [
                {
                    "version": "2.5.9",
                    "name": "akismet"
                }
            ]

        },
        {
            "path": "/var/www/joomla_alt",
            "version": "1.0.15",
            "name": "Joomla",
            "score": 0.96875,
            "plugins": null
        }

    ]
}
 ```