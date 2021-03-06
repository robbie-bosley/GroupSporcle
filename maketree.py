import numpy as np
import ROOT
from array import array
from ROOT import TGraph, TH1F, TFile, TCanvas, TPaveText, TTree, TBranch, TString


filename = "sporcle.txt"

inpscore, inpmaximum, inppercentage, inpaverage, inpdifference, inpcategory, inpday, inpplayers, inpwinnipeg = np.loadtxt(filename, dtype = 'string', unpack=True)

print inpscore


nentries = len(inpscore)

score = array('f', nentries*[0.])#[] #array('f', nentries*[0.])
maximum = array('f', nentries*[0.])
percentage = array('f', nentries*[0.])
average = array('f', nentries*[0.])
difference = array('f', nentries*[0.])
category = []
day = array('i', nentries*[0])
players = array('i', nentries*[0])
winnipeg = []

print score

#print score
    
#TTree
tSporcleData = TTree("SporcleData", "Tree containing Sporcle information");

#Tbranches
#score
indivscore = float(0.0)
tSporcleData.Branch('score', indivscore, 'score/F')
#maximum

print "started loop"
for i in range (0, len(inpscore)):
    score[i] = float(inpscore[i])
    indivscore = score[i]
    tSporcleData.Fill()

print score

#fracdifference = (difference/average)

#print "Score inputted is", score[i]
for i in range (0, len(inpscore)):  
    maximum[i] = float(inpmaximum[i])
    percentage[i] = float(inppercentage[i])
    average[i] = float(inpaverage[i])
    difference[i] = float(inpdifference[i])
    category.append(inpcategory[i])
    day[i] = int(inpday[i])
    players[i] = int(inpplayers[i])
    winnipeg.append(inpwinnipeg[i])
    
#tSporcleData.Fill()
    
h_difference = TH1F("difference", "Difference between recorded percentage score and average percentage", 50, -101, 101)
for i in difference:
    h_difference.Fill(i)
    
    
#h_fracdifference = TH1F("fracdifference", "Fractional Difference between recorded percentage score and average percentage", 50, -1, 1)
#for i in fracdifference:
#    h_fracdifference.Fill(i)
    
#h_score = TH1F("score", "Raw score from sporcle quiz", int(max(score)+1)/4, -1, int(max(score)+1))
#for i in range (0, len(inpscore)):
#    #print "Filling histogram with", i
    #score [i] = float(inpscore[i])
    #print "filled with", score[i]
    #h_score.Fill(score[i])
    #tSporcleData.Fill()
    #h_score.Fill(score[i])
#for i in score:
#    print "score is", i
#    h_score.Fill(i)
#    tSporcleData.Fill()
    
#h_maximum = TH1F("maximum", "Maximum score for sporcle quiz", int(max(maximum)+1)/4, -1, int(max(maximum)+1))
#for i in maximum:
#    h_maximum.Fill(i)

#h_percentage = TH1F("percentage", "Percentage score from sporcle quiz", 50, -1, 101)
#for i in percentage:
#    h_percentage.Fill(i)

#h_average = TH1F("average", "Average public score for sporcle quiz", 50, -1, 101)
#for i in average:
#    h_average.Fill(i)

#h_day = TH1F("day", "Day on which sporcle quiz was attempted", max(day)+1, -1, max(day)+1)
#for i in day:
#    h_day.Fill(float(i))

#h_players = TH1F("players", "Number of players playing the quiz", max(players)+1, -1, max(players)+1)
#for i in players:
#    h_players.Fill(float(i))

#h_difference.SetFillColor(2)
#h_fracdifference.SetFillColor(3)
#h_score.SetFillColor(4)
#h_maximum.SetFillColor(5)
#h_percentage.SetFillColor(6)
#h_average.SetFillColor(7)
#h_day.SetFillColor(8)
#h_players.SetFillColor(9)

#c_forgov = TCanvas("forgov", "Canvas for Gov. <3", 1000, 1000)
#h_fracdifference.GetXaxis().SetTitle("This is the x axis")
#h_fracdifference.GetYaxis().SetTitle("This is the y axis")
#h_fracdifference.Draw()
#text = TPaveText(0.1, 0.7, 0.3, 0.9)
#text.AddText("There is no z axis")
#text.Draw()
#c_forgov.BuildLegend()
#c_forgov.Print("canvasforgov.png")

tree_file = TFile("TreeSporcleAnalysis.root", "RECREATE")
tSporcleData.Write("SporcleData")
tree_file.Close()


#s_file = TFile("SporcleAnalysis.root", "RECREATE")
#h_difference.Write("Difference")
#h_fracdifference.Write("FractionalDifference")
#h_score.Write("Score")
#h_maximum.Write("Maximum")
#h_percentage.Write("Percentage")
#h_average.Write("Average")
#h_day.Write("Day")
#h_players.Write("Players")
#s_file.Close()
