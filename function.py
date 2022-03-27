# import package
# to manage the dataframe
import pandas as pd
# for the plot
import matplotlib.pyplot as plt
# to get date object
from datetime import datetime
import math


################################################################################
# declaration of global variable
# dictionnary use to store all our timing data by strains
strainDict = {}
wormsDict= {}


################################################################################
# functions


def getDataFromFile(file):
    with open(file, "r") as data:
        section = ""
        platingTiming =""
        strain = ""
        cellName = ""
        cellState = ""
        for line in data:
            if line.startswith("##"):
                section = str.upper(line.replace("#","").replace(" ", "").strip())

            if section == "GLOBAL_INFOS":
                if line.startswith("genotype"):
                    strain = str.upper(line[line.find(":")+1:].replace(" ", "").strip())
                    if strain != "" and not strain in strainDict.keys():
                        strainDict[strain]  = {}

                if line.startswith("plating_date_time"):
                    platingTiming= datetime.strptime(line[line.find(":")+1:].replace(" ", "").strip(), '%Y/%m/%d:%H-%M')


            elif section == "DIVISIONS":
                if line.startswith("# "):
                    cellName=  str.upper(line.replace(" ","").replace("#", "").strip())
                    if cellName != "" and  not cellName in strainDict[strain].keys():
                        strainDict[strain][cellName] = {}


                if cellName in line and line.split(":")[0].endswith("_div_date_time"):
                    cellState = str.upper(line[0:line.find("_")])
                    if cellState != "" and  not cellState in strainDict[strain][cellName].keys() : 
                        strainDict[strain][cellName][cellState] = []

                    checkValue = line[line.find(":")+1:].replace(" ", "").strip()
                    if str.upper(checkValue) != "NA":
                        divTiming = datetime.strptime(checkValue, '%Y/%m/%d:%H-%M')
                        tmp = divTiming - platingTiming
                        timing = (tmp.days*24) + math.floor(tmp.seconds/3600) + ((tmp.seconds%3600)/3600)
                        strainDict[strain][cellName][cellState].append(timing)


getDataFromFile("exemple.txt")


for strain in strainDict.keys():
    print(strain + " : {")
    for cell in strainDict[strain].keys():
        print(cell  + " : {")
        for state in strainDict[strain][cell].keys():
            print(state + " : " + str(strainDict[strain][cell][state]))

        print("}")

    print("}")
