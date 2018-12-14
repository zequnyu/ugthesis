from datetime import timedelta
import csv

class Result():
    def __init__(self):
        self.answers = [1]*20
        self.times = [0]*4
        self.rates = [1]*4
        self.ratetimes = [0]*4

    def updateAnswer(self, index, value):
        self.answers[index] = value

    def updateTime(self, index, value):
        self.times[index] = value

    def updateRate(self, index, value):
        self.rates[index] = value

    def updateRateTime(self, index, value):
        self.ratetimes[index] = value

    def printResult(self):
        for i in range(0, 20):
            fi = "{0:0=2d}".format(i+1)
            print(fi + '|' + str(self.answers[i]))
            #timedelta(milliseconds=
        print(self.times[0], self.times[1], self.times[2], self.times[3])
        print(self.ratetimes[0], self.ratetimes[1], self.ratetimes[2], self.ratetimes[3])
        print(self.rates[0], self.rates[1], self.rates[2], self.rates[3])
        self.saveToFile()


    def saveToFile(self):
        with open('result.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for i in range(0, 20):
                writer.writerow([i+1, self.answers[i]])
            writer.writerow(['T', self.times[0], self.times[1], self.times[2], self.times[3]])
            writer.writerow(['T_R', self.ratetimes[0], self.ratetimes[1], self.ratetimes[2], self.ratetimes[3]])
            writer.writerow(['R', self.rates[0], self.rates[1], self.rates[2], self.rates[3]])
