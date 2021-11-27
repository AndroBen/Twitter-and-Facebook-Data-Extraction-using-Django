import facebook
import datetime
import requests
import json
import urllib3

def main():
    token='enter your token'
    graph=facebook.GraphAPI(token)
    profile=graph.get_object('me',fields='id,name,first_name,last_name,link,birthday,gender')
    print(json.dumps(profile,indent=4))


main()