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
from geohealth.core.tools import tr


PATH = dirname(abspath(__file__))


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

    if len(more) > 0:
        html_string += u'<tr>' \
                       u'<td>' \
                       u'<strong>More</strong>' \
                       u'<ul>'

        for item in more:
            html_string += u'<li class="more">%s</li>' % item

        html_string += u'</ul>' \
                       u'</td>' \
                       u'</tr>' \

    html_string += u'</table>' \
                   u'</body>' \
                   u'</html>'

    return html_string


def picture(filename):
    return "<img src='file:%s' />" % (join(PATH, filename))


def help_open_shapefile():
    title = tr('Import shapefile')
    intro = tr('Import a shapefile into QGIS.')
    inputs = [
        tr('Shapefile')
    ]
    outputs = [
        tr('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_raster():
    title = tr('Import raster')
    intro = tr('Import a raster into QGIS.')
    inputs = [
        tr('Raster file')
    ]
    outputs = [
        tr('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_table():
    title = tr('Import table')
    intro = tr('XLS or DBF format.')
    inputs = [
        tr('Table file')
    ]
    outputs = [
        tr('New table')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_csv():
    title = tr('Import CSV table')
    intro = tr('CSV format without geometry.')
    inputs = [
        tr('CSV file')
    ]
    outputs = [
        tr('New table')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_xy():
    title = tr('Import CSV table')
    intro = tr('CSV format with geometry.')
    inputs = [
        tr('CSV file')
    ]
    outputs = [
        tr('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_density():
    title = tr('Density')
    intro = tr('Compute density')
    inputs = [
        tr('Point layer : disease'),
        tr('Polygon layer : administrative boundary'),
        tr('Case field'),
        tr('Ratio'),
        tr('New column')
    ]
    outputs = [
        tr('New polygon layer with the density')
    ]
    more = [
        tr('This algorithm will count the number of points inside each '
           'polygons and run a formula to get the density.'),
        tr('number of cases / area * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_density_point():
    title = tr('Density with case layer')
    intro = tr('Compute density')
    inputs = [
        tr('Case layer'),
        tr('Polygon layer : administrative boundary with two fields pop and '
           'case'),
        tr('Ratio'),
        tr('New column')
    ]
    outputs = [
        tr('New polygon layer with the density')
    ]
    more = [
        tr('This algorithm will count the number of points inside each '
           'polygons and run a formula to get the density.'),
        tr('number of cases / area * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_blur():
    title = tr('Blurring')
    intro = tr('Plugin to blur point data, such as health personal data, and '
               'get some statistics about this blurring.')
    inputs = [
        tr('Point layer'),
        tr('Radius'),
        tr('Enveloppe : The layer will force the algorithm to have an '
           'intersection between the centroid and this layer. This is like a '
           'mask.')
    ]
    outputs = [
        tr('Blurred layer (polygon)')
    ]
    more = [
        tr('1 : Creating a buffer (radius r)'),
        picture('blurring_1.png'),
        tr('2 : Random selection of a point in each buffer'),
        picture('blurring_2.png'),
        tr('3 : Creating a buffer around the new point with the same radius. '
           'The initial point is at a maximal distance 2r of the centroid of '
           'the buffer.'),
        picture('blurring_3.png'),
        tr('4 : Deleting the random point and the first buffer'),
        picture('blurring_4.png'),
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_stats_blurring():
    title = tr('Stats')
    intro = tr('With two layers, the plugin will count the number of '
               'intersections between them and produces some stats.')
    inputs = [
        tr('Blurred layer'),
        tr('Stats layer : buildings for instanceon layer : administrative '
           'boundary')]
    outputs = [
        tr('New polygon layer with the density')
    ]
    more = [
        tr('This is usefull if you want to rate your blurring.'),
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_incidence():
    title = tr('Incidence')
    intro = tr('You can create an incidence map about a disease.')
    inputs = [
        tr('Polygon layer : administrative boundary with a population and '
           'case fields'),
        tr('Case field'),
        tr('Population field'),
        tr('Ratio'),
        tr('New column')
    ]
    outputs = [
        tr('New polygon layer with the incidence')
    ]
    more = [
        tr('This algorithm will count the number of points inside each '
           'polygons and run a formula to get the incidence.'),
        tr('number of cases / population * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_incidence_point():
    title = tr('Incidence with case layer')
    intro = tr('You can create an incidence map about a disease.')
    inputs = [
        tr('Point layer : disease'),
        tr('Polygon layer : administrative boundary with a population field'),
        tr('Population field'),
        tr('Ratio'),
        tr('New column')
    ]
    outputs = [
        tr('New polygon layer with the incidence')
    ]
    more = [
        tr('This algorithm will count the number of points inside each '
           'polygons and run a formula to get the incidence.'),
        tr('number of cases / population * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_attribute_table():
    title = tr('Export attribute table')
    intro = tr('Export as CSV format without geometry.')
    inputs = [
        tr('Vector layer')
    ]
    outputs = [
        tr('CSV file')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html
