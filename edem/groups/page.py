# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gs.group.stats import GroupPostingStats
from gs.groups.page import GroupsPage  # TODO: Move all of gs.groups.page here.


class EDemGroupsPage(GroupsPage):

    def __init__(self, groups, request):
        super(EDemGroupsPage, self).__init__(groups, request)
        self.groups = groups

    def get_stats(self, groupInfo):
        retval = GroupPostingStats(groupInfo)
        return retval
