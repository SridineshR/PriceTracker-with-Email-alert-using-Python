import time
import requests
from bs4 import BeautifulSoup
import smtplib
def check_price(URL, threshold_amt):
    headers = {'User-Agent':"Your user agent"}
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    price = soup.find(id="ur_tag").get_text()[1:].strip().replace(',','')#this will be ur tag where you want to scrap the content it wil be there while you view your current page as html.
    Fprice = float(price)
    print(Fprice)
    if Fprice < threshold_amt:
            alert_me(URL,Fprice)
def alert_me(URL,price):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('Your_Username','Your_app password')
    
    subject = 'Price fell down for '
    body = 'Buy it now here: '+URL
    msg = f"Subject:{subject}\n\n{body}"
    
    server.sendmail('sender_mail','Receiver_mail',msg)
    print('Email alert sent')
    server.quit()
while True:
    check_price("Your_url",thresholdvalue)
    time.sleep(300)#You can give as per ur wish for scraping website frequently
