# evga-gpu-bot
![2022-01-21 14-15-03_Trim](https://user-images.githubusercontent.com/42254833/150587298-8335bf0a-c7fa-4e5d-87ed-66fa3565c361.gif)

## Description
A Chrome bot I made for personal use so I can get a GPU during the great GPU crisis of 2019-2022. Let's you specify what GPU you want from EVGA B-stock, and buys the GPU when it comes in stock.

Written in Python using Selenium.

## Installation
If it's been a couple months you hopefully don't need a bot to get a gpu anymore, but to set this up, you need to have Python 3.10 installed as well as downloaded the chrome driver from [here](https://chromedriver.storage.googleapis.com/index.html)

```bash
pip install selenium
```

In order for this to work without your ip getting banned, you need a VPN that autoconnects to a location when it launches, I recommend [Windscribe](https://windscribe.com/). Once you have all of that set up, clone this git repo.

Navigate to the EVGA folder, and open constants.py in a text editor. You will want to change DRIVER_PATH and VPN_PATH to the path of your chrome driver and VPN respectively. 

In the .env file, you will want to fill out your details as well. Keep everything as it is, include spaces, like in your name, and don't include quotation marks. For instance:
Product_ID=01G-P3-1313-RX

You can find the product IDs here in the top left corner of this image
![Screenshot 2022-01-21 143456](https://user-images.githubusercontent.com/42254833/150589369-371fa341-d2c3-4db9-b43c-859da9c29b44.png)

Once this is setup, run the main.py file. 
