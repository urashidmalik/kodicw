import urllib
import urlparse
import sys
import xbmcgui
import xbmcplugin
from resources.lib import cwtv

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'cwtv')



def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def addShows():
    current_show_list = cwtv.get_shows_list()
    mode = args.get('mode', None)
    if mode is None:
        for current_show in current_show_list:
            rl = build_url({'mode': 'folder', current_show.id: current_show.name})
            li = xbmcgui.ListItem(current_show.name, iconImage=current_show.image)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=current_show.url,
                                    listitem=li, isFolder=True)
        xbmcplugin.endOfDirectory(addon_handle)


addShows()


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