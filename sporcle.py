from __future__ import print_function
import os, random
import sys, socket
import datetime
#import writeData
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
print("""                                            ``````````````                                          
                                       ``````````````````....``                                     
                                   `````           ```````....--..`                                 
                               `````                  ``````...--::-.`                              
                             ````                       ``````..--::::-`                            
                           `````                          `````..--::///-`                          
                         ``````                            `````..--:://+/.                         
                        ``````                              ````...--://++o:`                       
                       `.````                                ````..--:://+oo/`                      
                      ..````                                 ````...--://++oo/`                     
                     ...````                                 `````..--://++ooo:                     
                    `-..````                                  ````..--://++oooo.                    
                    --..````                                  ````..--://++oooo+                    
                   `--..````                                 `````..--://++ooooo.                   
                   .--...````                                ````..--:://+oooooo:                   
                   -:--..````                               `````..--:://+oooooo/                   
                   -:--...````                             `````..--:://++oooooo/                   
                   .::--..`````                           `````...--:///+ooooooo:                   
                   ./::--...`````                        `````...--:://++ooooooo.                   
                    :/::--...``````                    ``````...--:://++ooooooo+                    
                    .//::---...```````              ```````...---::///+oooooooo.                    
                     ://::---....````````````````````````....---::///++oooooo+:                     
                     `////::---....```````````````````.....---:::///+++++++++/`                     
                      `/+///::----......`````````.......----:::///++++++++++/`                      
                       `:++///:::-----.............------:::::///++++++++++:`                       
                         -+++////:::::---------------::::::////+++++++++//.                         
                          `:++++/////::::::::::::::::://////++++++++////-`                          
                            .:+o+++++///////////////////++++++++++////-`                            
                              `-/oooo+++++++++++++++++++++++++++///:.`                              
                                `.-/+oooooooooooooooooo+++++++//:-`                                 
                                    `.-/++ooooooooooooo+++//:-.`                                    
                                        ```.:syyyyyyyyh+.```                                        
                                             +hhddddddh`                                            
                                            .syhddddhhh:`                                           
                                         `./syyhhhhhhhhho:`                                         
                                    ``.-/+ossyyyyyyyyyyyyyso/-``                                    
                                  .://++ooosssssssssssssssssssso+-                                  
                       ``.-.      `.-://++ooooooooooooooooo+++//-.      -:-.`                       
                     .//+o+:``          ````............````          `.oddhyo:`                    
                    .++++++++//:::-..``````              ``````..-:/+syhhhhhhhh-                    
                     `.-://///+syyyyyysssooooo++++++++ooooosssyyyyyyyyyyyyss+:.                     
                         ``..-//++oooooooooooooooooooooooooooooooo++//:--.`                         
                                     ````..................````                                     
                                                                                                    
                                                                                                    
                                                                                                    
""")

dayofyear = datetime.datetime.now().timetuple().tm_yday
year =  datetime.datetime.now().timetuple().tm_year
yearafter = year - 2019
if (year%4 == 0):
    leap = 1
else:
    leap = 0
yearmod = 160 + (yearafter * 365) + leap
truedate = dayofyear+yearmod
#print (dayofyear + yearmod)



print ("You are entering a score from a sporcle quiz!")
inpscore = input("What was your raw score?\n")
score = float(inpscore)
inpmaximum = input("What was the maximum score?\n")
maximum = float(inpmaximum)
print ("score is", score, ",  maximum is", maximum, "and their sum is", score+maximum, "and their ratio is ", score/maximum)
percentage = (score/maximum)*100
inpaverage = input("What was the average percentage?\n")
average = int(inpaverage)
difference = percentage - average
if sys.version_info[0] < 3:
	category = raw_input("What was the category?\n")
	players = raw_input("How many of you played the quiz?\n")
	day = str(truedate)
	winnipeg = raw_input("Winnipeg? [y/n]\n")
else:
	category = input("What was the category?\n")
	players = input("How many of you played the quiz?\n")
	day = str(truedate)
	winnipeg = input("Winnipeg? [y/n]\n")

print ("Ok, so on day", day, ",", players, "of you played a", category, "quiz, and you got", score, "/", maximum, "=", percentage, "% while the average was", average, "%? And winnipeg is a ", winnipeg, "?")

goodlist = ["That right there was the work of a superior intellect.", "Most people would not have been that smart. You are not most people.", "I bet you fill out crossword puzzles in pen.", "We bet your mum always liked you the best too.", "Someone's firing on all cylinders!", "Is this the greatest moment of your life?", "What's it like to be perfect?", "Now you're getting the hang of it!", "Great job! Next time, win CASH when you do this well ... on FleetWit!", "9/10 dentists agree: You are the BEST. Now go win some cash on FleetWit!", "We're so proud of you.", "Want to win cash for knowing stuff? Play trivia on FleetWit!", "'All things excellent are as difficult as they are rare.' -Baruch Spinoza", "*fist bump*"]
averagelist = ["You get an A for ... Average.", "Of all the scores you could possibly have achieved, that was certainly one of them.", "A perfectly cromulent score.", "Close, but no cigar! Smoking is bad for your health anyway.", "I see what you did there. If you can't beat 'em, join 'em!", "Right smack dab at average. Well played.", "How nice of you not to ruin the curve for everyone else.", "You're in the sweet spot between really awesome and totally not awesome."]
badlist = ["You have died of dysentery.", "Maybe this will build character.", "Not your best effort, but keep trying!", "OK, now that you are all warmed up, let's do this for real!", "There's nothing like a good score, and that was nothing like a good score.", "Oof. This is not your area of expertise.", "Good first effort! Try again and you'll nail this bad boy!", "Just so you know, these comments get funnier the better you do.", "I just want you to feel you're doing well."]

print (len(goodlist))

print ("That's a difference of", difference, "!")
if (difference < 0):
    choice = random.randint(0, len(badlist)-1)
    print (badlist[choice])
elif (difference > 10):
    choice = random.randint(0, len(goodlist)-1)
    print (goodlist[choice])
else:
    choice = random.randint(0, len(averagelist)-1)
    print (averagelist[choice])
    
#os.system("chmod 755 sporcle.sh")
if sys.version_info[0] < 3:
	submit = raw_input("Are the details above correct?[y/n]\n")
else:
	submit = input("Are the details above correct?[y/n]\n")
with open('sporcle.sh', 'w') as fout:
	fout.write("#!/bin/bash\n")
	fout.write("echo "+str(score)+" "+str(maximum)+" "+str(percentage)+" "+str(average)+" "+str(difference)+" "+category+" "+day+" "+players+" "+winnipeg+" >> sporcle.txt\n")
	fout.write("echo Score stored to sporcle.txt")
if (submit == "y"):
	if ("ph.bham.ac.uk" not in socket.gethostname()):
		data=str(score)+" "+str(maximum)+" "+str(percentage)+" "+str(average)+" "+str(difference)+" "+category+" "+day+" "+players+" "+winnipeg
		print ("You appear to be a remote user, copying data to eprexa")
		#writeData.put_file('eprexa.ph.bham.ac.uk','/home/rb/Documents/GroupSporcle', 'sporcle.txt', data)
	else:	
		os.system("./sporcle.sh")
else:
    print ("You can store the score still by sourcing sporcle.sh")

