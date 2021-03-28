__author__    = 'Dr.ehsanakbari.programmer@gmail.com'
__copyright__ = 'MIT (2021)'
__version__   = '1.0.0'

class TradeOperation:
    OP_BUY = 0
    OP_SELL = 1
    OP_BUYLIMIT = 2
    OP_SELLLIMIT = 3
    OP_BUYSTOP = 4
    OP_SELLSTOP = 5
    OP_BALANCE = 6
    OP_CREDIT = 7
    OP_REBATE = 8

class EnumChartPropertyDouble:
    CHART_SHIFT_SIZE = 3
    CHART_FIXED_MAX = 8
    CHART_FIXED_MIN = 9
    CHART_POINTS_PER_BAR = 11
    CHART_FIXED_POSITION = 41
    CHART_PRICE_MIN = 108
    CHART_PRICE_MAX = 109

class EnumChartPropertyInteger:
    CHART_MODE = 0
    CHART_FOREGROUND = 1
    CHART_SHIFT = 2
    CHART_AUTOSCROLL = 4
    CHART_SCALE = 5
    CHART_SCALEFIX = 6
    CHART_SCALEFIX_11 = 7
    CHART_SCALE_PT_PER_BAR = 10
    CHART_SHOW_OHLC = 12
    CHART_SHOW_BID_LINE = 13
    CHART_SHOW_ASK_LINE = 14
    CHART_SHOW_LAST_LINE = 15
    CHART_SHOW_PERIOD_SEP = 16
    CHART_SHOW_GRID = 17
    CHART_SHOW_VOLUMES = 18
    CHART_SHOW_OBJECT_DESCR = 19
    CHART_COLOR_BACKGROUND = 21
    CHART_COLOR_FOREGROUND = 22
    CHART_COLOR_GRID = 23
    CHART_COLOR_VOLUME = 24
    CHART_COLOR_CHART_UP = 25
    CHART_COLOR_CHART_DOWN = 26
    CHART_COLOR_CHART_LINE = 27
    CHART_COLOR_CANDLE_BULL = 28
    CHART_COLOR_CANDLE_BEAR = 29
    CHART_COLOR_BID = 30
    CHART_COLOR_ASK = 31
    CHART_COLOR_LAST = 32
    CHART_COLOR_STOP_LEVEL = 33
    CHART_SHOW_TRADE_LEVELS = 34
    CHART_BRING_TO_TOP = 35
    CHART_SHOW_DATE_SCALE = 36
    CHART_SHOW_PRICE_SCALE = 37
    CHART_EVENT_OBJECT_CREATE = 38
    CHART_EVENT_OBJECT_DELETE = 39
    CHART_EVENT_MOUSE_MOVE = 40
    CHART_MOUSE_SCROLL = 42
    CHART_DRAG_TRADE_LEVELS = 43
    CHART_QUICK_NAVIGATION = 45
    CHART_VISIBLE_BARS = 100
    CHART_WINDOWS_TOTAL = 101
    CHART_WINDOW_IS_VISIBLE = 102
    CHART_WINDOW_HANDLE = 103
    CHART_FIRST_VISIBLE_BAR = 104
    CHART_WIDTH_IN_BARS = 105
    CHART_WIDTH_IN_PIXELS = 106
    CHART_HEIGHT_IN_PIXELS = 107
    CHART_WINDOW_YDISTANCE = 110
    CHART_IS_OFFLINE = 112

class EnumChartPropertyString:
    CHART_COMMENT = 20

class ENUM_TIMEFRAMES:
    PERIOD_CURRENT = 0
    PERIOD_M1 = 1
    PERIOD_M2 = 2
    PERIOD_M3 = 3
    PERIOD_M4 = 4
    PERIOD_M5 = 5
    PERIOD_M6 = 6
    PERIOD_M10 = 10
    PERIOD_M12 = 12
    PERIOD_M15 = 15
    PERIOD_M20 = 20
    PERIOD_M30 = 30
    PERIOD_H1 = 60
    PERIOD_H2 = 120
    PERIOD_H3 = 180
    PERIOD_H4 = 240
    PERIOD_H6 = 360
    PERIOD_H8 = 480
    PERIOD_H12 = 720
    PERIOD_D1 = 1440
    PERIOD_W1 = 10080
    PERIOD_MN1 = 43200

