import typing as t
import typing_extensions as te

from pydantic import BaseModel, Field, ConstrainedInt, PositiveInt, PositiveFloat


# class ModelInput(BaseModel):
#     """
#     Call this using something like
#     yr=2011, mnth=1, hr=2,season=1, holiday=0, weekday=4,workingday=0, 
#     weathersit=1, temp=0.24, atemp=0.287, hum=0.8, windspeed=0.0
    
#     """
#     yr:int
#     mnth:int
#     hr:int
#     season:int
#     holiday:int
#     weekday:int
#     workingday:int
#     weathersit:int
#     temp: float
#     atemp: float
#     hum:float
#     windspeed:float


# NeighborhoodLiteral = te.Literal[
#     "Blmgtn",
#     "Blueste",
#     "BrDale",
#     "BrkSide",
#     "ClearCr",
#     "CollgCr",
#     "Crawfor",
#     "Edwards",
#     "Gilbert",
#     "IDOTRR",
#     "Meadow",
#     "Mitchel",
#     "Names",
#     "NoRidge",
#     "NPkVill",
#     "NridgHt",
#     "NWAmes",
#     "OldTwon",
#     "SWISU",
#     "Sawyer",
#     "SawyerW",
#     "Somerst",
#     "StoneBr",
#     "Timber",
#     "Veenker",
# ]
# HouseStyleLiteral = te.Literal[
#     "1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"
# ]


# class ModelInput(BaseModel):
#     YrSold: PositiveInt
#     YearBuilt: PositiveInt
#     YearRemodAdd: PositiveInt
#     GarageYrBlt: PositiveInt
#     LotArea: PositiveFloat
#     Neighborhood: NeighborhoodLiteral
#     HouseStyle: HouseStyleLiteral


class YearInteger(ConstrainedInt):
    ge = 2010
    le = 2020

class MonthInteger(ConstrainedInt):
    ge = 1
    le = 12

class HourInteger(ConstrainedInt):
    ge = 0
    le = 23

class SeasonInteger(ConstrainedInt):
    ge = 1
    le = 4

class WeekDayInteger(ConstrainedInt):
    ge = 1
    le = 7

class BoleanInteger(ConstrainedInt):
    ge = 0
    le = 1

class ModelInput(BaseModel):
    '''
    
    yr=2011, mnth=1, hr=2,season=1, holiday=0, weekday=4,workingday=0, 
    weathersit=1, temp=0.24, atemp=0.287, hum=0.8, windspeed=0.0
    
    '''

    yr: YearInteger
    mnth: MonthInteger
    hr: HourInteger
    season: SeasonInteger
    holiday: BoleanInteger
    weekday: WeekDayInteger
    workingday: BoleanInteger
    weathersit: SeasonInteger
    temp: PositiveFloat
    atemp: PositiveFloat
    hum: PositiveFloat
    windspeed: PositiveFloat

