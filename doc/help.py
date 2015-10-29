# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from os.path import dirname, abspath, join

PATH = dirname(abspath(__file__))

from GeoHealth.core.tools import trans


def html_table(title, intro, inputs, outputs, more):
    html_string = u'' \
                  u'<html>' \
                  u'<head>' \
                  u'<style type="text/css">' \
                  u'body {' \
                  u'font-family: Ubuntu,Verdana,Arial,helvetica;' \
                  u'margin:0px;' \
                  u'padding:0px;' \
                  u'background-color:#B7B7B7;' \
                  u'}' \
                  u'table {' \
                  u'padding: 0;' \
                  u'width:100%%;' \
                  u'}' \
                  u'tr:nth-child(even) {' \
                  u'background-color:#DBDBDB;' \
                  u'}' \
                  u'tr:nth-child(odd) {' \
                  u'background-color:#CACACA;' \
                  u'}' \
                  u'caption {' \
                  u'background-color:#129300;' \
                  u'font-size:20;' \
                  u'color:#FFFFDC;' \
                  u'font-style:bold;' \
                  u'padding:5px;' \
                  u'}' \
                  u'.more{' \
                  u'list-style-type: none;' \
                  u'}' \
                  u'</style>' \
                  u'</head>' \
                  u'<body><table>' \
                  u'<caption>%s</caption>' \
                  u'<tr>' \
                  u'<td>%s</td>' \
                  u'</tr>' \
                  u'<tr>' \
                  u'<td>' \
                  u'<strong>Input</strong>' \
                  u'<ul>' % (title, intro)

    for item in inputs:
        html_string += u'<li>%s</li>' % item

    html_string += u'' \
                   u'</ul>' \
                   u'</td>' \
                   u'</tr>' \
                   u'<tr>' \
                   u'<td>' \
                   u'<strong>Output</strong>' \
                   u'<ul>'

    for item in outputs:
        html_string += u'<li>%s</li>' % item

    html_string += u'' \
                   u'</ul></td>'\
                   u'</tr>' \
                   u'<tr>' \
                   u'<td>' \
                   u'<strong>More</strong>' \
                   u'<ul>'

    for item in more:
        html_string += u'<li class="more">%s</li>' % item

    html_string += u'' \
                   u'</ul>' \
                   u'</td>' \
                   u'</tr>' \
                   u'</table>' \
                   u'</body>' \
                   u'</html>'

    return html_string


def picture(filename):
    return "<img src='file:%s' />" % (join(PATH, filename))


def help_blur():
    title = trans('Blurring')
    intro = trans('Vous pouvez flouter lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip')
    inputs = [trans('Point layer'), trans('Radius')]
    outputs = [trans('Blurred layer (polygon)')]
    more = [
        picture('blurring_1.png'),
        picture('blurring_2.png'),
        picture('blurring_3.png'),
        picture('blurring_4.png'),
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_incidence():
    title = trans('Incidence')
    intro = trans('You can create an incidence map about a disease.')
    inputs = [trans('Point layer : disease'), trans('Polygon layer : administrative boundary')]
    outputs = [trans('New polygon layer with the incidence')]
    more = [trans('This algorithm will count the number of points inside each polygons and run a formula to get the incidence.')]
    html = html_table(title, intro, inputs, outputs, more)
    return html