class EnumAlignMode:
    ALIGN_RIGHT = 0
    ALIGN_LEFT = 1
    ALIGN_CENTER = 2

class OrderSelectMode:
    SELECT_BY_POS = 0
    SELECT_BY_TICKET = 1

class OrderSelectSource:
    MODE_TRADES = 0
    MODE_HISTORY = 1

class ChartPeriod:
    ZERO = 0
    PERIOD_M1 = 1
    PERIOD_M5 = 5
    PERIOD_M15 = 15
    PERIOD_M30 = 30
    PERIOD_H1 = 60
    PERIOD_H4 = 240
    PERIOD_D1 = 1440
    PERIOD_W1 = 10080
    PERIOD_MN1 = 43200

class SeriesIdentifier:
    MODE_OPEN = 0
    MODE_LOW = 1
    MODE_HIGH = 2
    MODE_CLOSE = 3
    MODE_VOLUME = 4
    MODE_TIME = 5

class MarketInfoModeType:
    MODE_LOW = 1
    MODE_HIGH = 2
    MODE_TIME = 5
    MODE_BID = 9
    MODE_ASK = 10
    MODE_POINT = 11
    MODE_DIGITS = 12
    MODE_SPREAD = 13
    MODE_STOPLEVEL = 14
    MODE_LOTSIZE = 15
    MODE_TICKVALUE = 16
    MODE_TICKSIZE = 17
    MODE_SWAPLONG = 18
    MODE_SWAPSHORT = 19
    MODE_STARTING = 20
    MODE_EXPIRATION = 21
    MODE_TRADEALLOWED = 22
    MODE_MINLOT = 23
    MODE_LOTSTEP = 24
    MODE_MAXLOT = 25
    MODE_SWAPTYPE = 26
    MODE_PROFITCALCMODE = 27
    MODE_MARGINCALCMODE = 28
    MODE_MARGININIT = 29
    MODE_MARGINMAINTENANCE = 30
    MODE_MARGINHEDGED = 31
    MODE_MARGINREQUIRED = 32
    MODE_FREEZELEVEL = 33

class EnumObject:
    OBJ_VLINE = 0
    OBJ_HLINE = 1
    OBJ_TREND = 2
    BJ_TRENDBYANGLE = 3
    OBJ_REGRESSION = 4
    OBJ_CHANNEL = 5
    OBJ_STDDEVCHANNEL = 6
    OBJ_GANNLINE = 7
    OBJ_GANNFAN = 8
    OBJ_GANNGRID = 9
    OBJ_FIBO = 10
    OBJ_FIBOTIMES = 11
    OBJ_FIBOFAN = 12
    OBJ_FIBOARC = 13
    OBJ_EXPANSION = 14
    OBJ_FIBOCHANNEL = 15
    OBJ_RECTANGLE = 16
    OBJ_TRIANGLE = 17
    OBJ_ELLIPSE = 18
    OBJ_PITCHFORK = 19
    OBJ_CYCLES = 20
    OBJ_TEXT = 21
    OBJ_ARROW = 22
    OBJ_LABEL = 23
    OBJ_BITMAP_LABEL = 24
    OBJ_BUTTON = 25
    OBJ_BITMAP = 26
    OBJ_EDIT = 27
    OBJ_RECTANGLE_LABEL = 28
    OBJ_ARROW_THUMB_UP = 29
    OBJ_ARROW_THUMB_DOWN = 30
    OBJ_ARROW_UP = 31
    OBJ_ARROW_DOWN = 32
    OBJ_ARROW_STOP = 33
    OBJ_ARROW_CHECK = 34
    OBJ_ARROW_LEFT_PRICE = 35
    OBJ_ARROW_RIGHT_PRICE = 36
    OBJ_ARROW_BUY = 37
    OBJ_ARROW_SELL = 38
    OBJ_EVENT = 42

class EnumObjectPropertyDouble:
    OBJPROP_SCALE = 12
    OBJPROP_ANGLE = 13
    OBJPROP_DEVIATION = 16
    OBJPROP_PRICE = 20
    OBJPROP_LEVELVALUE = 204

