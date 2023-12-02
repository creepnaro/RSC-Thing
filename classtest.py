# Clear exports

fp = open("New MMR Values.txt","w")
fp.close()


# Lists/Dictionaries

tiers = ['amateur','contender','prospect','challenger','rival','veteran','elite','master','premier']
RSCID = {}

#Constants for RPV

minrpv = 15
maxrpv = 75

promotion_constant = maxrpv-minrpv
doublepromorpv = 95
double_promotion_constant = doublepromorpv - minrpv

#Constants for MMR

ammymin = 750
tendymin = 935
prospectmin = 1045
challymin = 1165
rivalmin = 1295
vetmin = 1415
elitemin = 1510
mastermin = 1650
premmin = 1760
premmax = 2000

premdelta = (premmax-premmin)
masterdelta = (premmin-mastermin-5)
elitedelta = (mastermin-elitemin-5)
vetdelta = (elitemin-vetmin-5)
rivaldelta = (vetmin-rivalmin-5)
challydelta = (rivalmin-challymin-5)
prospectdelta = challymin-prospectmin-5
tendydelta = prospectmin-tendymin-5
ammydelta = tendymin-ammymin-5

tiermin = {'amateur':ammymin,'contender':tendymin,'prospect':prospectmin,'challenger':challymin,'rival':rivalmin,'veteran':vetmin,'elite':elitemin,'master':mastermin,'premier':premmin}
tierdelta = {'amateur':ammydelta,'contender':tendydelta,'prospect':prospectdelta,'challenger':challydelta,'rival':rivaldelta,'veteran':vetdelta,'elite':elitedelta,'master':masterdelta,'premier':premdelta}

# Class Set-up

class mmrCalculator:
    
    def __init__(self,rscid,tier,rpv):

        if tier.lower() in tiers:
            self.rscid = rscid
            self.tier = tier.lower()
            if rpv <= 0:
                self.rpv = 0
            else:
                self.rpv = rpv
            self.mmr = None
        else:
            print('Tier Error')
            return None
    
    def __repr__(self):
        return '{} {} {} {}'.format(self.rscid,self.tier,self.rpv,self.mmr)

    def promotion(self):
        tier_index = tiers.index(self.tier)
        if self.rpv >= doublepromorpv and self.tier != tiers[-2]:
            self.rpv -= double_promotion_constant
            self.tier = tiers[tier_index + 2]
            return
        elif self.rpv >= maxrpv and self.tier != tiers[-1]:
            self.rpv -= promotion_constant
            self.tier = tiers[tier_index + 1]
            return
        else:
            return
        

    def calculateMMR(self):
        if self.tier == 'amateur' or self.tier == 'premier':
            self.mmr = (tierdelta[self.tier]/(maxrpv)) * self.rpv + tiermin[self.tier]
        else:
            self.mmr = ((tierdelta[self.tier]/(maxrpv-minrpv)) * self.rpv + (tiermin[self.tier]-(((tierdelta[self.tier])/(maxrpv-minrpv))*minrpv)))

    def exportingMMR(self):
        fp = open("New MMR Values.txt","a")
        fp.write(self.rscid + ',' + str(self.mmr) + '\n')
        fp.close()

# TEXT FILE MUST BE IN THE FORMAT "RSCID,Tier,RPV"

fp = open("S19 RPV Player Info.txt", "r")

for line in fp.readlines():
    line = line.strip("\n")
    record = line.split(",")
    code = record[0]
    tier = record[1]
    rpv = float(record[2])
    RSCID[code] = mmrCalculator(code,tier,rpv)

fp.close()

for id,mmr in RSCID.items():
    mmr.promotion()
    mmr.calculateMMR()
    mmr.exportingMMR()