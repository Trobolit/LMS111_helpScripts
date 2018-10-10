# LMS111_helpScripts

These are a collection of python scripts that helps getting a SICK LMS111-10100, but probably any LMS1xx, under control.

* The **factoryReset** script does what it says, just replace the TCP_IP at the top to match its current settings. **Note** None of the scripts will work if the LIDAR has had its passwords changed (uncommon).
* The **setIP** stuff was made to match our current settings on the permocar, if you change these a dec to hex converter is very useful.
* The **setConfig** is a good example on how to set standard settings for most usecases, 50Hz, 0.5 deg resolution, no averaging, etc.
* The **justRun** is a tester to see that it works, and actually scans at the wanted frequency. The math is off by approx .2Hz for some reason.

## Useful tips

* As the **factoryReset** script shows; many settings require a login, setup, save to non volatile memory, logout/run and finally a hard reboot to take effect. I think that the nMeanFilter setting requires this.
* Having the datagram manual for the lidar closeby is very helpful.
