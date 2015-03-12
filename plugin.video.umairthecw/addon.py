import urllib
import urlparse
import sys
import xbmcgui
import xbmcplugin
from resources.lib import cwtv

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
current_show_list = cwtv.get_shows_list()

xbmcplugin.setContent(addon_handle, 'cwtv')



def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def add_shows():
    for current_show in current_show_list:
        url = build_url(current_show)
        li = xbmcgui.ListItem(current_show['name'], iconImage=current_show['image'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)

def add_episode():
    for current_show in current_show_list:
        current_episode_list = cwtv.get_last_five_episodes(current_show)
        url1 = build_url(current_show)
        for current_episode in current_episode_list:
            url = build_url(current_episode)
            li = xbmcgui.ListItem(current_episode['name'], iconImage=current_episode['image'])
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url1,
                                        listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)

mode = args.get('mode', None)
if mode is None:
    add_shows()
elif mode[0] == 'show':
    add_episode()
    pass

# if mode is None:
#     url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
#     li = xbmcgui.ListItem('Folder One', iconImage='DefaultFolder.png')
#     xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
#                                 listitem=li, isFolder=True)
#
#     url = build_url({'mode': 'folder', 'foldername': 'Folder Two'})
#     li = xbmcgui.ListItem('Folder Two', iconImage='DefaultFolder.png')
#     xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
#                                 listitem=li, isFolder=True)
#
#     xbmcplugin.endOfDirectory(addon_handle)
#
# elif mode[0] == 'folder':
#     foldername = args['foldername'][0]
#     url = 'http://localhost/some_video.mkv'
#     li = xbmcgui.ListItem(foldername + ' Video', iconImage='DefaultVideo.png')
#     xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
#     xbmcplugin.endOfDirectory(addon_handle)