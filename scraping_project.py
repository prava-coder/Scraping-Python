#importing requests module
import requests
#importing beautifulsoup module
from bs4 import BeautifulSoup as bs
#creating a variable to get the input from the user
github_user=input("enter the gitub user name:")
#creating a variable url to get the url of the github user
url="https://github.com/"+github_user
#requesting the url page to get the by using the requests.get function
r=requests.get(url)
#creating a variable soup to get the html content of the page by using the beautiful soup
soup=bs(r.content,"html.parser")
#to print the profile image we use the soup.find
profile_image=soup.find("img",{"alt":"Avatar"})["src"]
print(profile_image)