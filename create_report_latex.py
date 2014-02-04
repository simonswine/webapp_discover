#!/usr/bin/env python

import sys
import json
import pprint
import webapp_discover
import datetime

# Load webapp_discover env
WEB_APP_DISC = webapp_discover.Explorer()


# Loads webapps from json result files
def load_input(files):

    webapps=[]

    for path in sys.argv[1:]:
        webapps += json.load(open(path, 'r'))['webapps']

    return webapps

# Calculates dat file for the age of webapps
def get_age_of_webapps(webapps,sample_in_years=float(1.0/6.0)):

    webapps_per_age = {}

    # loop over all webapps
    for webapp in webapps:

        # get release date of webapp version
        release_date = WEB_APP_DISC\
            .get_webapp_per_name(webapp['name'])\
            .get_release(webapp['version'])

        # if i get no date next item
        if release_date == None:
            continue

        # calc diff in years
        age = float((datetime.date.today() - release_date).days)/365.25

        # Add to dict
        if age not in webapps_per_age.keys():
            webapps_per_age[age] = 0

        # increment count
        webapps_per_age[age] += 1

    #pprint.pprint(webapps_per_age)

    # Sample it in the right way
    age_keys=webapps_per_age.keys()
    age_keys.sort()

    value=0
    old=0.0
    values = []
    for age in age_keys:
        new=float(int(float(age)/sample_in_years)*sample_in_years)+float(sample_in_years/2)
        if new == old:
             value += webapps_per_age[age]
        else:
             values.append((old,value))
             old=new
             value=webapps_per_age[age]
    values.append((old,value))

    return "\n".join(
        ['#Webapps count per age in years'] +
        ["%f %d" % (i[0],i[1]) for i in values[1:]] +
        ['']
    )

# Get a version distribution for a specfic webapp
def get_version_distribution(webapps,name):

    webapps_per_version = {}

    # loop over all webapps
    for webapp in webapps:

        # check name of webapp
        if webapp['name'] != name:
            continue

        # new version add key
        if not webapps_per_version.has_key(webapp['version']):
            webapps_per_version[webapp['version']] = {
                 'count' :0,
                 'release_date' : WEB_APP_DISC.get_webapp_per_name(name).get_release(webapp['version'])
            }

        # count up
        webapps_per_version[webapp['version']]['count'] += 1

    # Sort list
    version_list = webapps_per_version.keys()
    try:
        version_list.sort(key=lambda s: map(int, s.split('.')))
    except AttributeError:
        version_list.remove(None)
        version_list.sort(key=lambda s: map(int, s.split('.')))
        version_list.append(None)


    return "\n".join(
        ["# Webapp %s version distribution" % name]+
        [ "%s %d" %(key,webapps_per_version[key]['count']) for key in version_list ]+
        ['']
    )







def main():
    # Storage for webapps
    webapps = load_input(sys.argv[1:])

    # Count Webapps per app
    webapps_per_app = {}
    webapps_per_age = {}

    # Generate age data files
    f=open('webapp_count_per_age.dat','w')
    f.write(get_age_of_webapps(webapps))
    f.close()

    # Generate verison distribution per app
    for webapp in [webapp.webapp_name for webapp in WEB_APP_DISC.webapps]:
        f=open('webapp_%s_version_distribution.dat' % webapp,'w')
        f.write(get_version_distribution(webapps,webapp))
        f.close()
        print webapp




if __name__ == "__main__":
    main()