#!/bin/bash 
mkdir data 
cd data 

echo "Retrieve speech data"
mkdir speech 
cd speech 
wget http://media.radiofrance-podcast.net/podcast09/10902-21.12.2010-ITEMA_20259141-0.mp3 

echo "Retrieve music data, under Creative Commons licence "
cd ../
mkdir music 
cd 
wget "http://download29.jamendo.com/download/track/674453/mp32/34a3dca3d9/Hope.mp3"
wget "http://download31.jamendo.com/download/track/391002/mp32/9ebfb2d8d2/Balrog%20Boogie.mp3"
wget "http://download29.jamendo.com/download/track/608272/mp32/0ae3a1780b/zero-project%20-%20Infinity.mp3"
wget "http://download30.jamendo.com/download/track/108580/mp32/f3bd3439c2/Dirty%20angel.mp3"
wget "http://download29.jamendo.com/download/playlist/185867/mp32/cfea093ef2/occidentalindigene%20yaada%20(Playlist%20by%20o%20sombo)%20--%20Jamendo%20-%20MP3%20VBR%20192k%20%5Bwww.jamendo.com%5D.zip"
unzip *.zip 
rm -Rf *.zip 
