import base64
import urllib2
import re
import sys
import xbmcgui
import xbmcplugin
import m3u8
from pprint import  pprint


url_dict = {
    "main": "http://www.cwtv.com",
    "shows": "http://www.cwtv.com/shows/"

}

def __get_cw_page_(url, ref_url='http://www.cwtv.com/shows/the-flash/'):
    """
    Helper function to get the page data

    :param url: Url to be fetched
    :param ref_url: Referencing URL
    :return: Page Data in Text
    """
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    req.add_header('Referer', base64.b64decode(ref_url))
    response = urllib2.urlopen(req)
    data = response.read()
    response.close()
    return data

def get_shows_list():
    """
    Gets the current running shows
    :return List [] containing Dict {}

    """
    current_shows = __get_cw_page_(url_dict.get("shows"))
    # Gets Current Show Div which contains all shows
    match = re.compile('(<ul class=\"shows\">(?s).*?</ul>)').findall(current_shows)

    # Get each li which contains all shows
    match = re.compile('<li class=\"\">(.*\n.*\n.*\n.*\n.*\n.*\n.*\n)').findall(str(match[0]))
    shows_list = []
    for shows_content in match:
        img_match = re.compile('img(.*)(src="(.*)" alt)').findall(str(shows_content))
        show_name_match = re.compile('<p class=\"t\">(.*)</p>').findall(str(shows_content))
        show_url_match = re.compile('<a class=\"hublink\" href=\"(.*)\">').findall(str(shows_content))
        if show_name_match[0] != "More Video" :
            show_dic = dict(image=img_match[0][2], name=show_name_match[0], url=url_dict.get("main")+show_url_match[0])
        shows_list.append(show_dic)
    return shows_list


def get_last_five_episodes(show_dict):
    """
    Fetches Latest Five Episodes for requested show

    :param show_dict: Dictionary containing image, name, url
    :return: episode_list: List [] containing Dict {} image, name, url
    """
    current_episodes = __get_cw_page_(show_dict.get("url"))

    # Gets Current Show Div which contains all shows
    match = re.compile('<ul id=\"list_1\"((.|\n)*?)<\/ul>').findall(current_episodes)

    img_match = re.compile('img src="(.*)"').findall(match[0][0])
    name_match = re.compile('videodetails1.*\n.*<p>(.*)<').findall(match[0][0])
    url_match = re.compile('<a class="thumbLink" href="(.*)">').findall(match[0][0])
    episode_list = []
    i = 0
    for name in name_match :
        episode_dict = dict(image=img_match[i], name=name_match[i], url=url_dict.get("main")+url_match[i])
        i += 1
        episode_list.append(episode_dict)
    return episode_list

##########################################################

#allShows = get_shows_list()
#allEpisodes = get_last_five_episodes(allShows[0])
#pprint(allEpisodes)
#m3u8_obj = m3u8.load("http://hlsioscwtv.warnerbros.com/hls/2015/02/24/Arrow-315-NandaParbat-3J5165-CW-Stereo_a12c4752a_2100kbps/Arrow-315-NandaParbat-3J5165-CW-Stereo_a12c4752a_2100kbps.m3u8");
#m3u8_obj = m3u8.load("http://www.cwtv.com/shows/arrow")
#print( m3u8_obj.segments)

addon_handle = init(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
url = ''
li = xbmcgui.ListItem("My First Video", iconImage='DefaultIcon.png')
xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li)
xbmcplugin.endOfDirectory(addon_handle)
