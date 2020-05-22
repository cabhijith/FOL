# FOL
FOL is a bot that repeatedly likes and unlikes a message so as to create a stream of hearts with Instagrams latest update.

## Setup 
```pip install selenium```
Download the [driver](https://chromedriver.chromium.org/) for Chrome (Not tested with Gecko). 

Fill in your username, password and the target username and run ```love.py```. Since this was a one evening project, I just used
```sleep``` to account for browser delays and not proper Selenium wait exceptions. You may have to play around with the durations
based on your internet. 
