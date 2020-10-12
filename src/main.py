#file --main.py--

from cell import cell
from motor import motor
from pack import pack
from vehicle import vehicle

#Vehicle inputs:
motorCount = 4
#example
#Motor input:
motorName = 'U7 V2.0 - KV 420'
motorVoltage =  25
motorMaxCurrent = 47.5

#Energy input:
#Format [power(Watts), duration(hours)],[power2(Watts), duration2(hours)]
powerInterval = [[8650,.00833],[5970,.5], [7040, .5], [3830,.00833]]

myPack = pack()
myPack.setVoltageRequired(motorVoltage)
myPack.energyRequiredFromList(powerInterval)
myPack.setPowerRequired(motorMaxCurrent*motorCount)
print('_______________________________________________________________')
myPack.optimizePack()