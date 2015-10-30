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


def help_open_shapefile():
    title = trans('Import shapefile')
    intro = trans('Import a shapefile into QGIS.')
    inputs = [
        trans('Shapefile')
    ]
    outputs = [
        trans('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_raster():
    title = trans('Import raster')
    intro = trans('Import a raster into QGIS.')
    inputs = [
        trans('Raster file')
    ]
    outputs = [
        trans('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_table():
    title = trans('Import table')
    intro = trans('XLS or DBF format.')
    inputs = [
        trans('Table file')
    ]
    outputs = [
        trans('New table')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_csv():
    title = trans('Import CSV table')
    intro = trans('CSV format without geometry.')
    inputs = [
        trans('CSV file')
    ]
    outputs = [
        trans('New table')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_open_xy():
    title = trans('Import CSV table')
    intro = trans('CSV format with geometry.')
    inputs = [
        trans('CSV file')
    ]
    outputs = [
        trans('New layer')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_density():
    title = trans('Density')
    intro = trans('Compute density')
    inputs = [
        trans('Point layer : disease'),
        trans('Polygon layer : administrative boundary')]
    outputs = [
        trans('New polygon layer with the density')
    ]
    more = [
        trans('This algorithm will count the number of points inside each polygons and run a formula to get the density.'),
        trans('number of cases / area * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_blur():
    title = trans('Blurring')
    intro = trans('Plugin to blur point data, such as health personal data, and get some statistics about this blurring.')
    inputs = [
        trans('Point layer'),
        trans('Radius'),
        trans('Enveloppe : The layer will force the algorithm to have an intersection between the centroid and this layer. This is like a mask.')
    ]
    outputs = [
        trans('Blurred layer (polygon)')
    ]
    more = [
        trans('1 : Creating a buffer (radius r)'),
        picture('blurring_1.png'),
        trans('2 : Random selection of a point in each buffer'),
        picture('blurring_2.png'),
        trans('3 : Creating a buffer around the new point with the same radius. The initial point is at a maximal distance 2r of the centroid of the buffer.'),
        picture('blurring_3.png'),
        trans('4 : Deleting the random point and the first buffer'),
        picture('blurring_4.png'),
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_stats_blurring():
    title = trans('Stats')
    intro = trans('With two layers, the plugin will count the number of intersections between them and produces some stats.')
    inputs = [
        trans('Blurred layer'),
        trans('Stats layer : buildings for instanceon layer : administrative boundary')]
    outputs = [
        trans('New polygon layer with the density')
    ]
    more = [
        trans('This is usefull if you want to rate your blurring.'),
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_incidence():
    title = trans('Incidence')
    intro = trans('You can create an incidence map about a disease.')
    inputs = [
        trans('Point layer : disease'),
        trans('Polygon layer : administrative boundary with a population field')
    ]
    outputs = [
        trans('New polygon layer with the incidence')
    ]
    more = [
        trans('This algorithm will count the number of points inside each polygons and run a formula to get the incidence.'),
        trans('number of cases / population * ratio')
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html


def help_attribute_table():
    title = trans('Export attribute table')
    intro = trans('Export as CSV format without geometry.')
    inputs = [
        trans('Vector layer')
    ]
    outputs = [
        trans('CSV file')
    ]
    more = [
    ]
    html = html_table(title, intro, inputs, outputs, more)
    return html
