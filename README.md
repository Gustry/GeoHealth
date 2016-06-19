<<<<<<< HEAD
## GeoHealth

GeoHealth aims to provide a simplified interface for users in epidemiology in QGIS : 
 * blurring a point layer
 * get some statistics about this blurring
 * incidence map

## Quality control
 * Travis : [![Build Status](https://api.travis-ci.org/Gustry/GeoHealth.svg)](https://travis-ci.org/Gustry/GeoHealth)
 * Landscape : [![Code Health](https://landscape.io/github/Gustry/GeoHealth/master/landscape.svg?style=flat)](https://landscape.io/github/Gustry/GeoHealth/master)

## Authors
  * Etienne Trimaille
  * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).
=======
# GeoPublicHealth 0.2

GeoPublicHealth aims to provide a simplified interface for users in epidemiology and public health for QGIS . It is based on the [GeoHealth Plugin](https://github.com/Gustry/GeoHealth) developed by Etienne Trimaille. This includes additional methods that are very relevant for the use of GIS in public health and epidemiology.

## Setup

For using the autocorrelation, please install [PySAL](https://pysal.readthedocs.io/ )

###Installing PySAL for [OSGeo4W](http://trac.osgeo.org/osgeo4w/)

  1. Run the OSGeo4W Shell on `Start -> All Programs -> OSGeo4W` menu
  2. Run in the OSGeo4W Shell  the following command  `pip install pysal`
  3. After the command finish a success message as Successfully installed `pysal-X.XX.X should appear`

###Installing PySAL for OSX QGIS
  1. In the Finder App please locate the `Applications` folder the `QGIS.app`
  1. Right click over the icon
  1. Select from the menu `Show Package Contents`
  1. Open a terminal console. Click `[Command+Space]` and write `Terminal` and press `[return]` key
  1. Write there in the Terminal prompt `cd ` (be sure that after the cd to enter a blank space)
  1. Drag from the Finder Window the `python` folder
  1. Something like `cd /Applications/QGIS.app/Contents/Resources/python` should be in your Terminal. That will depend of the actual folder where you installed QGIS
  1. Run `sudo easy_install pip` in the Terminal
  1. Run in the Terminal `pip install pysal`
  1. After the command finish a success message as `Successfully installed pysal-X.XX.X` should appear.
  1. Run in the Terminal the command  `pip install pysal` again to obtain the folder for installation
  1. Copy the folder name, for example: `/opt/boxen/homebrew/lib/python2.7/site-package`
  1. Run a command based on the copied folder name as: `cp -Rv /opt/boxen/homebrew/lib/python2.7/site-packages/pysal pysal`


## Contributing

  1. Fork it!
  2. Create your feature branch: `git checkout -b my-new-feature`
  3. Commit your changes: `git commit -am 'Add some feature'`
  4. Push to the branch: `git push origin my-new-feature`
  5. Submit a pull request :D

## History
Dr. Carlos Castillo-Salgado has teach in The Bloomberg School of Public Health of Johns Hopkins University the 340.701.11 Epidemiologic Applications of GIS the last 15 years and also in his work as Chief of the Special Program for Health Analysis for the Panamerican Health Organization, Regional Office of the World Health Organization for the Regional Office of the Americas. In this capacity, he leaded the development of [SIGEpi](http://ais.paho.org/sigepi/index.asp?xml=sigepi/index.htm&lang=en) as a pionner GIS for Epidemiology and Public Health. Now using the QGIS the GeoPublicHealth will integrated several of the methods and techniques used in SIGEpi but enhancing those with the capacities of QGIS.
  
## Credits

Original GeoHealth Plugin:
   * Etienne Trimaille
   * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).

GeoPublicHealth:
  * ePublicHealth
  * Dr. Carlos Castillo-Salgado
  * This project was desighed and extended by the Johns Hopkins/Bloomberg School of Public Health [Global Public Health Observatory](http://gpho.info/)

## License
Please see [LICENSE](LICENSE)

>>>>>>> Updating the README
