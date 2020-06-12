## GeoHealth upgrade for QGIS 3.0 (In progress)

The project aims to upgrade the GeoPublicHealth 0.95 the GeoPublicHealth to work under QGIS 3.0 (3.10 and 3.12) No change on the orginal function.

Tested on QGIS 3.10 and QGIS 3.12 on Windows 10 only. **Install provided Fiona from "installation" directory only as the newer version causes problem with GDAL.

## Installation (for Windows only)
  
For windows 
- Download all packages provided in the installation folder.
- Start OSGeo4W Shell as administration
- py3_env
- CD to installation folder
- pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz pyproj-2.5.0-cp37-cp37m-win_amd64.whl

3. Lauch QGIS, it should up and running.

## Current developing environment (Windows 10 only, I don't have Mac)
- QGIS 3.10 and QGIS 3.12
- Python 3.7
- Pysal 2.1, Pyproj 2.5, Fiona 1.8.13, libpysal 4.2.2, and geopandas 0.7

## Quality control
 * Travis : [![Build Status](https://api.travis-ci.org/Gustry/GeoHealth.svg)](https://travis-ci.org/Gustry/GeoHealth)
 * Landscape : [![Code Health](https://landscape.io/github/Gustry/GeoHealth/master/landscape.svg?style=flat)](https://landscape.io/github/Gustry/GeoHealth/master)

## Authors
  * Etienne Trimaille
  * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).
  * Pai (Supharerk Thawillarp) -- QGIS2to3 Migration work
=======

# GeoPublicHealth 0.95

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
