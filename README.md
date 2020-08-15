# AdidasBot
Browser automation script for buying adidas shoes and checking restocks

## Prerequisites
selenium module
```
pip install selenium
```

webdriver_manager module
```
pip install webdriver_manager
```

## Setup
1) Clone respository or download zip
```
git clone https://github.com/gdotzheng/AdidasBot.git
```
2) Edit ```details.py``` with autofill credentials 
```
info = {
    'fname': 'test',
    'lname': 'test',
    'address': '123 street',
    'city': 'city',
    'state': 'Pennsylvania', # not abbreviated and capitalize first letter
    'zip': '12345',
    'phone': '1234567890',
    'email': 'test@test.com',
    'cardnumber': '1234567890123456',
    'expiration': '0523',
    'cvv': '123'
}
```

3) Run the script
```
python adidasbot.py
```
