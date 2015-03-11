import base64
import urllib2
import re
from pprint import  pprint


url_dict = {
    "main": "http://www.cwtv.com",
    "shows": "http://www.cwtv.com/shows/"

}
def getShowsList():
    """
    Gets the current running shows
    :return List [] containing Dict {}

    """
    req = urllib2.Request(url_dict.get("shows"))
    req.add_header('User-Agent', 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10')
    req.add_header('Referer', base64.b64decode('http://www.cwtv.com/shows/the-flash/'))
    response = urllib2.urlopen(req)
    current_shows = response.read()
    response.close()

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
            show_dic = dict(image=img_match[0][2], name=show_name_match[0], url=show_url_match[0])
        shows_list.append(show_dic)
    return shows_list

allShows = getShowsList()

