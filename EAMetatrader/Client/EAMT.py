import os
import time
from ..Enums import *
from ..Using import *

__author__    = 'Dr.ehsanakbari.programmer@gmail.com'
__copyright__ = 'MIT (2021)'
__version__   = '1.0.0'

#TODO
#-----------------------------
# Test & Debug MT4Client
# debug On Array Indicators / ObjectGetValueByTime / TextSetFont
# Crate Pypi Package
# MT5Client Class

DateTime = Datetime()

class MT4Client:

    def __init__(self,LOG=False):
        #sys.path.append(r"EAMetatrader\Client")
        clr.AddReference(os.path.dirname(os.path.abspath(__file__))+"\MtApi")
        import MtApi as mt
        self._client = mt.MtApiClient()
        self.log = LOG

    def Connect(self,port,ip='127.0.01'):
        try:
            for i in range(10):
                if self.log: print('  [{}] Connecting '.format(i), end='')
                self._client.BeginConnect(ip,port)
                time.sleep(1)

                if self._client.ConnectionState == 0:
                    if self.log: print('Disconnected');  continue;
                if self._client.ConnectionState == 1:
                    if self.log: print('.', end='');     continue;
                if self._client.ConnectionState == 2:
                    if self.log: print('OK');            return True
                if self._client.ConnectionState == 3:
                    if self.log: print('FAILED');        return False

        except Exception as e:
            if self.log: print(e)
            return False

    def Disconnect(self):
        try:
            self._client.BeginDisconnect()
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def AccountBalance(self):
        try:
            return self._client.AccountBalance()
        except Exception as e:
            if self.log: print(e)

    def AccountCompany(self):
        try:
            return self._client.AccountCompany()
        except Exception as e:
            if self.log: print(e)

    def AccountCredit(self):
        try:
            return self._client.AccountCredit()
        except Exception as e:
            if self.log: print(e)

    def AccountCurrency(self):
        try:
            return self._client.AccountCurrency()
        except Exception as e:
            if self.log: print(e)

    def AccountEquity(self):
        try:
            return self._client.AccountEquity()
        except Exception as e:
            if self.log: print(e)

    def AccountFreeMargin(self):
        try:
            return self._client.AccountFreeMargin()
        except Exception as e:
            if self.log: print(e)

    def AccountFreeMarginCheck(self,symbol,TradeOperation,volume):
        try:
            return self._client.AccountFreeMarginCheck(symbol,TradeOperation,volume)
        except Exception as e:
            if self.log: print(e)

    def AccountFreeMarginMode(self):
        try:
            return self._client.AccountFreeMarginMode()
        except Exception as e:
            if self.log: print(e)

    def AccountLeverage(self):
        try:
            return self._client.AccountLeverage()
        except Exception as e:
            if self.log: print(e)

    def AccountMargin(self):
        try:
            return self._client.AccountMargin()
        except Exception as e:
            if self.log: print(e)

    def AccountName(self):
        try:
            return self._client.AccountName()
        except Exception as e:
            if self.log: print(e)

    def AccountNumber(self):
        try:
            return self._client.AccountNumber()
        except Exception as e:
            if self.log: print(e)

    def AccountProfit(self):
        try:
            return self._client.AccountProfit()
        except Exception as e:
            if self.log: print(e)

    def AccountServer(self):
        try:
            return self._client.AccountServer()
        except Exception as e:
            if self.log: print(e)

    def AccountStopoutLevel(self):
        try:
            return self._client.AccountStopoutLevel()
        except Exception as e:
            if self.log: print(e)

    def AccountStopoutMode(self):
        try:
            return self._client.AccountStopoutMode()
        except Exception as e:
            if self.log: print(e)

    def Alert(self,message):
        try:
            self._client.Alert(message)
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def ChangeAccount(self,login,password,host):
        try:
            return self._client.ChangeAccount(str(login),str(password),str(host))
        except Exception as e:
            if self.log: print(e)

    def ChartApplyTemplate(self,ChartId,filename):
        try:
            return self._client.ChartApplyTemplate(ChartId,filename)
        except Exception as e:
            if self.log: print(e)

    def ChartClose(self,ChartId):
        try:
            return self._client.ChartClose(ChartId)
        except Exception as e:
            if self.log: print(e)

    def ChartFirst(self):
        try:
            return self._client.ChartFirst()
        except Exception as e:
            if self.log: print(e)

    def ChartGetDouble(self,ChartId,EnumChartPropertyDouble,subWindow=0):
        try:
            return self._client.ChartGetDouble(ChartId,EnumChartPropertyDouble,subWindow)
        except Exception as e:
            if self.log: print(e)

    def ChartGetInteger(self,ChartId,EnumChartPropertyInteger,subWindow=0):
        try:
            return self._client.ChartGetInteger(ChartId,EnumChartPropertyInteger,subWindow)
        except Exception as e:
            if self.log: print(e)

    def ChartGetString(self,ChartId,EnumChartPropertyString):
        try:
            return self._client.ChartGetString(ChartId,EnumChartPropertyString)
        except Exception as e:
            if self.log: print(e)

    def ChartId(self):
        try:
            return self._client.ChartId()
        except Exception as e:
            if self.log: print(e)

    def ChartIndicatorDelete(self,ChartId,SubWindow,indicatorShortname):
        try:
            return self._client.ChartIndicatorDelete(ChartId,SubWindow,indicatorShortname)
        except Exception as e:
            if self.log: print(e)

    def ChartIndicatorName(self,ChartId,SubWindow,index):
        try:
            return self._client.ChartIndicatorName(ChartId,SubWindow,index)
        except Exception as e:
            if self.log: print(e)

    def ChartIndicatorsTotal(self,ChartId,SubWindow):
        try:
            return self._client.ChartIndicatorsTotal(ChartId,SubWindow)
        except Exception as e:
            if self.log: print(e)

    def ChartNavigate(self,ChartId,ENUM_CHART_POSITION,shift=0):
        try:
            return self._client.ChartNavigate(ChartId,ENUM_CHART_POSITION,shift)
        except Exception as e:
            if self.log: print(e)

    def ChartNext(self,ChartId):
        try:
            return self._client.ChartNext(ChartId)
        except Exception as e:
            if self.log: print(e)

    def ChartOpen(self,symbol,ENUM_TIMEFRAMES):
        try:
            return self._client.ChartOpen(symbol,ENUM_TIMEFRAMES)
        except Exception as e:
            if self.log: print(e)

    def ChartPeriod(self,ChartId):
        try:
            return self._client.ChartPeriod(ChartId)
        except Exception as e:
            if self.log: print(e)

    def ChartPriceOnDropped(self):
        try:
            return self._client.ChartPriceOnDropped()
        except Exception as e:
            if self.log: print(e)

    def ChartRedraw(self,ChartId=0):
        try:
            self._client.ChartRedraw(ChartId)
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def ChartSaveTemplate(self,ChartId,filename):
        try:
            return self._client.ChartSaveTemplate(ChartId,filename)
        except Exception as e:
            if self.log: print(e)

    def ChartScreenShot(self,ChartId,filename,width,height,_EnumAlignMode = EnumAlignMode.ALIGN_RIGHT):
        try:
            return self._client.ChartScreenShot(ChartId,filename,width,height,_EnumAlignMode)
        except Exception as e:
            if self.log: print(e)

    def ChartSetDouble(self,ChartId,EnumChartPropertyDouble,value):
        try:
            return self._client.ChartSetDouble(ChartId,EnumChartPropertyDouble,value)
        except Exception as e:
            if self.log: print(e)

    def ChartSetInteger(self,ChartId,EnumChartPropertyInteger,value):
        try:
            return self._client.ChartSetInteger(ChartId,EnumChartPropertyInteger,value)
        except Exception as e:
            if self.log: print(e)

    def ChartSetString(self,ChartId,EnumChartPropertyString,value):
        try:
            return self._client.ChartSetString(ChartId,EnumChartPropertyString,str(value))
        except Exception as e:
            if self.log: print(e)

    def ChartSetSymbolPeriod(self,ChartId,symbol,ENUM_TIMEFRAMES):
        try:
            return self._client.ChartSetSymbolPeriod(ChartId,symbol,ENUM_TIMEFRAMES)
        except Exception as e:
            if self.log: print(e)

    def ChartSymbol(self,ChartId):
        try:
            return self._client.ChartSymbol(ChartId)
        except Exception as e:
            if self.log: print(e)

    def ChartTimeOnDropped(self):
        try:
            time = self._client.ChartTimeOnDropped()
            out = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def ChartTimePriceToXY(self,ChartId,subWindow,Time,price):
        try:
            _x = 0
            _y = 0
            settime = DateTime.datetime(Time.year,Time.month,Time.day,Time.hour,Time.minute,Time.second)
            XY = self._client.ChartTimePriceToXY(ChartId,subWindow,settime,price,_x,_y)
            return XY
        except Exception as e:
            if self.log: print(e)

    def ChartWindowFind(self,ChartId,indicatorShortname):
        try:
            return self._client.ChartWindowFind(ChartId,indicatorShortname)
        except Exception as e:
            if self.log: print(e)

    def ChartWindowOnDropped(self):
        try:
            return self._client.ChartWindowOnDropped()
        except Exception as e:
            if self.log: print(e)

    def ChartXOnDropped(self):
        try:
            return self._client.ChartXOnDropped()
        except Exception as e:
            if self.log: print(e)

    def ChartXYToTimePrice(self,ChartId,x,y):
        try:
            subWindow = 0
            time = DateTime.datetime(1970,1,1)
            price = 0.0
            out = self._client.ChartXYToTimePrice(ChartId,x,y,subWindow,time,price)
            time = datetime.datetime(out[2].Year,out[2].Month,out[2].Day,out[2].Hour,out[2].Minute,out[2].Second)
            return (out[0],out[1],time,out[3])
        except Exception as e:
            if self.log: print(e)

    def ChartYOnDropped(self):
        try:
            return self._client.ChartYOnDropped()
        except Exception as e:
            if self.log: print(e)

    def Comment(self,message):
        try:
            self._client.Comment(message)
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def CopyRates(self,symbolName,ENUM_TIMEFRAMES,startPos,count):
        pass

    def CopyRates(self,symbolName,ENUM_TIMEFRAMES,startTime,count):
        pass

    def CopyRates(self,symbolName,ENUM_TIMEFRAMES,startTime,stopTime):
        try:
            if type(startTime) == int and type(stopTime) == int:
                Rates = self._client.CopyRates(symbolName,ENUM_TIMEFRAMES,startTime,stopTime)
                out = MqlRates(Rates)
                return out
            elif type(startTime) == datetime.datetime and type(stopTime) == int:
                _starttime = DateTime.datetime(startTime.year,startTime.month,startTime.day,startTime.hour,startTime.minute,startTime.second)
                Rates = self._client.CopyRates(symbolName,ENUM_TIMEFRAMES,_starttime,stopTime)
                out = MqlRates(Rates)
                return out
            elif type(startTime) == datetime.datetime and type(stopTime) == datetime.datetime:
                _starttime = DateTime.datetime(startTime.year,startTime.month,startTime.day,startTime.hour,startTime.minute,startTime.second)
                _stoptime = DateTime.datetime(stopTime.year,stopTime.month,stopTime.day,stopTime.hour,stopTime.minute,stopTime.second)
                Rates = self._client.CopyRates(symbolName,ENUM_TIMEFRAMES,_starttime,_stoptime)
                out = MqlRates(Rates)
                return out
            else:
                return False
        except Exception as e:
            if self.log: print(e)

    def Day(self):
        try:
            return self._client.Day()
        except Exception as e:
            if self.log: print(e)

    def DayOfWeek(self):
        try:
            return self._client.DayOfWeek()
        except Exception as e:
            if self.log: print(e)

    def DayOfYear(self):
        try:
            return self._client.DayOfYear()
        except Exception as e:
            if self.log: print(e)

    def ErrorDescription(self,errorCode):
        try:
            return self._client.ErrorDescription(errorCode)
        except Exception as e:
            if self.log: print(e)

    def GetLastError(self):
        try:
            return self._client.GetLastError()
        except Exception as e:
            if self.log: print(e)

    def GetOrder(self,index,OrderSelectMode,OrderSelectSource):
        try:
            order = self._client.GetOrder(index,OrderSelectMode,OrderSelectSource)
            return MtOrder(order)
        except Exception as e:
            if self.log: print(e)
            return False

    def GetOrders(self,OrderSelectSource):
        try:
            orders = self._client.GetOrders(OrderSelectSource)
            return MtOrders(orders)
        except Exception as e:
            if self.log: print(e)

    def GetQuotes(self):
        try:
            quotes = self._client.GetQuotes()
            return MtQuote(quotes)
        except Exception as e:
            if self.log: print(e)

    def GetTickCount(self):
        try:
            return self._client.GetTickCount()
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableCheck(self,name):
        try:
            return self._client.GlobalVariableCheck(name)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableDel(self,name):
        try:
            return self._client.GlobalVariableDel(name)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableGet(self,name):
        try:
            return self._client.GlobalVariableGet(name)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableName(self,index):
        try:
            return self._client.GlobalVariableName(index)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariablesDeleteAll(self,prefixName):
        try:
            return self._client.GlobalVariablesDeleteAll(prefixName)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableSet(self,name,value):
        try:
            time = self._client.GlobalVariableSet(name,value)
            _time = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return _time
        except Exception as e:
            if self.log: print(e)

    def GlobalVariableSetOnCondition(self,name,value,checkValue):
        try:
            return self._client.GlobalVariableSetOnCondition(name,value,checkValue)
        except Exception as e:
            if self.log: print(e)

    def GlobalVariablesTotal(self):
        try:
            return self._client.GlobalVariablesTotal()
        except Exception as e:
            if self.log: print(e)

    def Hour(self):
        try:
            return self._client.Hour()
        except Exception as e:
            if self.log: print(e)

    def iAC(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iAC(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iAD(self,symbol,timeframe,shift):
        try:
            return self._client.iAD(symbol,timeframe,shift)
        except Exception as e:
            if self.log: print(e)

    def iADX(self,symbol,timeframe,period,appliedPrice,mode,shift):
        try:
            return self._client.iADX(symbol,timeframe,period,appliedPrice,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iAlligator(self,symbol,timeframe,jawPeriod,jawShift,teethPeriod,teethShift,lipsPeriod,lipsShift,maMethod,appliedPrice,mode,shift):
        try:
            return self._client.iAlligator(symbol,timeframe,jawPeriod,jawShift,teethPeriod,teethShift,lipsPeriod,lipsShift,maMethod,appliedPrice,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iAO(self,symbol,timeframe,shift):
        try:
            return self._client.iAO(symbol,timeframe,shift)
        except Exception as e:
            if self.log: print(e)

    def iATR(self,symbol,timeframe,period,shift):
        try:
            return self._client.iATR(symbol,timeframe,period,shift)
        except Exception as e:
            if self.log: print(e)

    def iBands(self,symbol,timeframe,period,deviation,bandsShift,appliedPrice,mode,shift):
        try:
            return self._client.iBands(symbol,timeframe,period,deviation,bandsShift,appliedPrice,mode,shift)
        except Exception as e:
            if self.log: print(e)

#    def iBandsOnArray(self,array,total,period,deviation,bandsShift,mode,shift):
#        try:
#            return self._client.iBandsOnArray(array,total,period,deviation,bandsShift,mode,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iBars(self,symbol,ChartPeriod):
        try:
            return self._client.iBars(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iBarShift(self,symbol,ChartPeriod,time,exact):
        try:
            _time = DateTime.datetime(time.year,time.month,time.day,time.hour,time.minute,time.second)
            return self._client.iBarShift(symbol,ChartPeriod,_time,exact)
        except Exception as e:
            if self.log: print(e)

    def iBearsPower(self,symbol,timeframe,period,appliedPrice,shift):
        try:
            return self._client.iBearsPower(symbol,timeframe,period,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iBullsPower(self,symbol,timeframe,period,appliedPrice,shift):
        try:
            return self._client.iBullsPower(symbol,timeframe,period,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iBWMFI(self,symbol,timeframe,shift):
        try:
            return self._client.iBWMFI(symbol,timeframe,shift)
        except Exception as e:
            if self.log: print(e)

    def iCCI(self,symbol,timeframe,period,appliedPrice,shift):
        try:
            return self._client.iCCI(symbol,timeframe,period,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

#    def iCCIOnArray(self,array,total,period,shift):
#        try:
#            return self._client.iCCIOnArray(array,total,period,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iClose(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iClose(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iCloseArray(self,symbol,ChartPeriod):
        try:
            return self._client.iCloseArray(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iCustom(self,symbol,timeframe,name,mode,shift):
        pass

    def iCustom(self,symbol,timeframe,name,parameters=None,mode=0,shift=0):
        try:
            if parameters == None:
                return self._client.iCustom(symbol,timeframe,name,mode,shift)
            else:
                return self._client.iCustom(symbol,timeframe,name,parameters,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iDeMarker(self,symbol,timeframe,period,shift):
        try:
            return self._client.iDeMarker(symbol,timeframe,period,shift)
        except Exception as e:
            if self.log: print(e)

    def iEnvelopes(self,symbol,timeframe,maPeriod,maMethod,maShift,appliedPrice,deviation,mode,shift):
        try:
            return self._client.iEnvelopes(symbol,timeframe,maPeriod,maMethod,maShift,appliedPrice,deviation,mode,shift)
        except Exception as e:
            if self.log: print(e)

#    def iEnvelopesOnArray(self,array,total,maPeriod,maMethod,maShift,deviation,mode,shift):
#        try:
#            return self._client.iEnvelopesOnArray(array,total,maPeriod,maMethod,maShift,deviation,mode,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iForce(self,symbol,timeframe,period,maMethod,appliedPrice,shift):
        try:
            return self._client.iForce(symbol,timeframe,period,maMethod,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iFractals(self,symbol,timeframe,mode,shift):
        try:
            return self._client.iFractals(symbol,timeframe,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iGator(self,symbol,timeframe,jawPeriod,jawShift,teethPeriod,teethShift,lipsPeriod,lipsShift,maMethod,appliedPrice,mode,shift):
        try:
            return self._client.iGator(symbol,timeframe,jawPeriod,jawShift,teethPeriod,teethShift,lipsPeriod,lipsShift,maMethod,appliedPrice,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iHigh(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iHigh(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iHighArray(self,symbol,ChartPeriod):
        try:
            return self._client.iHighArray(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iHighest(self,symbol,ChartPeriod,SeriesIdentifier,count,start):
        try:
            return self._client.iHighest(symbol,ChartPeriod,SeriesIdentifier,count,start)
        except Exception as e:
            if self.log: print(e)

    def iIchimoku(self,symbol,timeframe,tenkanSen,kijunSen,senkouSpanB,mode,shift):
        try:
            return self._client.iIchimoku(symbol,timeframe,tenkanSen,kijunSen,senkouSpanB,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iLow(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iLow(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iLowArray(self,symbol,ChartPeriod):
        try:
            return self._client.iLowArray(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iLowest(self,symbol,ChartPeriod,SeriesIdentifier,count,start):
        try:
            return self._client.iLowest(symbol,ChartPeriod,SeriesIdentifier,count,start)
        except Exception as e:
            if self.log: print(e)

    def iMA(self,symbol,timeframe,period,maShift,maMethod,appliedPrice,shift):
        try:
            return self._client.iMA(symbol,timeframe,period,maShift,maMethod,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iMACD(self,symbol,timeframe,fastEmaPeriod,slowEmaPeriod,signalPeriod,appliedPrice,mode,shift):
        try:
            return self._client.iMACD(symbol,timeframe,fastEmaPeriod,slowEmaPeriod,signalPeriod,appliedPrice,mode,shift)
        except Exception as e:
            if self.log: print(e)

#    def iMAOnArray(self,array,total,period,maShift,maMethod,shift):
#        try:
#            return self._client.iMAOnArray(array,total,period,maShift,maMethod,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iMFI(self,symbol,timeframe,period,shift):
        try:
            return self._client.iMFI(symbol,timeframe,period,shift)
        except Exception as e:
            if self.log: print(e)

    def iMomentum(self,symbol,timeframe,period,appliedPrice,shift):
        try:
            return self._client.iMomentum(symbol,timeframe,period,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

#    def iMomentumOnArray(self,array,total,period,shift):
#        try:
#            return self._client.iMomentumOnArray(array,total,period,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iOBV(self,symbol,timeframe,appliedPrice,shift):
        try:
            return self._client.iOBV(symbol,timeframe,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iOpen(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iOpen(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iOpenArray(self,symbol,ChartPeriod):
        try:
            return self._client.iOpenArray(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iOsMA(self,symbol,timeframe,fastEmaPeriod,slowEmaPeriod,signalPeriod,appliedPrice,shift):
        try:
            return self._client.iOsMA(symbol,timeframe,fastEmaPeriod,slowEmaPeriod,signalPeriod,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

    def iRSI(self,symbol,timeframe,period,appliedPrice,shift):
        try:
            return self._client.iRSI(symbol,timeframe,period,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

#    def iRSIOnArray(self,array,total,period,shift):
#        try:
#            return self._client.iRSIOnArray(array,total,period,shift)
#        except Exception as e:
#            if self.log: print(e)

    def iRVI(self,symbol,timeframe,period,mode,shift):
        try:
            return self._client.iRVI(symbol,timeframe,period,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def iSAR(self,symbol,timeframe,step,maximum,shift):
        try:
            return self._client.iSAR(symbol,timeframe,step,maximum,shift)
        except Exception as e:
            if self.log: print(e)

    def IsConnected(self):
        try:
            return self._client.IsConnected()
        except Exception as e:
            if self.log: print(e)

    def IsDemo(self):
        try:
            return self._client.IsDemo()
        except Exception as e:
            if self.log: print(e)

    def IsDllsAllowed(self):
        try:
            return self._client.IsDllsAllowed()
        except Exception as e:
            if self.log: print(e)

    def IsExpertEnabled(self):
        try:
            return self._client.IsExpertEnabled()
        except Exception as e:
            if self.log: print(e)

    def IsLibrariesAllowed(self):
        try:
            return self._client.IsLibrariesAllowed()
        except Exception as e:
            if self.log: print(e)

    def IsOptimization(self):
        try:
            return self._client.IsOptimization()
        except Exception as e:
            if self.log: print(e)

    def IsStopped(self):
        try:
            return self._client.IsStopped()
        except Exception as e:
            if self.log: print(e)

    def iStdDev(self,symbol,timeframe,maPeriod,maShift,maMethod,appliedPrice,shift):
        try:
            return self._client.iStdDev(symbol,timeframe,maPeriod,maShift,maMethod,appliedPrice,shift)
        except Exception as e:
            if self.log: print(e)

#    def iStdDevOnArray(self,array,total,maPeriod,maShift,maMethod,shift):
#        try:
#            return self._client.iStdDevOnArray(array,total,maPeriod,maShift,maMethod,shift)
#        except Exception as e:
#            if self.log: print(e)

    def IsTesting(self):
        try:
            return self._client.IsTesting()
        except Exception as e:
            if self.log: print(e)

    def iStochastic(self,symbol,timeframe,pKperiod,pDperiod,slowing,method,priceField,mode,shift):
        try:
            return self._client.iStochastic(symbol,timeframe,pKperiod,pDperiod,slowing,method,priceField,mode,shift)
        except Exception as e:
            if self.log: print(e)

    def IsTradeAllowed(self):
        try:
            return self._client.IsTradeAllowed()
        except Exception as e:
            if self.log: print(e)

    def IsTradeContextBusy(self):
        try:
            return self._client.IsTradeContextBusy()
        except Exception as e:
            if self.log: print(e)

    def IsVisualMode(self):
        try:
            return self._client.IsVisualMode()
        except Exception as e:
            if self.log: print(e)

    def iTime(self,symbol,ChartPeriod,shift):
        try:
            time = self._client.iTime(symbol,ChartPeriod,shift)
            out = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def iTimeArray(self,symbol,ChartPeriod):
        try:
            times = self._client.iTimeArray(symbol,ChartPeriod)
            array = []
            for time in times:
                array.append(datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second))
            return array
        except Exception as e:
            if self.log: print(e)

    def iVolume(self,symbol,ChartPeriod,shift):
        try:
            return self._client.iVolume(symbol,ChartPeriod,shift)
        except Exception as e:
            if self.log: print(e)

    def iVolumeArray(self,symbol,ChartPeriod):
        try:
            return self._client.iVolumeArray(symbol,ChartPeriod)
        except Exception as e:
            if self.log: print(e)

    def iWPR(self,symbol,timeframe,period,shift):
        try:
            return self._client.iWPR(symbol,timeframe,period,shift)
        except Exception as e:
            if self.log: print(e)

    def MarketInfo(self,symbol,MarketInfoModeType):
        try:
            return self._client.MarketInfo(symbol,MarketInfoModeType)
        except Exception as e:
            if self.log: print(e)

    def MessageBox(self,text):
        pass

    def MessageBox(self,text,caption):
        pass

    def MessageBox(self,text,caption=None,flag=None):
        try:
            if caption == None and flag == None:
                return self._client.MessageBox(text)
            elif flag == None:
                return self._client.MessageBox(text,caption)
            else:
                return self._client.MessageBox(text,caption,flag)
        except Exception as e:
            if self.log: print(e)

    def Minute(self):
        try:
            return self._client.Minute()
        except Exception as e:
            if self.log: print(e)

    def Month(self):
        try:
            return self._client.Month()
        except Exception as e:
            if self.log: print(e)

    def ObjectCreate(self,ChartId,objectName,EnumObject,subWindow,time1,price1,time2 = None,price2 = None,time3 = None,price3 = None):
        try:
            if time2 == None and time3 == None:
                _time1 = DateTime.datetime(time1.year,time1.month,time1.day,time1.hour,time1.minute,time1.second)
                return self._client.ObjectCreate(ChartId,objectName,EnumObject,subWindow,_time1,price1,time2,price2,time3,price3)
            elif time3 == None:
                _time1 = DateTime.datetime(time1.year,time1.month,time1.day,time1.hour,time1.minute,time1.second)
                _time2 = DateTime.datetime(time2.year,time2.month,time2.day,time2.hour,time2.minute,time2.second)
                return self._client.ObjectCreate(ChartId,objectName,EnumObject,subWindow,_time1,price1,_time2,price2,time3,price3)
            else:
                _time1 = DateTime.datetime(time1.year,time1.month,time1.day,time1.hour,time1.minute,time1.second)
                _time2 = DateTime.datetime(time2.year,time2.month,time2.day,time2.hour,time2.minute,time2.second)
                _time3 = DateTime.datetime(time3.year,time3.month,time3.day,time3.hour,time3.minute,time3.second)
                return self._client.ObjectCreate(ChartId,objectName,EnumObject,subWindow,_time1,price1,_time2,price2,_time3,price3)
        except Exception as e:
            if self.log: print(e)

    def ObjectDelete(self,ChartId,objectName):
        try:
            return self._client.ObjectDelete(ChartId,objectName)
        except Exception as e:
            if self.log: print(e)

    def ObjectDescription(self,objectName):
        try:
            return self._client.ObjectDescription(objectName)
        except Exception as e:
            if self.log: print(e)

    def ObjectFind(self,ChartId,objectName):
        try:
            return self._client.ObjectFind(ChartId,objectName)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetDouble(self,ChartId,objectName,EnumObjectPropertyDouble,propModifier = 0):
        try:
            return self._client.ObjectGetDouble(ChartId,objectName,EnumObjectPropertyDouble,propModifier)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetFiboDescription(self,objectName,index):
        try:
            return self._client.ObjectGetFiboDescription(objectName,index)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetInteger(self,ChartId,objectName,EnumObjectPropertyInteger,propModifier = 0):
        try:
            return self._client.ObjectGetInteger(ChartId,objectName,EnumObjectPropertyInteger,propModifier)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetShiftByValue(self,objectName,value):
        try:
            return self._client.ObjectGetShiftByValue(objectName,value)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetString(self,ChartId,objectName,EnumObjectPropertyString,propModifier = 0):
        try:
            return self._client.ObjectGetString(ChartId,objectName,EnumObjectPropertyString,propModifier)
        except Exception as e:
            if self.log: print(e)

    def ObjectGetTimeByValue(self,ChartId,objectName,value,lineId = 0):
        try:
            time = self._client.ObjectGetTimeByValue(ChartId,objectName,value,lineId)
            out = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def ObjectGetValueByShift(self,objectName,shift):
        try:
            return self._client.ObjectGetValueByShift(objectName,shift)
        except Exception as e:
            if self.log: print(e)

#    def ObjectGetValueByTime(self,ChartId,objectName,time,lineId = 0):
#        try:
#            settime = DateTime.datetime(time.year,time.month,time.day,time.hour,time.minute,time.second)
#            return self._client.ObjectGetValueByTime(ChartId,objectName,settime,lineId)
#        except Exception as e:
#            if self.log: print(e)

    def ObjectMove(self,ChartId,objectName,pointIndex,time,price):
        try:
            _time = DateTime.datetime(time.year,time.month,time.day,time.hour,time.minute,time.second)
            return self._client.ObjectMove(ChartId,objectName,pointIndex,_time,price)
        except Exception as e:
            if self.log: print(e)

    def ObjectName(self,ChartId,objectIndex,subWindow = -1,objectType = -1):
        try:
            return self._client.ObjectName(ChartId,objectIndex,subWindow,objectType)
        except Exception as e:
            if self.log: print(e)

    def ObjectsDeleteAll(self,ChartId,subWindow = -1,objectType = -1):
        try:
            return self._client.ObjectsDeleteAll(ChartId,subWindow,objectType)
        except Exception as e:
            if self.log: print(e)

    def ObjectSet(self,objectName,index,value):
        try:
            return self._client.ObjectSet(objectName,index,value)
        except Exception as e:
            if self.log: print(e)

    def ObjectSetDouble(self,ChartId,objectName,EnumObjectPropertyDouble,propValue):
        pass

    def ObjectSetDouble(self,ChartId,objectName,EnumObjectPropertyDouble,propValue,propModifier=None):
        try:
            if propModifier == None:
                return self._client.ObjectSetDouble(ChartId, objectName, EnumObjectPropertyDouble, propValue)
            else:
                return self._client.ObjectSetDouble(ChartId,objectName,EnumObjectPropertyDouble,propModifier,propValue)
        except Exception as e:
            if self.log: print(e)

    def ObjectSetFiboDescription(self,objectName,index,text):
        try:
            return self._client.ObjectSetFiboDescription(objectName,index,text)
        except Exception as e:
            if self.log: print(e)

    def ObjectSetInteger(self,ChartId,objectName,EnumObjectPropertyInteger,propValue):
        pass

    def ObjectSetInteger(self,ChartId,objectName,EnumObjectPropertyInteger,propValue,propModifier=None):
        try:
            if propModifier == None:
                return self._client.ObjectSetInteger(ChartId, objectName, EnumObjectPropertyInteger, propValue)
            else:
                return self._client.ObjectSetInteger(ChartId,objectName,EnumObjectPropertyInteger,propModifier,propValue)
        except Exception as e:
            if self.log: print(e)

    def ObjectSetString(self,ChartId,objectName,EnumObjectPropertyString,propValue):
        pass

    def ObjectSetString(self,ChartId,objectName,EnumObjectPropertyString,propValue,propModifier=None):
        try:
            if propModifier == None:
                return self._client.ObjectSetString(ChartId, objectName, EnumObjectPropertyString, propValue)
            else:
                return self._client.ObjectSetString(ChartId,objectName,EnumObjectPropertyString,propModifier,propValue)
        except Exception as e:
            if self.log: print(e)

    def ObjectSetText(self,objectName,text,fontSize):
        pass

    def ObjectSetText(self,objectName,text,fontSize,fontName):
        pass

    def ObjectSetText(self,objectName,text,fontSize = 12,fontName = None,textColor = None):
        try:
            if fontName == None and textColor == None:
                return self._client.ObjectSetText(objectName,text,fontSize,"Arial")
            elif textColor == None:
                return self._client.ObjectSetText(objectName,text,fontSize,fontName)
            else:
                return self._client.ObjectSetText(objectName,text,fontSize,fontName,textColor)
        except Exception as e:
            if self.log: print(e)

    def ObjectsTotal(self,ChartId,subWindow = -1,type = -1):
        try:
            return self._client.ObjectsTotal(ChartId,subWindow,type)
        except Exception as e:
            if self.log: print(e)

    def ObjectType(self,objectName):
        try:
            return self._client.ObjectType(objectName)
        except Exception as e:
            if self.log: print(e)

    def OrderClose(self,ticket,slippage):
        pass

    def OrderClose(self,ticket,slippage,lots):
        pass

    def OrderClose(self,ticket,slippage,lots,price):
        pass

    def OrderClose(self,ticket,slippage,lots=None,price=None,color=None):
        try:
            if lots == None and price == None and color == None:
                return self._client.OrderClose(ticket,slippage)
            elif price == None and color == None:
                return self._client.OrderClose(ticket,lots,slippage)
            elif color == None:
                return self._client.OrderClose(ticket,lots,price,slippage)
            else:
                return self._client.OrderClose(ticket,lots,price,slippage,color)
        except Exception as e:
            if self.log: print(e)

    def OrderCloseAll(self):
        try:
            return self._client.OrderCloseAll()
        except Exception as e:
            if self.log: print(e)

#    def OrderCloseBy(self,ticket,opposite):
#        pass
#
#    def OrderCloseBy(self,ticket,opposite,color=None):
#        try:
#            if color == None:
#                return self._client.OrderCloseBy(ticket,opposite)
#            else:
#                return self._client.OrderCloseBy(ticket,opposite,color)
#        except Exception as e:
#            if self.log: print(e)

    def OrderCloseByCurrentPrice(self,ticket,slippage):
        try:
            return self._client.OrderCloseByCurrentPrice(ticket,slippage)
        except Exception as e:
            if self.log: print(e)

    def OrderClosePrice(self):
        pass

    def OrderClosePrice(self,ticket=None):
        try:
            if ticket == None:
                return self._client.OrderClosePrice()
            else:
                return self._client.OrderClosePrice(ticket)
        except Exception as e:
            if self.log: print(e)

    def OrderCloseTime(self):
        try:
            time = self._client.OrderCloseTime()
            out = datetime.datetime(time.Year, time.Month, time.Day, time.Hour, time.Minute, time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def OrderComment(self):
        try:
            return self._client.OrderComment()
        except Exception as e:
            if self.log: print(e)

    def OrderCommission(self):
        try:
            return self._client.OrderCommission()
        except Exception as e:
            if self.log: print(e)

    def OrderDelete(self,ticket):
        pass

    def OrderDelete(self,ticket,color=None):
        try:
            if color == None:
                return self._client.OrderDelete(ticket)
            else:
                return self._client.OrderDelete(ticket,color)
        except Exception as e:
            if self.log: print(e)

    def OrderExpiration(self):
        try:
            time = self._client.OrderExpiration()
            out = datetime.datetime(time.Year, time.Month, time.Day, time.Hour, time.Minute, time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def OrderLots(self):
        try:
            return self._client.OrderLots()
        except Exception as e:
            if self.log: print(e)

    def OrderMagicNumber(self):
        try:
            return self._client.OrderMagicNumber()
        except Exception as e:
            if self.log: print(e)

    def OrderModify(self,ticket,price,stoploss,takeprofit):
        pass

    def OrderModify(self,ticket,price,stoploss,takeprofit,expiration):
        pass

    def OrderModify(self,ticket,price,stoploss,takeprofit,expiration=None,arrowColor=None):
        try:
            if expiration == None and arrowColor == None:
                time = DateTime.datetime(1970,1,1)
                return self._client.OrderModify(ticket,price,stoploss,takeprofit,time)
            if arrowColor == None:
                time = DateTime.datetime(expiration.year,expiration.month,expiration.day,expiration.hour,expiration.minute,expiration.second)
                return self._client.OrderModify(ticket,price,stoploss,takeprofit,time)
            else:
                time = DateTime.datetime(expiration.year,expiration.month,expiration.day,expiration.hour,expiration.minute,expiration.second)
                return self._client.OrderModify(ticket,price,stoploss,takeprofit,time,arrowColor)
        except Exception as e:
            if self.log: print(e)

    def OrderOpenPrice(self):
        pass

    def OrderOpenPrice(self,ticket=None):
        try:
            if ticket == None:
                return self._client.OrderOpenPrice()
            else:
                return self._client.OrderOpenPrice(ticket)
        except Exception as e:
            if self.log: print(e)

    def OrderOpenTime(self):
        try:
            time = self._client.OrderOpenTime()
            out = datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
            return out
        except Exception as e:
            if self.log: print(e)

    def OrderPrint(self):
        try:
            self._client.OrderPrint()
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def OrderProfit(self):
        try:
            return self._client.OrderProfit()
        except Exception as e:
            if self.log: print(e)

    def OrderSelect(self,index,OrderSelectMode):
        pass

    def OrderSelect(self,index,OrderSelectMode,OrderSelectSource=None):
        try:
            if OrderSelectSource == None:
                return self._client.OrderSelect(index,OrderSelectMode)
            else:
                return self._client.OrderSelect(index,OrderSelectMode,OrderSelectSource)
        except Exception as e:
            if self.log: print(e)

    def OrderSend(self,symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit):
        pass

    def OrderSend(self,symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment):
        pass

    def OrderSend(self,symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment,magic):
        pass

    def OrderSend(self,symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment,magic,expiration):
        pass

    def OrderSend(self,symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment=None,magic=None,expiration=None,arrowColor=None):
        try:
            if comment == None and magic == None and expiration == None and arrowColor == None:
                return self._client.OrderSend(symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit)
            elif magic == None and expiration == None and arrowColor == None:
                return self._client.OrderSend(symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment)
            elif expiration == None and arrowColor == None:
                return self._client.OrderSend(symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment,magic)
            elif arrowColor == None:
                time = DateTime.datetime(expiration.year,expiration.month,expiration.day,expiration.hour,expiration.minute,expiration.second)
                return self._client.OrderSend(symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment,magic,time)
            else:
                time = DateTime.datetime(expiration.year,expiration.month,expiration.day,expiration.hour,expiration.minute,expiration.second)
                return self._client.OrderSend(symbol,TradeOperation,volume,price,slippage,stoploss,takeprofit,comment,magic,time,arrowColor)
        except Exception as e:
            if self.log: print(e)

    def OrderSendBuy(self,symbol,volume,slippage):
        pass

    def OrderSendBuy(self,symbol,volume,slippage,stoploss,takeprofit):
        pass

    def OrderSendBuy(self,symbol,volume,slippage,stoploss=None,takeprofit=None,comment=None,magic=None):
        try:
            if stoploss == None and takeprofit == None and comment == None and magic == None:
                return self._client.OrderSendBuy(symbol,volume,slippage)
            elif comment == None and magic == None:
                return self._client.OrderSendBuy(symbol,volume,slippage,stoploss,takeprofit)
            else:
                return self._client.OrderSendBuy(symbol,volume,slippage,stoploss,takeprofit,comment,magic)
        except Exception as e:
            if self.log: print(e)

    def OrderSendSell(self,symbol,volume,slippage):
        pass

    def OrderSendSell(self,symbol,volume,slippage,stoploss,takeprofit):
        pass

    def OrderSendSell(self,symbol,volume,slippage,stoploss=None,takeprofit=None,comment=None,magic=None):
        try:
            if stoploss == None and takeprofit == None and comment == None and magic == None:
                return self._client.OrderSendSell(symbol,volume,slippage)
            elif comment == None and magic == None:
                return self._client.OrderSendSell(symbol,volume,slippage,stoploss,takeprofit)
            else:
                return self._client.OrderSendSell(symbol,volume,slippage,stoploss,takeprofit,comment,magic)
        except Exception as e:
            if self.log: print(e)

    def OrdersHistoryTotal(self):
        try:
            return self._client.OrdersHistoryTotal()
        except Exception as e:
            if self.log: print(e)

    def OrderStopLoss(self):
        try:
            return self._client.OrderStopLoss()
        except Exception as e:
            if self.log: print(e)

    def OrdersTotal(self):
        try:
            return self._client.OrdersTotal()
        except Exception as e:
            if self.log: print(e)

    def OrderSwap(self):
        try:
            return self._client.OrderSwap()
        except Exception as e:
            if self.log: print(e)

    def OrderSymbol(self):
        try:
            return self._client.OrderSymbol()
        except Exception as e:
            if self.log: print(e)

    def OrderTakeProfit(self):
        try:
            return self._client.OrderTakeProfit()
        except Exception as e:
            if self.log: print(e)

    def OrderTicket(self):
        try:
            return self._client.OrderTicket()
        except Exception as e:
            if self.log: print(e)

    def OrderType(self):
        try:
            return self._client.OrderType()
        except Exception as e:
            if self.log: print(e)

    def PlaySound(self,filename):
        try:
            return self._client.PlaySound(filename)
        except Exception as e:
            if self.log: print(e)

    def Print(self,message):
        try:
            self._client.Print(message)
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def RefreshRates(self):
        try:
            self._client.RefreshRates()
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def Seconds(self):
        try:
            return self._client.Seconds()
        except Exception as e:
            if self.log: print(e)

    def SendFTP(self,filename):
        pass

    def SendFTP(self,filename,ftpPath=None):
        try:
            if ftpPath == None:
                return self._client.SendFTP(filename)
            else:
                return self._client.SendFTP(filename,ftpPath)
        except Exception as e:
            if self.log: print(e)

    def SendMail(self,subject,someText):
        try:
            return self._client.SendMail(subject,someText)
        except Exception as e:
            if self.log: print(e)

    def SeriesInfoInteger(self,symbolName,ENUM_TIMEFRAMES,EnumSeriesInfoInteger):
        try:
            return self._client.SeriesInfoInteger(symbolName,ENUM_TIMEFRAMES,EnumSeriesInfoInteger)
        except Exception as e:
            if self.log: print(e)

    def Sleep(self,milliseconds):
        try:
            self._client.Sleep(milliseconds)
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def SymbolInfoDouble(self,symbolName,EnumSymbolInfoDouble):
        try:
            return self._client.SymbolInfoDouble(symbolName,EnumSymbolInfoDouble)
        except Exception as e:
            if self.log: print(e)

    def SymbolInfoInteger(self,name,EnumSymbolInfoInteger):
        try:
            return self._client.SymbolInfoInteger(name,EnumSymbolInfoInteger)
        except Exception as e:
            if self.log: print(e)

    def SymbolInfoSession(self,symbol,DayOfWeek,index,SessionType):
        try:
            Session = self._client.SymbolInfoSession(symbol,DayOfWeek,index,SessionType)
            return MtSession(Session)
        except Exception as e:
            if self.log: print(e)

    def SymbolInfoString(self,name,ENUM_SYMBOL_INFO_STRING):
        try:
            return self._client.SymbolInfoString(name,ENUM_SYMBOL_INFO_STRING)
        except Exception as e:
            if self.log: print(e)

    def SymbolInfoTick(self,symbol):
        try:
            Tick = self._client.SymbolInfoTick(symbol)
            return MqlTick(Tick)
        except Exception as e:
            if self.log: print(e)

    def SymbolName(self,pos,selected):
        try:
            return self._client.SymbolName(pos,selected)
        except Exception as e:
            if self.log: print(e)

    def SymbolSelect(self,name,selected):
        try:
            return self._client.SymbolSelect(name,selected)
        except Exception as e:
            if self.log: print(e)

    def SymbolsTotal(self,selected):
        try:
            return self._client.SymbolsTotal(selected)
        except Exception as e:
            if self.log: print(e)

    def TerminalCompany(self):
        try:
            return self._client.TerminalCompany()
        except Exception as e:
            if self.log: print(e)

    def TerminalInfoDouble(self,EnumTerminalInfoDouble):
        try:
            return self._client.TerminalInfoDouble(EnumTerminalInfoDouble)
        except Exception as e:
            if self.log: print(e)

    def TerminalInfoInteger(self,EnumTerminalInfoInteger):
        try:
            return self._client.TerminalInfoInteger(EnumTerminalInfoInteger)
        except Exception as e:
            if self.log: print(e)

    def TerminalInfoString(self,ENUM_TERMINAL_INFO_STRING):
        try:
            return self._client.TerminalInfoString(ENUM_TERMINAL_INFO_STRING)
        except Exception as e:
            if self.log: print(e)

    def TerminalName(self):
        try:
            return self._client.TerminalName()
        except Exception as e:
            if self.log: print(e)

    def TerminalPath(self):
        try:
            return self._client.TerminalPath()
        except Exception as e:
            if self.log: print(e)

#    def TextSetFont(self,name,size,flagfontstyle = FlagFontStyle.FW_DONTCARE,orientation = 0):
#        try:
#            return self._client.TextSetFont(name,size,flagfontstyle,orientation)
#        except Exception as e:
#            if self.log: print(e)

    def TimeCurrent(self):
        try:
            time = self._client.TimeCurrent()
            return datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
        except Exception as e:
            if self.log: print(e)

    def TimeDay(self,date):
        try:
            time = DateTime.datetime(date.year,date.month,date.day,date.hour,date.minute,date.second)
            return self._client.TimeDay(time)
        except Exception as e:
            if self.log: print(e)

    def TimeDayOfWeek(self,date):
        try:
            time = DateTime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
            return self._client.TimeDayOfWeek(time)
        except Exception as e:
            if self.log: print(e)

    def TimeDayOfYear(self,date):
        try:
            time = DateTime.datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)
            return self._client.TimeDayOfYear(time)
        except Exception as e:
            if self.log: print(e)

    def TimeGMT(self):
        try:
            time = self._client.TimeGMT()
            return datetime.datetime(time.Year, time.Month, time.Day, time.Hour, time.Minute, time.Second)
        except Exception as e:
            if self.log: print(e)

    def TimeHour(self,time):
        try:
            _time = DateTime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            return self._client.TimeHour(_time)
        except Exception as e:
            if self.log: print(e)

    def TimeLocal(self):
        try:
            time = self._client.TimeLocal()
            return datetime.datetime(time.Year, time.Month, time.Day, time.Hour, time.Minute, time.Second)
        except Exception as e:
            if self.log: print(e)

    def TimeMinute(self,time):
        try:
            _time = DateTime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            return self._client.TimeMinute(_time)
        except Exception as e:
            if self.log: print(e)

    def TimeMonth(self,time):
        try:
            _time = DateTime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            return self._client.TimeMonth(_time)
        except Exception as e:
            if self.log: print(e)

    def TimeSeconds(self,time):
        try:
            _time = DateTime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            return self._client.TimeSeconds(_time)
        except Exception as e:
            if self.log: print(e)

    def TimeYear(self,time):
        try:
            _time = DateTime.datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            return self._client.TimeYear(_time)
        except Exception as e:
            if self.log: print(e)

    def UninitializeReason(self):
        try:
            return self._client.UninitializeReason()
        except Exception as e:
            if self.log: print(e)

    def UnlockTicks(self):
        try:
            self._client.UnlockTicks()
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def WindowBarsPerChart(self):
        try:
            return self._client.WindowBarsPerChart()
        except Exception as e:
            if self.log: print(e)

    def WindowExpertName(self):
        try:
            return self._client.WindowExpertName()
        except Exception as e:
            if self.log: print(e)

    def WindowFind(self,name):
        try:
            return self._client.WindowFind(name)
        except Exception as e:
            if self.log: print(e)

    def WindowFirstVisibleBar(self):
        try:
            return self._client.WindowFirstVisibleBar()
        except Exception as e:
            if self.log: print(e)

    def WindowHandle(self,symbol,timeframe):
        try:
            return self._client.WindowHandle(symbol,timeframe)
        except Exception as e:
            if self.log: print(e)

    def WindowIsVisible(self,index):
        try:
            return self._client.WindowIsVisible(index)
        except Exception as e:
            if self.log: print(e)

    def WindowOnDropped(self):
        try:
            return self._client.WindowOnDropped()
        except Exception as e:
            if self.log: print(e)

    def WindowPriceMax(self,index = 0):
        try:
            return self._client.WindowPriceMax(index)
        except Exception as e:
            if self.log: print(e)

    def WindowPriceMin(self,index = 0):
        try:
            return self._client.WindowPriceMin(index)
        except Exception as e:
            if self.log: print(e)

    def WindowPriceOnDropped(self):
        try:
            return self._client.WindowPriceOnDropped()
        except Exception as e:
            if self.log: print(e)

    def WindowRedraw(self):
        try:
            self._client.WindowRedraw()
            return True
        except Exception as e:
            if self.log: print(e)
            return False

    def WindowScreenShot(self,filename,sizeX,sizeY,startBar = -1,chartScale = -1,chartMode = -1):
        try:
            return self._client.WindowScreenShot(filename,sizeX,sizeY,startBar,chartScale,chartMode)
        except Exception as e:
            if self.log: print(e)

    def WindowsTotal(self):
        try:
            return self._client.WindowsTotal()
        except Exception as e:
            if self.log: print(e)

    def WindowTimeOnDropped(self):
        try:
            time = self._client.WindowTimeOnDropped()
            return datetime.datetime(time.Year,time.Month,time.Day,time.Hour,time.Minute,time.Second)
        except Exception as e:
            if self.log: print(e)

    def WindowXOnDropped(self):
        try:
            return self._client.WindowXOnDropped()
        except Exception as e:
            if self.log: print(e)

    def WindowYOnDropped(self):
        try:
            return self._client.WindowYOnDropped()
        except Exception as e:
            if self.log: print(e)

    def Year(self):
        try:
            _time = DateTime.datetime(1990,1,1,0,0,0)
            return self._client.Year(_time)
        except Exception as e:
            if self.log: print(e)

class MT5Client:
    pass
