### The West Wing Randomizer! 

I'm an avid fan :) 

My next being my >= 8th rewatch of TWW, I decided I wanted to watch all episodes without repeats, but in a random order. 

Some data in /helpers could be modified to suit another show. I'll leave anything further up to you. 

<h4> Requirements: </h4>

Python3 installed, honestly version probably does matter. 

`reset.sh` is written for zsh. I'm pretty sure it works in bash as well. 

<h4> Usage: </h4>

The repo is ready to go out of the box, clone and: 

When you want to watch an episode: `python3 script.py`

resetting with the help of my script requires `chmod +x reset.sh` **DO NOT `CHMOD +X` ANYTHING YOU DON'T TRUST** I trust myself :) you shouldn't. But review the code yourself, it's very simple, or trust the comments section of the reddit post I will link after creating it. 

To reset: `./reset.sh`

<h4> /helpers </h4> 

`static_watched.txt` is necessary for reset, and should not be modified for any reason. 

`this_time_through.txt` is a list of the episodes you've watched this time through in order! It has no technical function. 

`titles.txt` 

Season 5, Episode 18, "Access" is a terrible episode, and it is included, but to skip if it shows up, simply run the program again. Which episode it is is listed in `helpers/Access.note`

`rawepisodes.txt` is a copy-paste from https://www.westwingepguide.com/list.html that I parsed to generate some stuff

`watch_throughs.txt` will track all subsequent watch throughs. 