#GroupProjectPart2
#Shawn Perkins

#Starting Message
#z is a useless variable
z = input("Press Enter to Start")

classScores = [95,96,97]
#Function for finding average in percent:
def classAverage(Scores):
    sumScores = 0
    numScores = len(Scores)
    for i in range (numScores):
       sumScores += Scores[i]
       i+1
    averagePercent = sumScores / len(classScores)
    return averagePercent

print(classAverage(classScores))