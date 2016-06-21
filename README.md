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

##Setup

###Installing GeoPublicHealth Plugin
  1. Start QGIS and launch the plugins manager by going to the **Plugins menu and selecting Manage and Install Plugins….**
  1. In the **Settings** tab of the plugins settings dialog, scroll down and click on the **Add…** button.
  1. Give the plugin repository the name **epipublichealth** and then add the complete URL **http://epublichealth.co/oss/qgis/plugins/plugins.xml** in the URL field.
  1. Click on the **OK** button.
  1. Activate the **All** tab and in the **Search** field input **geopu**.
  1. Select the *GeoPublicHealth* plugin
  1. Click on the **Install plugin** button
  1. Close the Plugins dialog 
  1. Check in the **Plugins** menu that the **GeoPublicHealth** plugin is a new option there

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
Please review the [Contribution Guidelines](.github/CONTRIBUTING)

  1. Fork it!
  2. Create your feature branch: `git checkout -b my-new-feature`
  3. Commit your changes: `git commit -am 'Add some feature'`
  4. Push to the branch: `git push origin my-new-feature`
  5. Submit a pull request :D

###Reporting Issues

This section guides you through submitting a issue report for GeoPublicHealth. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report).

#### Before Submitting A Bug Report
.
* **Perform a [cursory search](https://github.com/ePublicHealth/GeoPublicHealth/issues)** to see if the problem has already been reported. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on thir repository and provide the following information.

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
* **Did the problem start happening recently** (e.g. after updating to a new version ) or was this always a problem?
* If the problem started happening recently, **can you reproduce the problem in an older version?** What's the most recent version in which the problem doesn't happen?
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.
* If the problem is related to working with files (e.g. opening and editing files), **does the problem happen for all files and projects or only some?** Does the problem happen only when working with local or remote files (e.g. on network drives), with files of a specific type , with large files or files with very long lines, or with files in a specific encoding? Is there anything else special about the files you are using?

Include details about your configuration and environment:

* **Which version of QGIS are you using?** 
* **What's the name and version of the OS you're using**?
* **Which keyboard layout are you using?** Are you using a US layout or some other layout?

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
