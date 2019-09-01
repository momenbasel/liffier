# liffier
tired of manually add dot-dot-slash to your possible path traversal? this short snippet will increment ../ on the URL.


[*] Python3 is required and requests library (pip3 install requests)




## Usage:
1. git clone https://github.com/momenbasel/liffier.git
2. cd liffier && python3 liffier.py
3. enter the url to test on and the possible vulnerable parameter at the end of the URL, as the tool only appends at the end of the URL
4. enter internal filename with bypasses like nullbyte (https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Directory%20Traversal)
5. enter the number of requests that the tool will send || number of times the tool will append another ../ to the request.
