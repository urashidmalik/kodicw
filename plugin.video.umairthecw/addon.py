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

###############################################################################################
def build_url(query):
    """
    Builds query string required for navigation in pluggin
    :param query:
    :return: string with query string
    """
    return base_url + '?' + urllib.urlencode(query)
###############################################################################################
def add_shows():
    """
    Gets shows from cwtv module and add then to Kodi listing
    :return:
    """
    for current_show in current_show_list:
        url = build_url({'mode': 'show', 'id': current_show['id']})

        li = xbmcgui.ListItem(current_show['name'], iconImage=current_show['image'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)
###############################################################################################
def add_episode(id):
    """
    Gets episode of show whose id is provides as parameter
    :param id: Id of show e.g Arrow
    :return:
    """
    current_episode_list = cwtv.get_last_five_episodes(cwtv.get_show_dict_by_id(id))
    for current_episode in current_episode_list:
        url = build_url({'mode': 'episode', 'id': current_episode['id']})
        li = xbmcgui.ListItem(current_episode['name'], iconImage=current_episode['image'])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)
###############################################################################################



mode = args.get('mode', None)
if mode is None:
    print 'Adding Shows'
    add_shows()
elif mode[0] == 'show':
    print 'Adding Episodes'
    add_episode(args.get('id')[0])


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