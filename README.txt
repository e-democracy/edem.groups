==============================
``edem.groups``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
E-Democracy's customization of the groups page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Bill Bushey`_
:Contact: Bill Bushey <bill.bushey@e-democracy.org>
:Date: 2013-09-30
:Organization: `E-Democracy`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 License`_
  by `E-Democracy`_.

Introduction
===========

This product provides the /groups page of forums.e-democracy.org, and it
disables the Groups site home viewlet provided by `gs.groups`_.

/groups
=======

`E-Democracy`_ has 50+ groups falling into multiple categories. Because of
this, E-Democracy continues to use the /groups page that use to be provided
by `GroupServer`_ to list all of the groups available on the site, and divide
the listing of those groups up by category.

With the release of `GroupServer 14.03`_, core support for that page has been
deprecated in GroupServer. To continue to make /groups available on 
forums.e-democracy.org, much of the logic and template that supported 
GroupServer's /groups page have been imported into this egg. The logic can be
found in **page.py**, which provides the *EDemGroupsPage* Browser View that is
based on code that use to be found in gs.groups. The template can be found in
**browser/templates/groups_homepage.pt**, which again is based largely on a
template that use to be part of `gs.groups`_. 

Having imported the logic and template of gs.groups' /groups page, the
E-Democracy page is now able to exist independent of what is provided by 
gs.groups.

Disabled Groups Viewlet on the Homepage
=======================================

Again, because of the large number of groups on forums.e-democracy.org, it
became clear that E-Democracy needed a different way to display the site's
groups than the default listing of groups on the site homepage provided by
GroupServer. Thus, this egg disables the site home's listing of groups via
the *GroupsSiteHomeViewlet* in **viewlets.py**, which simply has a show()
method that returns False.

Resources
=========

- Code repository: https://github.com/e-democracy/edem.groups
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _E-Democracy: http://e-democracy.org/
.. _Bill Bushey: http://groupserver.org/p/wbushey
.. _Groupserver 14.03:
   http://groupserver.org/groups/groupserver_announcements/messages/topic/7apc0CDT4ReT0DrKfsnQy5
.. _gs.groups: https://source.iopen.net/groupserver/gs.groups/summary
.. _Creative Commons Attribution-Share Alike 3.0 License:
   http://creativecommons.org/licenses/by-sa/3.0/