class EnumObjectPropertyInteger:
    OBJPROP_COLOR = 6
    OBJPROP_STYLE = 7
    OBJPROP_WIDTH = 8
    OBJPROP_BACK = 9
    OBJPROP_ELLIPSE = 11
    OBJPROP_ARROWCODE = 14
    OBJPROP_TIMEFRAMES = 15
    OBJPROP_SELECTED = 17
    OBJPROP_TYPE = 18
    OBJPROP_TIME = 19
    OBJPROP_FONTSIZE = 100
    OBJPROP_CORNER = 101
    OBJPROP_XDISTANCE = 102
    OBJPROP_YDISTANCE = 103
    OBJPROP_LEVELS = 200
    OBJPROP_LEVELCOLOR = 201
    OBJPROP_LEVELSTYLE = 202
    OBJPROP_LEVELWIDTH = 203
    OBJPROP_ZORDER = 207
    OBJPROP_HIDDEN = 208
    OBJPROP_CREATETIME = 998
    OBJPROP_SELECTABLE = 1000
    OBJPROP_RAY_RIGHT = 1004
    OBJPROP_ANCHOR = 1011
    OBJPROP_STATE = 1018
    OBJPROP_XSIZE = 1019
    OBJPROP_YSIZE = 1020
    OBJPROP_BGCOLOR = 1025
    OBJPROP_READONLY = 1028
    OBJPROP_BORDER_TYPE = 1029
    OBJPROP_XOFFSET = 1033
    OBJPROP_YOFFSET = 1034
    OBJPROP_BORDER_COLOR = 1035
    OBJPROP_ALIGN = 1036

class EnumObjectPropertyString:
    OBJPROP_LEVELTEXT = 205
    OBJPROP_TOOLTIP = 206
    OBJPROP_TEXT = 999
    OBJPROP_FONT = 1001
    OBJPROP_BMPFILE = 1017
    OBJPROP_SYMBOL = 1021
    OBJPROP_NAME = 1037

class EnumSeriesInfoInteger:
    SERIES_BARS_COUNT = 0
    SERIES_FIRSTDATE = 1
    SERIES_SERVER_FIRSTDATE = 2
    SERIES_LASTBAR_DATE = 5

class EnumSymbolInfoDouble:
    SYMBOL_BID = 1
    SYMBOL_BIDHIGH = 2
    SYMBOL_BIDLOW = 3
    SYMBOL_ASK = 4
    SYMBOL_ASKHIGH = 5
    SYMBOL_ASKLOW = 6
    SYMBOL_LAST = 7
    SYMBOL_LASTHIGH = 8
    SYMBOL_LASTLOW = 9
    SYMBOL_POINT = 16
    SYMBOL_TRADE_TICK_VALUE = 26
    SYMBOL_TRADE_TICK_SIZE = 27
    SYMBOL_TRADE_CONTRACT_SIZE = 28
    SYMBOL_VOLUME_MIN = 34
    SYMBOL_VOLUME_MAX = 35
    SYMBOL_VOLUME_STEP = 36
    SYMBOL_SWAP_LONG = 38
    SYMBOL_SWAP_SHORT = 39
    SYMBOL_MARGIN_INITIAL = 42
    SYMBOL_MARGIN_MAINTENANCE = 43
    SYMBOL_MARGIN_LONG = 44
    SYMBOL_MARGIN_SHORT = 45
    SYMBOL_MARGIN_LIMIT = 46
    SYMBOL_MARGIN_STOP = 47
    SYMBOL_MARGIN_STOPLIMIT = 48
    SYMBOL_TRADE_TICK_VALUE_PROFIT = 53
    SYMBOL_TRADE_TICK_VALUE_LOSS = 54
    SYMBOL_VOLUME_LIMIT = 55
    SYMBOL_SESSION_VOLUME = 57
    SYMBOL_SESSION_TURNOVER = 58
    SYMBOL_SESSION_INTEREST = 59
    SYMBOL_SESSION_BUY_ORDERS_VOLUME = 61
    SYMBOL_SESSION_SELL_ORDERS_VOLUME = 63
    SYMBOL_SESSION_OPEN = 64
    SYMBOL_SESSION_CLOSE = 65
    SYMBOL_SESSION_AW = 66
    SYMBOL_SESSION_PRICE_SETTLEMENT = 67
    SYMBOL_SESSION_PRICE_LIMIT_MIN = 68
    SYMBOL_SESSION_PRICE_LIMIT_MAX = 69

