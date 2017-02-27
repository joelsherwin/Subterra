from guessit import guessit
import tmdbsimple as tmdb
import os
import hashlib
import time
import urllib2
import sys

<<<<<<< HEAD

=======
prePath = "I:\Movies\\"  #change this directory to yours
arr1 = os.listdir(prePath)
>>>>>>> origin/master
replace = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov"]


def calc_hash(filepath):
    readsize = 64*1024 #64kb
    with open(filepath,'rb') as file:
        size = os.path.getsize(filepath)
        data = file.read(readsize)
        file.seek(-readsize,os.SEEK_END)
        data += file.read(readsize)
        return hashlib.md5(data).hexdigest()

def get_subtitles(path):
    i=0
    print 'Calculating hash of video file...'
    hash = calc_hash(path)
<<<<<<< HEAD

=======
>>>>>>> origin/master
    for c in replace:
        path = path.replace(c,"")
    if os.path.exists(path+".srt"):
        print "It seems you already have the subtitle"
    elif not os.path.exists(path+".srt"):
        print 'Searching for subtitles...'
        print '[',
        while(i<5):
            time.sleep(0.1)
            print '####',
            i = i+1
        print ']'



        headers = { 'User-Agent' : 'SubDB/1.0 (subterra/0.1a; Subterra_v0.1a)' }
        url = "http://api.thesubdb.com/?action=download&hash="+hash+"&language=en"
        req = urllib2.Request(url, '', headers)
        response = urllib2.urlopen(req).read()
        with open(path+".srt","wb") as file1:
            file1.write(response)
        print 'Subtitle Downloaded'

        print '-------------------------'
prePath = sys.argv[1]
arr1 = os.listdir(prePath)
for files in arr1:
        if '.str' in files:
            continue
        else:
            print 'Looking for subtitles for',files
            path1 = prePath+files
            get_subtitles(path1)
