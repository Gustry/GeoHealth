## GeoHealth upgrade for QGIS 3.0 (In progress)

The project aims to upgrade the GeoPublicHealth 0.95 the GeoPublicHealth to work under QGIS 3.0 (3.10) No change on the orginal function.

**Still in progress, and most function are still broken

## Current progress
- qgis2to3 refactored
- Revised code to work on QGIS API 3
- Plugin loading success
- Main window intiation success
- Incidence function success
- <Working> Pysal migration to 2.0

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
