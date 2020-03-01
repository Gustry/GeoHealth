## GeoHealth upgrade for QGIS 3.0 (In progress)

The project aims to upgrade the GeoPublicHealth 0.95 the GeoPublicHealth to work under QGIS 3.0 (3.10) No change on the orginal function.

Tested on QGIS 3.10 and QGIS 3.12 on Windows 10 only. 

## Installation
- PLEASE SEE INSTALLATION folder README first, after download the plugin or download an entire installation folder separately then follow the instruction inside. 


## Installation details (Similar to README file in installation folder)
- As QGIS 3 does not support python module integration, we have run it from OSGEO command prompt. 
Please follow the follwing steps to make the plugin works.


1. Open osgeo shell from qgis directory (run as admin if you are on Windows)
2. Run the following command
2.1 py3_env

Run the following command on OSGEO shell

For windows 
pip install Fiona-1.8.13-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz

For Mac
pip install Fiona-1.8.13.post1-cp27-cp27m-macosx_10_9_x86_64 pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz

3. Lauch QGIS, it should up and running.

## Current developing environment (Windows 10 only, I don't have Mac)
- QGIS 3.10
- Python 3.7
- Pysal 2.1

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
