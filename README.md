# GroupSporcle
Group Sporcle repository used for updating results.

In order to log a score correctly:
1) Find out what day it is:
python whatdayisit.py

2) log a score:
python sporcle.py

NOTES: categories should have the first letter capitalised and spaces in the title should be denoted by an underscore e.g. Just_for_fun

If you are happy with the entry at the end, and you select 'y', the score will automatically be logged to sporcle.txt.
If you are unsure, and you select anything other than 'y', the score won't be logged, but it can still be logged by using:
source sporcle.sh
or
./sporcle.sh

For the moment, this process does not use TTrees, so simply use:
python makeroot.py

4) examine the graphs at your leisure:
root -l SporcleAnalysis.root
