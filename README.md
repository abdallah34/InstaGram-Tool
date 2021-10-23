# InstaGram-Tool
For Linux only
1) apt install git
2) git clone https://github.com/abdallah34/InstaGram-Tool/
3) cd InstaGram-Tool
4) apt install python3
5) apt install tor
6) tor --hash-password (yourpassword)
7) nano /etc/tor/torrc
8) past 
ControlPort 9051
HashedControlPassword (passhash)
CookieAuthentication 1
9) service tor start
10) pip install -r Requirements.txt
11) python3 Intagram-Tool.py
