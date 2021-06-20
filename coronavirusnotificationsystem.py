#Realtime CoronaVirus Outbreak Notification System


from plyer import notification         #notification module
import requests                        #allows to send HTTP requests and The HTTP request returns a Response Object with all the response data
from bs4 import BeautifulSoup          #for getting data out of HTML and parse it in a readable manner.
import time

def notif(title,message):              #function for notification
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\suman\\Desktop\\New folder (2)\\icon.ico",
        timeout = 20
    )


def getdata(url):                     #function for the covid data url
    r = requests.get(url)
    return r.text


if __name__ == "__main__":

    while(True):
        myHtmlData = getdata("https://www.mohfw.gov.in/")
        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        
        active_cases = soup.find("li" , {"class" : "bg-blue"}).findChildren("strong")[1].get_text()
        # print(active_cases.get_text())     

        discharged_cases = soup.find("li" , {"class" : "bg-green"}).findChildren("strong")[1].get_text()
        # print(discharged_cases) 

        death_cases = soup.find("li" , {"class" : "bg-red"}).findChildren("strong")[1].get_text()
        # print(death_cases)

        notification_title = "COVID-19 STATUS" 
        notification_text = f" Active cases : {active_cases}\nDischarged : {discharged_cases}\nDeaths : {death_cases}"
        notif(notification_title,notification_text)
        time.sleep(3600)
