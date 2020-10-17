#file --main.py--

from cell import cell
from motor import motor
from pack import pack
from vehicle import vehicle

#Vehicle inputs:
motorCount = 1
#example
#Motor input:
motorName = 'Emrax 228 MV'
motorVoltage =  300
motorMaxCurrent = 266.6

#Energy input:
#Format [power(Watts), duration(hours)],[power2(Watts), duration2(hours)]
powerInterval = [[80000,.33],[64000, .067], [36400, .017]] #FIXME: This doesn't assign correctly, set it in line 13 in pack.py

myPack = pack()
myPack.setVoltageRequired(motorVoltage)
myPack.energyRequiredFromList(powerInterval)
myPack.setPowerRequired(motorMaxCurrent*motorCount)
print('_______________________________________________________________')
myPack.optimizePack()