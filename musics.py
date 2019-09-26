# -*- coding: cp1252 -*-
import os
import sys
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from pytube import YouTube

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"



class Musics():
    
    def __init__(self, query):
        self.search(query)
    
    def search(self, query):
        try:    
            #req = AppURLopener()
            #html = req.open("https://www.youtube.com/results?search_query=" + query)
            req = Request("https://www.youtube.com/results?search_query=" + query, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req)
        except HTTPError as e:
            print(e)
        except URLError:
            print("Url incorreta ou Server Down")
        else:
            res = BeautifulSoup(html.read().decode('utf-8', 'ignore'), "html5lib")
            tags = res.findAll('a',attrs={'class':'yt-uix-tile-link'})
            
            musics = {}
            i = 1 #contador
            
            for tag in tags:
                musics[i] = (tag.getText()+" ", "https://www.youtube.com" + tag['href'])
                print(str(i) + ". " + musics[i][0])
                i += 1
                
            print()
            
            self.musics = musics
    
    def play(self, idM):
        idM = int(idM)
        print("# Playing " + self.musics[idM][0] + " ...\n")   
        os.system("google-chrome --new-window " + self.musics[idM][1])
    
    def download(self, idM):
        try:
            idM = int(idM)
            print("# Download " + self.musics[idM][0] + " ...\n")
            YouTube( self.musics[idM][1] ).streams.first().download('~/Downloads/')
        except HTTPError as e:
            print(e)
            self.download(idM)
        
        '''
        yt = YouTube( self.musics[idM][1] )
        video = yt.get('mp4','360p')
        yt.set_filename( self.musics[idM][0] )
        video.download('./')
        '''


os.system("cls || clear")

param = sys.argv[1]

music = Musics(param)

print("# Play Music: play <id_music>")
print("# Download: down <id_music>\n")

op,idM = input().split()

if op == "play":
    music.play(idM)
elif op == "down":
    music.download(idM)


