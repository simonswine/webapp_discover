#!/usr/bin/env python

import sys
import json
import webapp_discover
import datetime
import copy

# Load webapp_discover env
WEB_APP_DISC = webapp_discover.Explorer()

DISCOVERY_DATE=datetime.date(2014, 2, 4)


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
        age = float((DISCOVERY_DATE - release_date).days)/365.25

        # Add to dict
        if age not in webapps_per_age.keys():
            webapps_per_age[age] = 0

        # increment count
        webapps_per_age[age] += 1

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

# find matching verisons
def get_matching_version(ver,verions):

    if type(ver) == int:
        return [v for v in verions if v[0] == ver]
    elif type(ver) == tuple:
        ret_val = []
        for v in verions:
            for i in range(0,len(ver)):
                if v[i] != ver[i]:
                    break
            else:
                ret_val.append(v)
        return ret_val



# Get a version distribution for a specfic webapp
def get_colors_per_version(versions,name=None):

    versions = copy.deepcopy(versions)

    ret_val={}

    major_colors = ['black', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'purple', 'orange', 'gray']

    # Remove unknown versions
    if 'unknown' in versions:
        versions.remove('unknown')
        ret_val['unknown'] = 'black!20'

    versions_list = [map(int, i.split('.')) for i in versions]

    if name == 'Drupal':
        major_versions = set([ (i[0]) for i in versions_list])
    else:
        major_versions = set([ (i[0],i[1]) for i in versions_list])


    minor_start = 40.0
    minor_diff = 50.0

    count_major=0
    for v in major_versions:
        count_minor=0
        color = major_colors[count_major]
        sub_versions = get_matching_version(v,versions_list)
        for i in sub_versions:
            opacity=minor_start+(float(count_minor)*minor_diff/float(len(sub_versions)))

            ret_val[".".join(map(str,i))] = "%s!%d" % (color,opacity)

            count_minor +=1

        count_major += 1

    return ret_val


def get_app_distribution(webapps):

    count_per_app = {}

    for webapp in webapps:
        try:
            count_per_app[webapp['name']] += 1
        except KeyError:
            count_per_app[webapp['name']] = 1

    innen_kreis = 1.2
    aussen_kreis = 2.4
    abstand = 1

    ret_val =(
        "\\definecolor{lmugreen}{cmyk}{1,0,0.95,0.25}\n"
        "\\begin{tikzpicture}\n"
    )

    summe=len(webapps)
    start = 0.0
    color_version = ['magenta','blue','red','lmugreen','orange','violet']

    for app in count_per_app:
        ende = start + ((360.0/float(summe)) * float(count_per_app[app]))
        # Kreis Sektor  \draw[fill=\farbe,draw=none] (0,0) -- (\anfang:2cm) arc (\anfang:\ende:2cm);
        ret_val += "    \\draw[fill=%(color)s,draw=none] (0,0) -- (%(start)f:%(radius)fcm) arc (%(start)f:%(ende)f:%(radius)fcm);\n" % {
            'start' : start+abstand,
            'ende' : ende-abstand,
            'radius' : aussen_kreis,
            'color' : color_version.pop(),
        }

        winkel_label_pos = (ende+start)/2.0
        anchor_label="tip"

        if winkel_label_pos >= 337.5 and winkel_label_pos < 22.5:
            anchor_label='west'
        elif winkel_label_pos >= 22.5 and winkel_label_pos < 67.6:
            anchor_label='north west'
        elif winkel_label_pos >= 67.5 and winkel_label_pos < 112.5:
            anchor_label='north'
        elif winkel_label_pos >= 112.5 and winkel_label_pos < 157.5:
            anchor_label='north east'
        elif winkel_label_pos >= 157.5 and winkel_label_pos < 202.5:
            anchor_label='east'
        elif winkel_label_pos >= 202.5 and winkel_label_pos < 247.5:
            anchor_label='south east'
        elif winkel_label_pos >= 247.5 and winkel_label_pos < 292.5:
            anchor_label='south'
        elif winkel_label_pos >= 292.5 and winkel_label_pos < 337.5:
            anchor_label='south west'

        # Beschriftung
        ret_val += "    \\node[anchor=%(anchor)s] at (%(winkel)f:%(radius)fcm) {\\footnotesize\\emph{%(version)s} (%(count)d)};\n" % {
            'winkel' : winkel_label_pos,
            'radius' : aussen_kreis+0.5,
            'version' : app,
            'count' : count_per_app[app],
            'anchor': anchor_label,
        }


        start = ende


    ret_val +=(
        "    \\draw[fill=white,draw=none] (0,0) circle (%fcm);\n"
        "\\end{tikzpicture}\n"
    ) % innen_kreis

    return ret_val


def get_version_distribution(webapps,name):

    webapps_per_version = {}

    # loop over all webapps
    for webapp in webapps:

        # check name of webapp
        if webapp['name'] != name:
            continue

        # unknown versions:
        if webapp['version'] == None:
            webapp['version'] = 'unknown'

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
        version_list.sort(key=lambda s: map(int, s.split('.')), reverse=True)
    except ValueError:
        version_list.remove('unknown')
        version_list.sort(key=lambda s: map(int, s.split('.')), reverse=True)
        version_list.append('unknown')


    innen_kreis = 1.2
    aussen_kreis = 2.4
    abstand = 1

    ret_val =(
        "\\begin{tikzpicture}\n"
    )

    summe=sum([webapps_per_version[i]['count'] for i in version_list])
    start = 0.0
    color_version = get_colors_per_version(version_list,name=name)

    for version in version_list:
        ende = start + ((360.0/float(summe)) * float(webapps_per_version[version]['count']))
        # Kreis Sektor  \draw[fill=\farbe,draw=none] (0,0) -- (\anfang:2cm) arc (\anfang:\ende:2cm);
        ret_val += "    \\draw[fill=%(color)s,draw=none] (0,0) -- (%(start)f:%(radius)fcm) arc (%(start)f:%(ende)f:%(radius)fcm);\n" % {
            'start' : start+abstand,
            'ende' : ende-abstand,
            'radius' : aussen_kreis,
            'color' : color_version[version],
        }

        winkel_label_pos = (ende+start)/2.0
        if winkel_label_pos <=90 or winkel_label_pos >270:
            winkel_label_font = winkel_label_pos
        else:
            winkel_label_font = (winkel_label_pos+180 % 360)

        # Beschriftung
        ret_val += "    \\node[rotate=%(winkel_schrift)f] at (%(winkel)f:%(radius)fcm) {\\footnotesize\\texttt{%(version)s} (%(count)d)};\n" % {
            'winkel' : winkel_label_pos,
            'winkel_schrift' : winkel_label_font,
            'radius' : aussen_kreis+0.9,
            'version' : version,
            'count' : webapps_per_version[version]['count'],
        }


        start = ende


    ret_val +=(
        "    \\draw[fill=white,draw=none] (0,0) circle (%fcm);\n"
        "\\end{tikzpicture}\n"
    ) % innen_kreis

    return ret_val







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
        f=open('webapp_%s_version_distribution.tex' % webapp.lower(),'w')
        f.write(get_version_distribution(webapps,webapp))
        f.close()
        print webapp

    # Generate app distribution per app
    f=open('webapp_count_per_app.tex','w')
    f.write(get_app_distribution(webapps))
    f.close()



if __name__ == "__main__":
    main()