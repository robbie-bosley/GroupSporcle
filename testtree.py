import numpy as np
import ROOT
from array import array
from ROOT import TGraph, TH1F, TFile, TCanvas, TPaveText, TTree, TBranch, TString


x = [0.0, 10.0, 7.0, 6.0, 6.0, 3.0, 2.0, 5.0]
y = [3.0, 2.0, 1.0, 5.0, 4.0, 8.0, 11.0, 4.0]

File = TFile("test.root", "RECREATE")
Tree= TTree("Tree", "Tree for testing");

px = 0.0
py = 0.0

Tree.Branch(x)
Tree.Branch(y)

for i in range (0, len(x)):
    px = x[i]
    py = y[i]
    Tree.Fill()

File.Write()
