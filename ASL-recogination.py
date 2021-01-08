from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

from matplotlib import style
style.use("ggplot")

"""
This is the Assignment 4 for the course CP467 at Wilfrid Laurier Unviversity
Authors: Rahul Agarwala, Ravish Virani, Haricharan Vinukonda
"""

"""
ASSUMPTIONS: We assume that the signs are completely black in color
"""

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,6)
    for eachNum in range(0,10):
        for furtherNum in numbersWeHave:

            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.jpg'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

createExamples()

def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)
    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x+=1
        except Exception as e:
            print(str(e))
                
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]



    #fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY,align='center')
    
    
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()

whatNumIsThis('images/test1.jpg')
whatNumIsThis('images/test2.jpg')
whatNumIsThis('images/test3.jpg')
whatNumIsThis('images/test4.jpg')
whatNumIsThis('images/test5.jpg')
whatNumIsThis('images/test6.jpg')
whatNumIsThis('images/test7.jpg')
whatNumIsThis('images/test8.jpg')
whatNumIsThis('images/test9.jpg')