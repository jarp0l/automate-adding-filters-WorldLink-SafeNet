# automate-adding-filters-WorldLink-SafeNet
Automate adding a large number of domains to SafeNet filter.

------------------------------------------------------------
*WorldLink = WorldLink Communications (Pvt.) Ltd.

There are a large number of 'host' files out there. Unnecessary parts of such 'host' files should be trimmed as in the [sampleBlocklist.txt](./sampleBlocklist.txt). This program will automate adding the domains for you. All the domains that have been added to 'White List/ Black List' tab will be saved on a different file, which you will have to mention on the code before running it. [sampleBlocklist.txt](./sampleBlocklist.txt) is trimmed version of: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts.

In some cases same thing (like clicking a button, or passing text to a text-field) has been implemented in two different ways, one with use of Python directly and another by wrapping JavaScript in Python code.

I've used Selenium module, geckodriver (for using with firefox) and PyAutoGUI module (https://github.com/asweigart/pyautogui) among others. But PyAutoGUI is not mandatory, simply it can be commented in the script.

*Allowed number of domains for filtering (found it some time ago) is around 120 only.*
