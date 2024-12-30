# atari
My Atari 8-Bit projects.

This is a repository for my Atari 8-Bit code projects. Most of them require a FujiNet (the N: device) and/or an Atari 1020 printer, because that's what I have.

Everything is coded in FastBasic 4.6. https://github.com/dmsc/fastbasic

What's in here so far ...

* Wethern.FB - FujiNet based weather app. Also requires a companion Python script I have running on a Raspberry Pi. You will have to change a local URL in the code. Uses ALLCLTH.DAT and HEADER.DAT image files; put them at the root of your drive. If anyone wants to fix this to make the Atari able to extract the weather itself, that would be great. My FujiNet for some reason can't parse JSON and can't access Web sites that require authentication, thus the workarounds. Yes, Thom knows.

* Run-script.sh and simple-parse.py - Run on the RasPi, run-script launches the Pi's internal Web server and then fetches the weather once per hour. Get a free API key from https://www.meteomatics.com/en/api/getting-started/ and use that. I would love to implement this on the Atari but my Fujinet dies on the u/p authentication. Weather.txt is the output the Fujinet fetches.
  
* Quote.FB - FujiNet based app to download and display inspirational quotes.

* Printh.FB and Banner.FB - Prints a range of Hershey fonts on the 1020 in different sizes. There's some extra work required here.
  - I'm using MyDos 4.5. I create subdirectories called JHA and IDX. Put the JHA files into the JHA subdirectory, and create another subdirectory called IDX.
  - The tool Makedex.FB, when run, then creates a string of files in the IDX subdirectory with the disk locations of each glyph in each JHA file.
 
* Suite.ATR - An ATR with the programs set up to run. There are some loose hooks and such because it's all part of a bigger suite where some of the elements involve my personal data and I don't feel like releasing them to the public, but you'll get the sense of things.
