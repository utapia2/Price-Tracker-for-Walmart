import requests
from bs4 import BeautifulSoup
import smtplib
import time

def BestbuyPriceTracker():
    print('caling bestbuy tracker')

def WalmartPriceTracker():
    print('caling walmart tracker')
    while True:

        website = input('Enter Walmart item page you want to track: ')
        response = requests.get(website)

        if response.status_code == 200:
            print('Success! Website is accessible')
            time.sleep(3)

        soup = BeautifulSoup(response.content, "lxml")

        price = soup.find('span', {'class': "price-characteristic"})

        eprice = float(price["content"])

        print ('Price is ' ,  eprice);
        wishprice = float(input('Enter the price you wish to notify you when the item is that price or lower: '))

        if eprice <= wishprice:

            print('Your item is on sale! sending email...')
            sent_from = 'codemail5678@gmail.com'
            password = 'qwzx5678'
            to = 'utapia24@gmail.com'
            body = 'Your item is now $' + str(eprice) + ' dollars! \n ' \
                                                       'Go to the page: ' + website
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(sent_from, password)
            server.sendmail(sent_from, to, body)
            server.close()
            break

        else:
            print('Item is not on sale')
            freq = int(input('How often would you like to check for this price? ex: Type 2 for every 2 hours: '))
            print('Okay program will check every', freq,' hours')
            #temporary exit(), remove when actually price tracking
            exit()
            time.sleep(freq*60*60)
            print('Checking again!')


def main():

    print("in main funcion")

    selection = int(input("Enter 1 for Walmart \nEnter 2 for BestBuy \nEnter 3 for Target\n: "))

    if selection == 1:
        WalmartPriceTracker()

    else:
        exit()

if __name__ == '__main__':
    main()
