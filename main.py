from math import exp as e

#Dictionaries for RPV

premdc = {}
masterdc = {}
elitedc = {}
vetdc = {}
rivaldc = {}
challydc = {}
prospectdc = {}
tendydc = {}
ammydc = {}

#Dictionaries for MMR

premmmr = {}
mastermmr = {}
elitemmr = {}
vetmmr = {}
rivalmmr = {}
challymmr = {}
prospectmmr = {}
tendymmr = {}
ammymmr = {}

#Constants for RPV

minrpv = 15
maxrpv = 75

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

expo_constant_add = 2.2
expo_constant_multi = 0.1

lin_constant_multi = 1.5

tier_order = ['amateur','contender','prospect','challenger','rival','veteran','elite','master','premier']

# Recursive funtion
def recursive_fun(rpv,tier):
    x = tier_order.index(tier.lower())
    if rpv >= maxrpv and tier != 'premier':
        recursive_fun(rpv-25,tier_order[x+1])
    else:
        return float(rpv)

# TEXT FILE MUST BE IN THE FORMAT "RSCID,Tier,RPV,GP"

fp = open("S19 RPV Player Info.txt", "r")

for line in fp.readlines():
    line = line.strip("\n")
    record = line.split(",")
    record[3] = int(record[3])
    record[2] = float(record[2])
    if record[1].lower() == "premier":
        if record[2] <= 0:
            premdc[record[0]] = 0
        else:
            premdc[record[0]] = recursive_fun(record[2],'premier')

    elif record[1].lower() == "master":
        if record[2] <= 0:
            masterdc[record[0]] = 0
        else:
            masterdc[record[0]] = recursive_fun(record[2],'master')

    elif record[1].lower() == "elite":
        if record[2] <= 0:
            elitedc[record[0]] = 0
        else:
            elitedc[record[0]] = recursive_fun(record[2],'elite')

    elif record[1].lower() == "veteran":
        if record[2] <= 0:
            vetdc[record[0]] = 0
        else:
            vetdc[record[0]] = recursive_fun(record[2],'veteran')

    elif record[1].lower() == "rival":
        if record[2] <= 0:
            rivaldc[record[0]] = 0
        else:
            rivaldc[record[0]] = recursive_fun(record[2],'rival')

    elif record[1].lower() == "challenger":
        if record[2] <= 0:
            challydc[record[0]] = 0
        else:
            challydc[record[0]] = recursive_fun(record[2],'challenger')

    elif record[1].lower() == "prospect":
        if record[2] <= 0:
            prospectdc[record[0]] = 0
        else:
            prospectdc[record[0]] = recursive_fun(record[2],'prospect')

    elif record[1].lower() == "contender":
        if record[2] <= 0:
            tendydc[record[0]] = 0
        else:
            tendydc[record[0]] = recursive_fun(record[2],'contender')

    elif record[1].lower() == "amateur":
        ammydc[record[0]] = recursive_fun(record[2],'amateur')

def setPlayerMMR(RPV,tierminmmr,tierdelta, premier = False, ammy = False):
    if float(RPV) >= maxrpv and not premier:
        return   2.5**((expo_constant_multi * (RPV-maxrpv)) + expo_constant_add) + (tierminmmr + tierdelta)
    elif ammy:
        return (tierdelta/(maxrpv)) * RPV + tierminmmr
    else:
        return ((tierdelta/(maxrpv-minrpv)) * RPV + (tierminmmr-(((tierdelta)/(maxrpv-minrpv))*minrpv)))



for RSCID in premdc:
    premmmr[RSCID] = setPlayerMMR(premdc[RSCID],premmin,premdelta,True)

for RSCID in masterdc:
    mastermmr[RSCID] = setPlayerMMR(masterdc[RSCID],mastermin,masterdelta)

for RSCID in elitedc:
    elitemmr[RSCID] = setPlayerMMR(elitedc[RSCID],elitemin,elitedelta)

for RSCID in vetdc:
    vetmmr[RSCID] = setPlayerMMR(vetdc[RSCID],vetmin,vetdelta)

for RSCID in rivaldc:
    rivalmmr[RSCID] = setPlayerMMR(rivaldc[RSCID],rivalmin,rivaldelta)

for RSCID in challydc:
    challymmr[RSCID] = setPlayerMMR(challydc[RSCID],challymin,challydelta)

for RSCID in prospectdc:
    prospectmmr[RSCID] = setPlayerMMR(prospectdc[RSCID],prospectmin,prospectdelta)

for RSCID in tendydc:
    tendymmr[RSCID] = setPlayerMMR(tendydc[RSCID],tendymin,tendydelta)

for RSCID in ammydc:
    ammymmr[RSCID] = setPlayerMMR(ammydc[RSCID],ammymin,ammydelta)

fp = open("New MMR Values.txt","w")
for RSCID,NewMMR in premmmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in mastermmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in elitemmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in vetmmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in rivalmmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in challymmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in prospectmmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in tendymmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
for RSCID,NewMMR in ammymmr.items():
    fp.write(RSCID+','+str(NewMMR)+"\n")
fp.close()
