# GeoPublicHealth 0.97

GeoPublicHealth aims to provide a simplified interface for users in epidemiology and public health for QGIS. It is based on the [GeoHealth Plugin](https://github.com/Gustry/GeoHealth) developed by Etienne Trimaille. GeoPublicHealth includes additional methods that are very relevant for the use of GIS in public health and epidemiology.

## Installation (for Windows only)
  
For windows 
- Download installation210128.zip(See the repository or this link https://github.com/raynus/GeoPublicHealth/blob/master/installation210128.zip 
The zip file contains all package in installation folder
- Start OSGeo4W Shell as administration
- py3_env
- CD to installation folder

Then

### For GGIS 3.22.1
- pip install GDAL-3.3.3-cp39-cp39-win_amd64.whl Fiona-1.8.20-cp39-cp39-win_amd64.whl libpysal-4.2.2.tar.gz pysal-2.1.0-py3-none-any.whl

### For QGIS 3.16.3
- pip install Fiona-1.8.18-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz  

### For QGIS 3.14
- pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz  
### For QGIS 3.12 and 3.10  
- pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz pyproj-2.5.0-cp37-cp37m-win_amd64.whl  
### Install the plugin
- Start QGIS and launch the plugins manager by going to the Plugins menu and selecting Manage and Install Plugins….
- In the Settings tab of the plugins settings dialog, scroll down and click on the Add…
button.
- Give the plugin repository the name epipublichealth and then add the complete URL
https://raw.githubusercontent.com/ePublicHealth/GeoPublicHealth/master/docs/plugins.xml in the URL field.
- Click on the OK button.
- Please be sure that Show also experimental plugins is checked
- Activate the All tab and in the Search field input “geopu”.
- Select the GeoPublicHealth plugin
- Click on the Install plugin button
- Close the Plugins dialog
- Check in the Plugins menu that the GeoPublicHealth plugin is a new option there

Lauch QGIS, it should up and running.

## Current developing environment (Windows 10 only, I don't have Mac)
- QGIS 3.16.3 
- Python 3.7
- Pysal 2.1, Pyproj 2.6.1, Fiona 1.8.18, libpysal 4.2.2, and geopandas 0.8.2

## Authors
  * Etienne Trimaille
  * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).
  * Manuel Vidaurre, ePublicHealth
  * Pai (Supharerk Thawillarp) -- QGIS2to3 Migration work
=======

# GeoPublicHealth 0.97

## History
Dr. Carlos Castillo-Salgado has teach in The Bloomberg School of Public Health of Johns Hopkins University the 340.701.11 Epidemiologic Applications of GIS the last 15 years and also in his work as Chief of the Special Program for Health Analysis for the Panamerican Health Organization, Regional Office of the World Health Organization for the Regional Office of the Americas. In this capacity, he led the development of [SIGEpi](http://ais.paho.org/sigepi/index.asp?xml=sigepi/index.htm&lang=en) as a pioneer GIS for Epidemiology and Public Health. Now using the QGIS, the GeoPublicHealth will integrate several of the methods and techniques used in SIGEpi but enhancing those with the capacities of QGIS.
  
## Credits

Original GeoHealth Plugin:
   * Etienne Trimaille
   * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).

GeoPublicHealth:
  * ePublicHealth
  * Dr. Carlos Castillo-Salgado
  * This project was designed and extended by the Johns Hopkins/Bloomberg School of Public Health [Global Public Health Observatory](http://gpho.info/)

## License
Please see [LICENSE](LICENSE)