class EnumSymbolInfoInteger:
    SYMBOL_SELECT = 0
    SYMBOL_VOLUME = 10
    SYMBOL_VOLUMEHIGH = 11
    SYMBOL_VOLUMELOW = 12
    SYMBOL_TIME = 15
    SYMBOL_DIGITS = 17
    SYMBOL_SPREAD = 18
    SYMBOL_TRADE_CALC_MODE = 29
    SYMBOL_TRADE_MODE = 30
    SYMBOL_TRADE_STOPS_LEVEL = 31
    SYMBOL_TRADE_FREEZE_LEVEL = 32
    SYMBOL_TRADE_EXEMODE = 33
    SYMBOL_SWAP_MODE = 37
    SYMBOL_SWAP_ROLLOVER3DAYS = 40
    SYMBOL_SPREAD_FLOAT = 41
    SYMBOL_EXPIRATION_MODE = 49
    SYMBOL_FILLING_MODE = 50
    SYMBOL_START_TIME = 51
    SYMBOL_EXPIRATION_TIME = 52
    SYMBOL_SESSION_DEALS = 56
    SYMBOL_SESSION_BUY_ORDERS = 60
    SYMBOL_SESSION_SELL_ORDERS = 62
    SYMBOL_ORDER_MODE = 71
    SYMBOL_VISIBLE = 76

class DayOfWeek:
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

class SessionType:
    Quote = 0
    Trade = 1

class ENUM_SYMBOL_INFO_STRING:
    SYMBOL_DESCRIPTION = 20
    SYMBOL_PATH = 21
    SYMBOL_CURRENCY_BASE = 22
    SYMBOL_CURRENCY_PROFIT = 23
    SYMBOL_CURRENCY_MARGIN = 24

class EnumTerminalInfoDouble:
    TERMINAL_COMMUNITY_BALANCE = 25

class EnumTerminalInfoInteger:
    TERMINAL_BUILD = 5
    TERMINAL_CONNECTED = 6
    TERMINAL_DLLS_ALLOWED = 7
    TERMINAL_TRADE_ALLOWED = 8
    TERMINAL_EMAIL_ENABLED = 9
    TERMINAL_FTP_ENABLED = 10
    TERMINAL_MAXBARS = 11
    TERMINAL_CODEPAGE = 12
    TERMINAL_MEMORY_PHYSICAL = 14
    TERMINAL_MEMORY_TOTAL = 15
    TERMINAL_MEMORY_AVAILABLE = 16
    TERMINAL_MEMORY_USED = 17
    TERMINAL_DISK_SPACE = 20
    TERMINAL_CPU_CORES = 21
    TERMINAL_MQID = 22
    TERMINAL_COMMUNITY_ACCOUNT = 23
    TERMINAL_COMMUNITY_CONNECTION = 24
    TERMINAL_NOTIFICATIONS_ENABLED = 26
    TERMINAL_SCREEN_DPI = 27
    TERMINAL_PING_LAST = 28

class ENUM_TERMINAL_INFO_STRING:
    TERMINAL_COMPANY = 0
    TERMINAL_NAME = 1
    TERMINAL_PATH = 2
    TERMINAL_DATA_PATH = 3
    TERMINAL_COMMONDATA_PATH = 4
    TERMINAL_LANGUAGE = 13

class FlagFontStyle:
    FONT_ITALIC = -2147483648
    FW_DONTCARE = 0
    FW_THIN = 1
    FW_EXTRALIGHT = 2
    FW_ULTRALIGHT = 3
    FW_LIGHT = 4
    FW_NORMAL = 5
    FW_REGULAR = 6
    FW_MEDIUM = 7
    FW_SEMIBOLD = 8
    FW_DEMIBOLD = 9
    FW_BOLD = 10
    FW_EXTRABOLD = 11
    FW_ULTRABOLD = 12
    FW_HEAVY = 13
    FW_BLACK = 14
    FONT_STRIKEOUT = 536870912
    FONT_UNDERLINE = 1073741824

class ENUM_CHART_POSITION:
    CHART_BEGIN = 0
    CHART_CURRENT_POS = 1
    CHART_END = 2