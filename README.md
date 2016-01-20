# Nagios_check_slackpkg
Nagios plugin for monitoring available updates via slackpkg

This script returns a list of packages that need upgrading. It fetches an updated package list from the mirror, but does not download or install any packages itself.

If you need to use this as an unprivileged user, compile the c wrapper and do the setuid root trick with it.
  gcc -o check_slackpkg scriptwrap.c

Author: Nihlaeth <info@nihlaeth.nl>
