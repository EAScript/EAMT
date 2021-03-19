from EAMT import MT4Client
from EnumObjects import *

client = MT4Client(True)

client.Connect(8222)


#sub,time,price = client.ChartXYToTimePrice(132599478980016195,100,100)




