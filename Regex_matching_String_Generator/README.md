
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| FEEL FREE TO USE / MODIFY THE CODE			|
| JUST MENTION MY NAME AS THE CONTRIBUTOR FOR THIS CODE	|
| ALONG WITH THE GITHUB LINK TO THIS CODE 		|
|  -------- (THANKS) ----------				|
|							|
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||


==== Prerequisites ====
	-- Python 2.x, compatible with Python 3.x also. For 3.x compatibility  just change "raw_input" to "input" in source code.
	-- module "rstr" (pip install rstr)


==== Usage ====

-- LINUX USER ---
	-- Change it to executable (chmod 744 filename.py)  ## without ( )
	-- Run the file as script --- > ./<filename>.py

-- WINDOWS USER ---
	-- In command prompt, go to the directory of the file and type "python filename.py"   ## without quotes

-- Enter the Regular Expression
-- Enter the number of times you want the code to generate a random pattern based on the regular expression entered


==== Use case ====
(BRUTE FORCE URL SCAN)
----------------------

-- Many websites which display videos or images embedded cannot be downloaded directly
-- Using the inspect elecment in browser we first find the file names of the videos or images currently being viewed - eg :  https://video.somewebsite.com/video/Dt8Ku0wWkAAfvhA.mp4
-- Dt8Ku0wWkAAfvhA.mp4 is the filename of a video. We see it has random characters.
-- Checked another video, its name was Dt7pF2dXQAEyIb3.mp4
-- So we see that "Dt" remain constant in the name, 3rd character is an integer that varies 0-9 and there after till "." all 12 characters are random in nature, "mp4" is constant.
-- Thus to run a brute force attack to find the file names, we could use the regular expression "Dt[0-9][(\w\d*)]{12}.mp4" to generate a random list of strings that match the expression
-- Using that as a source "word list" in Dirbuster, we could run a brute force URL scan to detect the directories.
-- When code run, a file with name "Regex Search Pattern.txt" is created in the same directory to which the data is written.
-- Possibility of seeing duplicates in the final output. Remove them accordingly.
