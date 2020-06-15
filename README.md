# WorldLink-SafeNet-supplement
WorldLink-SafeNet Supplement | An automated tool in Python to whitelist/blacklist a large number of domains without user intervention | For use with SafeNet feature enabled | Best for using to filter ad, malware, porn sites

------------------------------------------------------------
*WorldLink = WorldLink Communications (Pvt.) Ltd. - an ISP of Nepal

Ever wanted to block/blacklist (or whitelist) a large number of sites using WorldLink's 'White List/Black List' feature under SafeNet? Well, now a large number of sites providing advertisement services (for e.g. ads.google.com), sites with malwares, porn, etc. can be easily blocked on all your devices connected to your router, and that, too, in an automated way using the power of Python and Selenium! 


There are a large number of 'hosts' files in the internet. You will have to trim unnecessary parts of such 'hosts' files yourself before mentioning path in the code. This program will automate adding the domains for you. All the domains that have been added to 'White List/ Black List' tab will be saved on a different file, which you will have to mention on the code before running it. You can see a text file sampleBlocklist.txt in my repo to get the idea of what I mean by 'trim'. That is only a portion of the 'hosts' file which can be found at: https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts. I made that truncated/trimmed list just to test with the program, and yes, for sample as well.

*(You don't ever need to worry about me obtaining your any kind of data, because everything will happen on your side. I will not even know if you are viewing anything on my repo! :D)


Currently I've added support for firefox browser only. If you need it for any other browser, you can either do a feature-request or add it yourself.

In some cases same thing (like clicking a button, or passing text to a text-field) has been implemented in two different ways, one with use of Python directly and another by wrapping JavaScript in Python code.

I've used Selenium module, geckodriver (for using with firefox) and PyAutoGUI module (https://github.com/asweigart/pyautogui) among others. But PyAutoGUI is not mandatory, you can use the code by commenting the part that uses this module.



**PLEASE NOTE that I cannot guarantee about anything, and neither liable if you misued it or it caused any problem to - be it your WorldLink account or your computer system by its use.

*I recently discovered that you are allowed to add only about 119 domains to the list, hence you will need to be sure which ones to add.
