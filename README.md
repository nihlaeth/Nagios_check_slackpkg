# Nagios_check_slackpkg
Nagios plugin for monitoring available updates via slackpkg

This script returns a list of packages that need upgrading. It fetches an updated package list from the mirror, but does not download or install any packages itself.

If you need to use this as an unprivileged user, compile the c wrapper and do the setuid root trick with it. Move the result to be in the PATH of your unprivleged user (it won't work otherwise!).
  gcc -o myslackpkg slackpkgwrap.c
You also need to make sure your user has the correct gpg keys in their home directory for this binary to work for an unprivileged user.

~~Caveat: myslackpkg won't blindly parrot arguments you pass to it. But it's by no means 100% secure. Using setuid root on this binary is a security risk.~~ fixed as of b46e63819c1f3ed7ca6f7d9040460e1b315f650f

Example nagios command definition:
```
# 'check_remote_slackpkg' command definition
define command{
    command_name    check_remote_slackpkg
    command_line    $USER1$/check_by_ssh -H $HOSTADDRESS$ -C "TERM=xterm bin/check_slackpkg_nonpriv.py"
    }
```

Author: Nihlaeth <info@nihlaeth.nl>
