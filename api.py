import json
import re
from http.cookiejar import CookieJar
from urllib.request import urlopen, HTTPCookieProcessor, build_opener, Request
from urllib.parse import urlencode, unquote_to_bytes

#from lxml.etree import fromstring, XMLParser
#from lxml.html.soupparser import fromstring

class APISession(object):
    def __init__(self):
        self.login_url = "https://www.fitocracy.com/accounts/login/"
        self.cookie_jar = CookieJar()
        self.opener = build_opener(HTTPCookieProcessor(self.cookie_jar))
        self.activity_list = False
        self.user_id = False
        self.activity_data = False

    def login(self, user, password):
        login = self.opener.open(self.login_url)
    
        csrf = None
        for cookie in self.cookie_jar:
            if cookie.name == "csrftoken":
                csrf = cookie.value
    
        post_data = bytes(urlencode({'username': user, 
                                     'password': password, 
                                     'csrfmiddlewaretoken': csrf, 
                                     'login': 'Log In', 
                                     'next': ''}
                                    ), encoding="utf_8")
        
        headers = {"Referer": "https://www.fitocracy.com/accounts/login/", "Origin": "https://www.fitocracy.com"}
    
        request = Request(self.login_url, post_data, headers=headers)
        response = self.opener.open(request)
        
        content = str(response.read())

        if "Please enter a correct username and password" in content:
            return False
        else:
            return True

    def _get_user_id(self):

        response = self.opener.open("http://www.fitocracy.com/profile")
        content = str(response.read())

        self.user_id = re.search("""var user_id = "(.+?)";""", content).group(1)

    def _get_activity_list(self):
        # Find values and names of exercises from options of 
        # the select element with id "history_activity_chooser".
        # For each value found, we can make a call to:
        # http://www.fitocracy.com/get_history_json_from_activity/{ACTIVITY}/?max_sets=-1&max_workouts=-1&reverse=1
        # where {ACTIVITY} is the value for the activity in question (a number).
        #cleaned_content = re.sub("<script.*?>.*</script>", "", content)
        #document = fromstring(cleaned_content)

        #selection = document.find(".//select[@id='history_activity_chooser']")
        #for option in selection.findall("option"):
        #    activity_list[option.text] = option.get("value")

        #select_list = re.search(
                    #"""<select id="history_activity_chooser".+>
                    #(.*)
                    #</select>""", content, re.X).group(1)

        if not self.user_id:
            self._get_user_id()

        response = self.opener.open("http://fitocracy.com/get_user_activities/{0}/".format(self.user_id))

        content = response.read().decode("utf8")

        self.activity_list = json.loads(content)
        
    def _get_activity_data_by_id(self, id):
        
        response = self.opener.open("http://fitocracy.com/get_history_json_from_activity/{0}/".format(id), b'max_sets=-1&max_workouts=-1&reverse=1')

        self.activity_data[id]['data'] = json.loads(response.read().decode("utf8"))

    def _get_all_activities(self):

        if not self.activity_list:
            self._get_activity_list()
        
        for activity in self.activity_list:
            self._get_activity_data_by_id(activity['id'])