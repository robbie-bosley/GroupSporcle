import os, random

print "You are entering a score from a sporcle quiz!"
inpscore = input("What was your raw score?\n")
score = float(inpscore)
inpmaximum = input("What was the maximum score?\n")
maximum = float(inpmaximum)
print "score is", score, ",  maximum is", maximum, "and their sum is", score+maximum, "and their ratio is ", score/maximum
percentage = (score/maximum)*100
inpaverage = input("What was the average percentage?\n")
average = int(inpaverage)
difference = percentage - average
category = raw_input("What was the category?\n")
players = raw_input("How many of you played the quiz?\n")
day = raw_input("What day is it (number form, where day 79 is 11/10/2018)\n")
winnipeg = raw_input("Winnipeg? [y/n]\n")


print "Ok, so on day", day, ",", players, "of you played a", category, "quiz, and you got", score, "/", maximum, "=", percentage, "% while the average was", average, "%? And winnipeg is a ", winnipeg, "?"

goodlist = ["That right there was the work of a superior intellect.", "Most people would not have been that smart. You are not most people.", "I bet you fill out crossword puzzles in pen.", "We bet your mum always liked you the best too.", "Someone's firing on all cylinders!", "Is this the greatest moment of your life?", "What's it like to be perfect?", "Now you're getting the hang of it!", "Great job! Next time, win CASH when you do this well ... on FleetWit!", "9/10 dentists agree: You are the BEST. Now go win some cash on FleetWit!", "We're so proud of you.", "Want to win cash for knowing stuff? Play trivia on FleetWit!", "'All things excellent are as difficult as they are rare.' -Baruch Spinoza"]
averagelist = ["You get an A for ... Average.", "Of all the scores you could possibly have achieved, that was certainly one of them.", "A perfectly cromulent score.", "Close, but no cigar! Smoking is bad for your health anyway.", "I see what you did there. If you can't beat 'em, join 'em!", "Right smack dab at average. Well played.", "How nice of you not to ruin the curve for everyone else."]
badlist = ["You have died of dysentery.", "Maybe this will build character.", "Not your best effort, but keep trying!", "OK, now that you are all warmed up, let's do this for real!", "There's nothing like a good score, and that was nothing like a good score.", "Oof. This is not your area of expertise.", "Good first effort! Try again and you'll nail this bad boy!", "Just so you know, these comments get funnier the better you do.", "I just want you to feel you're doing well."]

print len(goodlist)

print "That's a difference of", difference, "!"
if (difference < 0):
    choice = random.randint(0, len(badlist)-1)
    print badlist[choice]
elif (difference > 10):
    choice = random.randint(0, len(goodlist)-1)
    print goodlist[choice]
else:
    choice = random.randint(0, len(averagelist)-1)
    print averagelist[choice]
    
with open('sporcle.sh', 'w') as fout:
    fout.write("#!/bin/bash\n")
    fout.write("echo "+str(score)+" "+str(maximum)+" "+str(percentage)+" "+str(average)+" "+str(difference)+" "+category+" "+day+" "+players+" "+winnipeg+" >> sporcle.txt\n")
    fout.write("echo Score stored to sporcle.txt")

#os.system("chmod 755 sporcle.sh")

submit = raw_input("Are the details above correct?[y/n]\n")
if (submit == "y"):
    os.system("./sporcle.sh")
else:
    print "You can store the score still by sourcing sporcle.sh"

