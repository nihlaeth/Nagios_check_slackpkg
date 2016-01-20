# Nagios_check_slackpkg
Nagios plugin for monitoring available updates via slackpkg

This script returns a list of packages that need upgrading. It fetches an updated package list from the mirror, but does not download or install any packages itself.

If you need to use this as an unprivileged user, compile the c wrapper and do the setuid root trick with it. Move the result to be in the PATH of your unprivleged user (it won't work otherwise!).
  gcc -o myslackpkg slackpkgwrap.c

Caveat: myslackpkg won't blindly parrot arguments you pass to it. But it's by no means 100% secure. Using setuid root on this binary is a security risk. Patches are welcome - otherwise I'll come back to it when I have a better grasp of the C language.

Author: Nihlaeth <info@nihlaeth.nl>
