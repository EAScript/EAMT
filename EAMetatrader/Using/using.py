import sys
import clr
import datetime

__author__    = 'Dr.ehsanakbari.programmer@gmail.com'
__copyright__ = 'MIT (2021)'
__version__   = '1.0.0'

class Datetime:
    def __init__(self):
        sys.path.append(r"EAMetatrader\Using")
        clr.AddReference("WindowsBase")
        from System import DateTime
        self._DateTime = DateTime

    def datetime(self,year,month,day,hour=0,minute=0,second=0):
        try:
            return self._DateTime(year, month, day,hour,minute,second)
        except:
            pass

class MtOrder:

    def __init__(self,Order):
        self._order = Order

    def OpenTime(self):
        return self._order.OpenTime

    def StopLoss(self):
        return self._order.StopLoss

    def TakeProfit(self):
        return self._order.TakeProfit

    def MtExpiration(self):
        return self._order.MtExpiration

    def Swap(self):
        return self._order.Swap

    def MagicNumber(self):
        return self._order.MagicNumber

    def Commission(self):
        return self._order.Commission

    def Comment(self):
        return self._order.Comment

    def Profit(self):
        return self._order.Profit

    def MtCloseTime(self):
        return self._order.MtCloseTime

    def MtOpenTime(self):
        return self._order.MtOpenTime

    def Lots(self):
        return self._order.Lots

    def ClosePrice(self):
        return self._order.ClosePrice

    def OpenPrice(self):
        return self._order.OpenPrice

    def Operation(self):
        return self._order.Operation

    def Symbol(self):
        return self._order.Symbol

    def Ticket(self):
        return self._order.Ticket

    def CloseTime(self):
        return self._order.CloseTime

    def Expiration(self):
        return self._order.Expiration

class MtOrders:

    def __init__(self,Orders):
        self._orders = Orders

    def OpenTime(self,index=0):
        try:
            return self._orders[index].OpenTime
        except:
            return False

    def StopLoss(self,index=0):
        try:
            return self._orders[index].StopLoss
        except:
            return False

    def TakeProfit(self,index=0):
        try:
            return self._orders[index].TakeProfit
        except:
            return False

    def MtExpiration(self,index=0):
        try:
            return self._orders[index].MtExpiration
        except:
            return False

    def Swap(self,index=0):
        try:
            return self._orders[index].Swap
        except:
            return False

    def MagicNumber(self,index=0):
        try:
            return self._orders[index].MagicNumber
        except:
            return False

    def Commission(self,index=0):
        try:
            return self._orders[index].Commission
        except:
            return False

    def Comment(self,index=0):
        try:
            return self._orders[index].Comment
        except:
            return False

    def Profit(self,index=0):
        try:
            return self._orders[index].Profit
        except:
            return False

    def MtCloseTime(self,index=0):
        try:
            return self._orders[index].MtCloseTime
        except:
            return False

    def MtOpenTime(self,index=0):
        try:
            return self._orders[index].MtOpenTime
        except:
            return False

    def Lots(self,index=0):
        try:
            return self._orders[index].Lots
        except:
            return False

    def ClosePrice(self,index=0):
        try:
            return self._orders[index].ClosePrice
        except:
            return False

    def OpenPrice(self,index=0):
        try:
            return self._orders[index].OpenPrice
        except:
            return False

    def Operation(self,index=0):
        try:
            return self._orders[index].Operation
        except:
            return False

    def Symbol(self,index=0):
        try:
            return self._orders[index].Symbol
        except:
            return False

    def Ticket(self,index=0):
        try:
            return self._orders[index].Ticket
        except:
            return False

    def CloseTime(self,index=0):
        try:
            return self._orders[index].CloseTime
        except:
            return False

    def Expiration(self,index=0):
        try:
            return self._orders[index].Expiration
        except:
            return False

class MqlRates:

    def __init__(self,Rates):
        self._rates = Rates

    def MtTime(self,index=0):
        try:
            return self._rates[index].MtTime
        except:
            return False

    def Time(self,index=0):
        try:
            time = self._rates[index].Time
            out = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return out
        except:
            return False

    def Open(self,index=0):
        try:
            return self._rates[index].Open
        except:
            return False

    def High(self,index=0):
        try:
            return self._rates[index].High
        except:
            return False

    def Low(self,index=0):
        try:
            return self._rates[index].Low
        except:
            return False

    def Close(self,index=0):
        try:
            return self._rates[index].Close
        except:
            return False

    def TickVolume(self,index=0):
        try:
            return self._rates[index].TickVolume
        except:
            return False

    def Spread(self,index=0):
        try:
            return self._rates[index].Spread
        except:
            return False

    def RealVolume(self,index=0):
        try:
            return self._rates[index].RealVolume
        except:
            return False

class Color:

    def __init__(self):
        sys.path.append(r"EAMetatrader\Using")
        clr.AddReference("System.Drawing")
        from System.Drawing import Color
        self._Color = Color

    def Blue(self):
        return self._Color.Blue

    def Red(self):
        return self._Color.Red

    def White(self):
        return self._Color.White

    def Yellow(self):
        return self._Color.Yellow

    def Green(self):
        return self._Color.Green

    def Gold(self):
        return self._Color.Gold

    def Gray(self):
        return self._Color.Gray

    def Black(self):
        return self._Color.Black

    def Brown(self):
        return self._Color.Brown

    def Cyan(self):
        return self._Color.Cyan

    def Lime(self):
        return self._Color.Lime

    def Orange(self):
        return self._Color.Orange

    def FromArgb(self,red,green,blue):
        return self._Color.FromArgb(red,green,blue)

class MtSession:

    def __init__(self,Session):
        self._Session = Session

    def Symbol(self):
        return self._Session.Symbol

    def DayOfWeek(self):
        return self._Session.DayOfWeek

    def Index(self):
        return self._Session.Index

    def MtFromTime(self):
        return self._Session.MtFromTime

    def From(self):
        time = self._Session.From
        return datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)

    def MtToTime(self):
        return self._Session.MtToTime

    def To(self):
        time = self._Session.To
        return datetime.datetime(time.Year, time.Month, time.Day, time.Hour, time.Minute, time.Second)

    def HasData(self):
        return self._Session.HasData

    def Type(self):
        return self._Session.Type

class MqlTick:

    def __init__(self,Tick):
        self._Tick = Tick

    def MtTime(self):
        return self._Tick.MtTime

    def Time(self):
        time = self._Tick.Time
        return datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)

    def Bid(self):
        return self._Tick.Bid

    def Ask(self):
        return self._Tick.Ask

    def Last(self):
        return self._Tick.Last

    def Volume(self):
        return self._Tick.Volume

class MtQuote:

    def __init__(self,Quote):
        self.quote = Quote

    def Instrument(self,index=0):
        try:
            return self.quote[index].Instrument
        except:
            return False

    def Bid(self,index=0):
        try:
            return self.quote[index].Bid
        except:
            return False

    def Ask(self,index=0):
        try:
            return self.quote[index].Ask
        except:
            return False

    def ExpertHandle(self,index=0):
        try:
            return self.quote[index].ExpertHandle
        except:
            return False
