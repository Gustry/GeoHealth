# GeoPublicHealth 0.97

GeoPublicHealth aims to provide a simplified interface for users in epidemiology and public health for QGIS. It is based on the [GeoHealth Plugin](https://github.com/Gustry/GeoHealth) developed by Etienne Trimaille. GeoPublicHealth includes additional methods that are very relevant for the use of GIS in public health and epidemiology.

## Installation (for Windows only)
  
For windows 
- Download installation210128.zip(See the repository or this link https://github.com/raynus/GeoPublicHealth/blob/master/installation210128.zip 
The zip file contains all package in installation folder
- Start OSGeo4W Shell (For QGIS below 3.22.1, start the shell as administration)
- (For QGIS below 3.22.1) py3_env
- CD to installation folder

Then

### For GGIS 3.22.1
- pip install GDAL-3.3.3-cp39-cp39-win_amd64.whl Fiona-1.8.20-cp39-cp39-win_amd64.whl libpysal-4.2.2.tar.gz pysal-2.1.0-py3-none-any.whl

**If error AttributeError: ‘PathMetadata’ object has no attribute ‘isdir’
Run the following command and retry
- pip install pip==21.3.1 --user


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
=======
## The master branch currently is a GeoHealth upgrade for QGIS 3.x

This branch aims to upgrade the GeoPublicHealth 0.95 the GeoPublicHealth to work under QGIS 3.x (from 3.10) No change on the original function.

We tested on QGIS 3.16 on Windows 10 only and Mac. 

**Install provided Fiona from the "installation" directory only as the newer version causes problems with GDAL.

## Installation (for Windows only)
  
For windows 
1. Go to https://github.com/raynus/GeoPublicHealth/blob/master/installation210128.zip?raw=true for downloading the required libraries, take note of the downloading folder
1. Go to https://qgis.org/en/site/forusers/download.html and download OSGeo4W that correspond to your chip architecture (32 or 64)
1. To get the long term release (that is not also the latest release) choose Advanced Install and select **qgis-ltr-full** also **Fiona-1.8.18**
1. After installation is finished. Start OSGeo4W Shell as administration (go to the file and make right-click)
1. run `py3_env` to set the environmental variables required
1. CD to download folder, ex: `cd Downloads`
1. run `pip install Fiona-1.8.18-cp37-cp37m-win_amd64.whl pysal-2.1.0-py3-none-any.whl libpysal-4.2.2.tar.gz esda`
1. If there are no error messages, you are ready. An announcement regarding **pip** upgrade is OK.

## Current developing environment (Windows 10 only, I don't have Mac)
- QGIS 3.16.3 
- Python 3.7
- Pysal 2.1, Pyproj 2.5, Fiona 1.8.13, libpysal 4.2.2, and geopandas 0.7

## Install in Mac
  1. Click on https://qgis.org/downloads/macos/qgis-macos-ltr.dmg to download the **QGIS macOS Installer Version 3.16** installer
  1. Run the installer and follow instructions
  1. In some cases the **https://www.xquartz.org/** should be installed. If you have a error about `Library not loaded: /opt/X11/lib/libxcb.1.dylib` the installing of xquartz will fixed.

### Installing GeoPublicHealth Plugin
  1. Start QGIS and launch the plugins manager by going to the **Plugins menu and selecting Manage and Install Plugins….**
  1. In the **Settings** tab of the plugins settings dialog, scroll down and click on the **Add…** button.
  1. Give the plugin repository the name **epipublichealth** and then add the full URL **https://raw.githubusercontent.com/ePublicHealth/GeoPublicHealth/main/docs/plugins.xml** in the URL field.
  1. Please be sure that `Show also experimental plugins` is checked [x]
  1. Click on the **OK** button.
  1. Activate the **All** tab and **Search** field input **geopu**.
  1. Select the *GeoPublicHealth* plugin
  1. Click on the **Install plugin** button
  1. Close the Plugins dialog 
  1. Check in the **Plugins** menu that the **GeoPublicHealth** plugin is a new option there

## Contributing
Please review the [Contribution Guidelines](CONTRIBUTING.md)

  1. Fork it!
  2. Create your feature branch: `git checkout -b my-new-feature`
  3. Commit your changes: `git commit -am 'Add some feature'`
  4. Push to the branch: `git push origin my-new-feature`
  5. Submit a pull request :D

### Reporting Issues

This section guides you through submitting an issue report for GeoPublicHealth. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report).

#### Before Submitting A Bug Report

* **Perform a [cursory search](https://github.com/ePublicHealth/GeoPublicHealth/issues)** to see if the problem has already been reported. If it has, adds a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on this repository and provide the following information.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. 
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** which show you following the described steps and clearly demonstrate the problem. If you use the keyboard while following the steps, **record the GIF**. You can use [this tool](http://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **If you're reporting that GeoPublicHealth crashed**, include a crash report with the log from QGIS. Include the log report in the issue in a [code block](https://help.github.com/articles/markdown-basics/#multiple-lines), a [file attachment](https://help.github.com/articles/file-attachments-on-issues-and-pull-requests/), or put it in a [gist](https://gist.github.com/) and provide link to that gist.
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.

Provide more context by answering these questions:

* **Can you reproduce the problem?**
* **Did the problem start happening recently** (e.g., after updating to a new version ) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version?** What's the most recent version in which the problem doesn't happen?
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it usually happens.
* If the problem is related to working with files (e.g., opening and editing files), **does the problem happen for all files and projects or only some?** Does the problem happen only when working with local or remote files (e.g., on network drives), with files of a specific type, with large files or files with very long lines, or with files in a specific encoding? Is there anything else special about the files you are using?

Include details about your configuration and environment:

* **Which version of QGIS are you using?** 
* **What's the name and version of the OS you're using**?
* **Which keyboard layout are you using?** Are you using a US layout or some other layout?

## Authors
  * Etienne Trimaille
  * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).
  * Manuel Vidaurre, ePublicHealth
  * Pai (Supharerk Thawillarp) -- QGIS2to3 Migration work
=======

# GeoPublicHealth 0.97

## History
Dr. Carlos Castillo-Salgado has taught in The Bloomberg School of Public Health of Johns Hopkins University the 340.701.11 Epidemiologic Applications of GIS the last 15 years and also in his work as Chief of the Special Program for Health Analysis for the Panamerican Health Organization, Regional Office of the World Health Organization for the Regional Office of the Americas. In this capacity, he led the development of [SIGEpi](http://ais.paho.org/sigepi/index.asp?xml=sigepi/index.htm&lang=en) as a pioneer GIS for Epidemiology and Public Health. Using the QGIS, the GeoPublicHealth will integrate several of the methods and techniques used in SIGEpi but enhance those with the capacities of QGIS. In February 2020, [Pai (Supharerk Thawillarp)](https://github.com/raynus) did the migration work for the plugin from QGIS 2 systems to QGIS 3.
  
## Credits

Original GeoHealth Plugin:
   * Etienne Trimaille
   * This project was designed by UMR Espace-DEV (IRD, UAG, UM2, UR).

GeoPublicHealth:
  * ePublicHealth
  * Dr. Carlos Castillo-Salgado
  * This project was designed and extended by the Johns Hopkins/Bloomberg School of Public Health [Global Public Health Observatory](http://gpho.info/)

## License
Please see [LICENSE](LICENSE) @ 2021
