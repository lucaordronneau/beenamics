####### Définitions des variables facteurs (Paramétrisation)
ELRbase0 = 1600
ERLstochrange = 0.02
SUPthreshold = 0.2
CELLShive0 = 250000
x1, x2, x3, x4, x5 = 385, 30, 36, 155, 30
LIFESPANegg = 3
LIFESPANlarva = 5
LIFESPANpupa = 12
MORTALITYeggs = 0.03
MORTALITYlarvae = 0.01
MORTALITYpupae = 0.001
CANNIBALISMhungerbase = [0.23, 0.3, 0.58, 0.06, 0] # for i in [1,2,...,5]
MORTALITYbase = 0.01
MORTALITYnursing = 0.005
MORTALITYprocessing = 0.005
MORTALITYforaging = 0.035
LOADpollenforager = 0.06
LOADnectarforager = 0.04
TURNSnectarforager = 15
TURNSpollenforager = 10
FACTORforagingsuccess = 0.8
FACTORminpollenforagers = 0.01
FACTORforagingmax = 0.33
FACTORothertasks = 0.2
ProcessorsPerCell = 2
FACTORpollenstorage = 6
FACTORpollensavingmax = 0.3
RATIOnectar_to_honey = 0.4 # 20/50
w_nectar = 0.43
w_pollen = 0.23
w_cellsbase = 0.037
w_honey = 0.5
w_egg = 0.0001
w_pupa = 0.16
w_adult = 0.1
w_larva = [0.0002,0.00059, 0.00331, 0.0644, 0.160] # for i in [1,...,5]
w_hivebase = 14000 #("14,000g")

####### VARIABLE INITIALE
INITpollen = 0
INITnectar = 0
INIThoney = 50000
INITBEESadult = 15000
INITCELLSbrood = 0
INITWEIGHTcolony = 50

####### VARIABLE INITIALE METEO
INITlat = 43.4167
INITlon = -0.5833
INITmeteoCsv = "donne_meteo.csv"

####### Définitions des variables "inconnues" par lecture graphique approximative 
#Après série de test, les graphs semble cohérent avec ces paramètres
POLLENNEEDadult = 0.0037 
POLLENNEEDnurse = 0.045 
NECTARNEEDactiveforager = 0.03 
NECTARNEEDadult = 0.005
NECTARNEEDnurse = 0.2 
NEEDnurses_per_larva = [0.10,0.30,0.70,1.70,3.0] #REF p231 graph d
NEEDnurses_per_egg = 0.30
NEEDnurses_per_pupa = 0.30
MORTALITYadultbase = 0.01
NECTARNEEDlarva = [0.0025,0.0050,0.0084,0.016,0.032] #REF p231 graph b
POLLENNEEDlarva = [0.0150,0.0250,0.0400,0.080,0.156] #REF p231 graph b

####### Parameter swarming day
swd = 140
RATIOnectar_to_wax = 0.66

