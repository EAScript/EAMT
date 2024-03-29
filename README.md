# EAMT
![PyPI](https://img.shields.io/pypi/v/EAMetatrader)![PyPI - Downloads](https://img.shields.io/pypi/dm/EAMetatrader) \
![Python Version](https://img.shields.io/badge/Python%20Version-3.7-blue) \
![OS Support](https://img.shields.io/badge/OS%20Support-WIN--64-lightgrey) \
![GitHub](https://img.shields.io/github/license/EAScript/EAMT) \
![GitHub followers](https://img.shields.io/github/followers/EAScript?style=social)![GitHub User's stars](https://img.shields.io/github/stars/EAScript?style=social)
## Metatrader library for python powered by MtApi
This library currently only supports MetaTrader 4

## Installation
- Install the library with the `pip install EAMetatrader` command
- Copy and run the `MtApi.ex4` file in MetaTrader software
- Set up a `port` in Expert and Application for network connection
- and over
 
### Required libraries
```Python
from EAMetatrader import MT4Client
from EAMetatrader.Enums import *
from EAMetatrader.Using import Color
import datetime
```

### Connection
```Python
client = MT4Client(True)
client.Connect(8222)
```

### Copy Rates
```Python
start = datetime.datetime(2021,3,16)
end = datetime.datetime(2021,3,1)

mqlrate = client.CopyRates("EURUSD",ENUM_TIMEFRAMES.PERIOD_H1,start,end)
print(mqlrate.Time(2))
```

### Indicators
```Python
Symbol = "EURUSD"
Timeframe = 60
Period = 14
Appliedprice = 0  #Close
Shift = 0

RSI = client.iRSI(Symbol,Timeframe,Period,Appliedprice,Shift)
```

### Send Order
```Python
Lot = 0.01
Ask = client.MarketInfo("EURUSD",MarketInfoModeType.MODE_ASK)
SL = Ask - 0.002
TP = Ask + 0.004
Slippage = 5
Comment = "EAMetatrader"
Magic = 2222
Expiration = datetime.datetime(2021,3,25)
color = Color()

Order = client.OrderSend("EURUSD",TradeOperation.OP_BUY,Lot,Ask,Slippage,SL,TP,Comment,Magic,Expiration,color.Green())
```

## TODO
- Debug some functions
- Write MT5Client class
- Development of functions for working with artificial intelligence

## Issues
If you have a question or want to report a bug, send it in this section

## My social medias
[LinkedIn](https://www.linkedin.com/in/ehsan-akbari-0487ba187)

[Instagram](https://instagram.com/ea.forex.programmer)

[YouTube](https://www.youtube.com/channel/UCjoSfFPmcy7makwHFYuHM8Q)

[Github](https://github.com/EAScript)

## Donating

Bitcoin: `13fWKBESm6pqtCQzp3WgBarcmxFNv5aCXf`
<!-- </br><img src="http://eaforexrobot.com/Donate/assets/img/Bitcoin_qr.png" width="320" height="320"> -->

<!-- ## [More Cryptocurrency For Donate ...!](http://eaforexrobot.com/Donate) -->






