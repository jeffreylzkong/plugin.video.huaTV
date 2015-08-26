# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/nba
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.huaTV'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

# Entry point
def run():
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):

    plugintools.add_item(
        #action="",
        title="剧场1",
        url="plugin://plugin.video.youtube/channel/UCeb_lcsrAC4-_Qfb6syoADg/playlists/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item(
        #action="",
        title="剧场2",
        url="plugin://plugin.video.youtube/channel/UC4Kf3NigNJk1GVLi8UlE5TQ/playlists/",
        thumbnail=icon,
        folder=True )


    plugintools.add_item(
        #action="",
        title="剧场3",
        url="plugin://plugin.video.youtube/user/NBSCAST/playlists/",
        thumbnail=icon,
        folder=True )


    plugintools.add_item(
        #action="",
        title="剧场4",
        url="plugin://plugin.video.youtube/channel/UCpIpkRVIqJ9ugD5bhRVPwpQ/playlists/",
        thumbnail=icon,
        folder=True )

run()