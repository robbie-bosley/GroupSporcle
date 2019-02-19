import numpy as np
import ROOT
from array import array
from ROOT import TGraph, TH1F, TFile, TCanvas, TPaveText, TTree, TBranch, TString, TH2F


filename = "sporcle.txt"

inpscore, inpmaximum, inppercentage, inpaverage, inpdifference, inpcategory, inpday, inpplayers, winnipeg = np.loadtxt(filename, dtype = 'string', unpack=True)

#nentries = len(inpscore)

score = []
maximum = []
percentage = []
average = []
difference = []
day = []
players = []
fracdifference = []
category = []

#TTree
#tSporcleData = TTree("SporcleData", "Tree containing Sporcle information");

#Tbranches
#score
#tSporcleData.Branch('score', score, 'score/F')
#maximum
for i in inpcategory:
    category.append(i)
print category

for i in inpscore:
    score.append(float(i))
for i in inpmaximum:
    maximum.append(float(i))
for i in inppercentage:
    percentage.append(float(i))
for i in inpaverage:
    average.append(float(i))
for i in inpdifference:
    difference.append(float(i))
for i in inpday:
    day.append(int(i))
for i in inpplayers:
    players.append(int(i))

for i in range (0, len(difference)):
    fracdifference.append(difference[i]/average[i])

#for i in range (0, len(score)):
#    tSporcleData.Fill()

#Try to make an average fracdiff for each day:
day_for_avg = []
fracdiff_avg = []
for i in range (0, max(day)+1):
    fracdiffday = []
    for j in range (0, len(day)):
        if (day[j] == int(i)):
            fracdiffday.append(fracdifference[j])
    if (len(fracdiffday) != 0):
        day_for_avg.append(i)
        mean_list = np.mean(fracdiffday)
        fracdiff_avg.append(mean_list)
        
#print(len(fracdiff_avg))
#print(fracdiff_avg)
#print(len(day_for_avg))
#print(day_for_avg)
    
h_difference = TH1F("difference", "Difference between recorded percentage score and average percentage", 50, -101, 101)
for i in difference:
    h_difference.Fill(i)    
    
h_fracdifference = TH1F("fracdifference", "Fractional Difference between recorded percentage score and average percentage", 50, -max(fracdifference), max(fracdifference))
for i in fracdifference:
    h_fracdifference.Fill(i)
    
h_score = TH1F("score", "Raw score from sporcle quiz", int(max(score)+1)/4, -1, int(max(score)+1))
for i in score:
    h_score.Fill(i)

h_maximum = TH1F("maximum", "Maximum score for sporcle quiz", int(max(maximum)+1)/4, -1, int(max(maximum)+1))
for i in maximum:
    h_maximum.Fill(i)

h_percentage = TH1F("percentage", "Percentage score from sporcle quiz", 50, -1, 101)
for i in percentage:
    h_percentage.Fill(i)

h_average = TH1F("average", "Average public score for sporcle quiz", 50, -1, 101)
for i in average:
    h_average.Fill(i)

h_day = TH1F("day", "Day on which sporcle quiz was attempted", max(day)+1, -1, max(day)+1)
for i in day:
    h_day.Fill(float(i))

h_players = TH1F("players", "Number of players playing the quiz", max(players)+1, -1, max(players)+1)
for i in players:
    h_players.Fill(float(i))

h_day_vs_score = TH2F("DayVsScore", "Day sporcle quiz was attempted vs score of quiz", max(day)+1, -1, max(day)+1, int(max(score)+1)/4, -1, int(max(score)+1))
for i in range(0, len(score)):
    h_day_vs_score.Fill(float(day[i]), int(score[i]))

h_day_vs_fdif = TH2F("DayVsFracDiff", "Day sporcle quiz was attempted vs fractional difference", max(day)+1, -1, max(day)+1, 50, -max(fracdifference), max(fracdifference))
for i in range(0, len(score)):
    h_day_vs_fdif.Fill(float(day[i]), float(fracdifference[i]))

h_day_vs_fdif_avg = TH2F("DayVsFracDiffAvg", "Day sporcle quiz was attempted vs fractional difference average", len(day_for_avg)+2, min(day_for_avg)-1, max(day_for_avg)+1, 50, min(fracdiff_avg)-0.1, max(fracdiff_avg)+0.1)
for i in range(0, len(day_for_avg)):
    h_day_vs_fdif_avg.Fill(float(day_for_avg[i]), float(fracdiff_avg[i]))


    
h_difference.SetFillColor(2)
h_fracdifference.SetFillColor(3)
h_score.SetFillColor(4)
h_maximum.SetFillColor(5)
h_percentage.SetFillColor(6)
h_average.SetFillColor(7)
h_day.SetFillColor(8)
h_players.SetFillColor(9)

h_day_vs_fdif_avg.SetMarkerStyle(3)
h_day_vs_fdif_avg.SetMarkerColor(3)
h_day_vs_fdif_avg.GetXaxis().SetTitle("Day")
h_day_vs_fdif_avg.GetYaxis().SetTitle("Average Fractional Difference between Player scores and Public scores")
#h_day_vs_fdif_avg.SetStats(kFALSE)

c_forgov = TCanvas("forgov", "Canvas for Gov. <3", 1000, 1000)
h_fracdifference.GetXaxis().SetTitle("This is the x axis")
h_fracdifference.GetYaxis().SetTitle("This is the y axis")
h_fracdifference.Draw()
text = TPaveText(0.1, 0.7, 0.3, 0.9)
text.AddText("There is no z axis")
text.Draw()
c_forgov.BuildLegend()
c_forgov.Print("canvasforgov.png")

#tree_file = TFile("TreeSporcleAnalysis.root", "RECREATE")
#tSporcleData.Write("SporcleData")
#tree_file.Close()


s_file = TFile("SporcleAnalysis.root", "RECREATE")
h_difference.Write("Difference")
h_fracdifference.Write("FractionalDifference")
h_score.Write("Score")
h_maximum.Write("Maximum")
h_percentage.Write("Percentage")
h_average.Write("Average")
h_day.Write("Day")
h_players.Write("Players")
h_day_vs_score.Write("DayVsScore")
h_day_vs_fdif.Write("DayVsFracDifference")
h_day_vs_fdif_avg.Write("DayVsFracDiffAverage")
s_file.Close()
