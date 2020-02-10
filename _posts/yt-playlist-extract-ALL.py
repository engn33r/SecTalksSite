#!/usr/bin/env python
from __future__ import unicode_literals
import youtube_dl
import os
import nltk
# Python 2
# requirements: youtube_dl, nltk

def confPlaylist(conf, title_phrase, title_format, track, use_yt_tags, custom_tags, yr, date, playlist):
    # Conference talk details
    # SET THESE VALUES MANUALLY
    # playlist = "https://www.youtube.com/watch?v=3eSo5v35rpw&list=PL9fPq3eQfaaAKl_BhOwzeWlGe6yJMk-b0"
    # conf = "DEF CON 27"
    # title_phrase = "DEF CON 27" # Conference name found in video title
    # track = "Wireless Village"
    # use_yt_tags=False
    # custom_tags='DEFCON, DEF CON, DEFCON27, DEF CON 27, wireless'
    conf_title = conf.replace(' ', '_')
    # yr = "2019"
    # date = "2019-08-09"
    # title_format = 2

    # Format definitions
    # title_format = 1
    # Compatible conferences: AppSec Cali 2019, 
    # <Conf name> - <talk title> - <speaker(s)>
    # <Conf name> - <talk title>
    # title_format = 2
    # Compatible conferences: 
    # <speaker> - <talk title> - <Conf name>
    # format = 3
    # Compatible conferences: Grrcon 2019

    # Try to create folder to save output files
    # If directory already exists, perhaps because previous script
    # finished abruptly and incompletely, no need to create again    
    if len(track) > 0:
        try:
            os.mkdir(conf_title + "_" + track.replace(' ', '_'))
            os.chdir(conf_title + "_" + track.replace(' ', '_'))
        except OSError, e:
            # If error exists besides 'File exists', raise        
            if e.errno != os.errno.EEXIST:
                raise
            # Otherwise if known error exists, continue
            os.chdir(conf_title + "_" + track.replace(' ', '_'))
    else:
        try:
            os.mkdir(conf_title)
            os.chdir(conf_title)
        except OSError, e:
            # If error exists besides 'File exists', raise        
            if e.errno != os.errno.EEXIST:
                raise
            # Otherwise if known error exists, continue
            os.chdir(conf_title)

    #Initialize empty variables - these get set in the for loop below
    video_id=""
    title=""
    speaker=""
    url=""

    # Initial playlist data extraction
    # ignoreerrors: necessary to skip videos marked as "private" in playlist
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True, 'ignoreerrors':True, 'skip_download':True, 'youtube_include_dash_manifest':False})
    extracted_info = ydl.extract_info(playlist, download=False)
    # Any Private video or other errors create 'None" value entries, so remove those
    video_list = [x for x in extracted_info['entries'] if x is not None]

    # Now that playlist info is extracted, loop through all videos in playlist
    for i, item in enumerate(video_list):

        # Gather basic video info
        if video_list[i] is None:
            break
        url = video_list[i]['webpage_url']     #url of video
        video_id_phrase = "watch?v="
        video_id = url[(url.find(video_id_phrase) + len(video_id_phrase)):] #extract video_id from url
        title = video_list[i]['title']           #title of video
        # Borrow tags from youtube video - warning: these might be useless
        tags = video_list[i]['tags']
        if use_yt_tags:
            tags_list = '['
            for j in tags:
                tags_list = tags_list + j + ', '
            tags_list = tags_list[:-2] + ']'
        else:
            tags_list = '[' + custom_tags + ']'

        # Now branch to parse info for the correct format (based on video title)
        if title_format == 1:
            # Format:
            # <Conf name> - <talk title> - <speaker(s)>
            # <Conf name> - <talk title>
            # Find speaker name within video title
            split_title = title.split(' - ')
            if len(split_title) >=3:
                speaker = split_title[-1]
            else:
                speaker = ""

            # Find talk title within video title
            brief_title = title[(title.find(title_phrase) + len(title_phrase)):].strip()
            # strip '-' char from beginning of title
            if brief_title.find('-') < 2:
                brief_title = brief_title[2:].strip()
            # if speaker name identified within title (format case 2), remove speaker name from title
            if len(speaker) > 1:
                brief_title = brief_title[:brief_title.find(speaker)-2].strip()
            # Replace bad chars in title (avoid problems with Liquid templating)
            brief_title = brief_title.replace(': ', ' - ')
            brief_title = brief_title.replace(':', '-')
        elif title_format == 2:
            # Format:
            # <speaker> - <talk title> - <Conf name>
            # <speaker> -<talk title> - <Conf name>
            # <speaker>- <talk title> - <Conf name>
            # <speaker> - <talk title> -<Conf name>
            # <speaker> - <talk title>- <Conf name>
            # Find speaker name within video title
            split_title = title.split(' - ')
            split_title_alt1 = title.split(' -')
            split_title_alt2 = title.split('- ')
            if len(split_title_alt1) > len(split_title):
                split_title = split_title_alt1
            if len(split_title_alt2) > len(split_title):
                split_title = split_title_alt2
            speaker=split_title[0]

            # Find talk title within video title
            brief_title = ' - '.join(split_title[1:-1]).strip()
        elif title_format == 3:
            # Format:
            # <Conf name> <talk title> <speaker(s)>
            # Find speaker name within video title
            split_title = title.split(' ')
            # Find talk title within video title
            # Looks like there's a consistent header of 4 words to remove
            brief_title = ' '.join(split_title[4:]).strip()

            # New Strategy: Any Irongeek video has speaker name and title at irongeek link
            # Planning to implemnt a parser to follow this link and extract data from irongeek site
            # because Youtube title is unreliable for automating

            # Old Strategy: Tried using nltk to extract speaker name (see code below)
            # Use nltk to try and identify speaker name, because there's no consistent delimiter
            # We assume that there are four cases for the speaker name:
            # 1) There is no speaker name in the title
            # 2) There is one word of a name at the end of the title (space delimited)
            # 3) There are two words of a name at the end of the title (space delimited)
            # 4) There are three words of a name at the end of the title (space delimited)
            '''
            tagged_title = nltk.pos_tag(nltk.word_tokenize(title))
            nltk_last_three = tagged_title[len(tagged_title)-3:]
            print(nltk_last_three)
            has_name = True
            name_counter = len(nltk_last_three) - 1
            speaker = "" # reset global variable
            
            while (has_name is True) and (name_counter >= 0):
                if nltk_last_three[name_counter][1] == "NNP":
                    speaker = nltk_last_three[name_counter][0] + " " + speaker
                    name_counter -= 1
                else:
                    has_name = False
            '''
            track = split_title[2]

        # Replace bad chars in title (avoid problems with Liquid templating)
        brief_title = brief_title.replace(': ', ' - ')
        brief_title = brief_title.replace(':', '-')

        # Debug info - print URL and brief_title
        '''
        print(url)
        print("speaker: " + speaker)
        print("brief_title: " + brief_title)
        '''

        # Trim extra whitespace
        speaker = speaker.strip()
        brief_title = brief_title.strip()
        track = track.strip()

        # Write output to file
        filename = date+'-'+brief_title+'.md'
        f = open(filename, 'w')
        f.write("---\n")
        f.write("type: youtube\n")
        f.write("yt-video-id: " + video_id + "\n")	
        f.write("homedisplay: iframe\n")
        f.write(("title: " + brief_title + "\n").encode('utf-8')) # Encode because of possibility of non-ascii chars
        f.write(("tags: " + tags_list + "\n").encode('utf-8')) # Encode because of possibility of non-ascii chars
        f.write("category: " + conf_title + "\n")
        f.write("layout: post-classic-sidebar-left\n")
        f.write(("speaker: " + speaker + "\n").encode('utf-8')) # Encode because of possibility of non-ascii chars
        f.write("conf: " + conf + "\n")
        f.write("track: " + track + "\n")
        f.write("yr: " + yr + "\n")
        f.write("vidurl: " + url + "\n")
        f.write("---\n")
        f.write((video_list[i]['description']).encode('utf-8')) # Description
        f.close()
    os.chdir('../') # move back to parent directory for next function

# Now parse all playlists
# GrrCon 2019
#confPlaylist("GrrCON 2019", "GrrCON 2019", 3, "", True, "",
#    "2019", "2019-10-24", "https://www.youtube.com/watch?v=7nmZ-DHAQkg&list=PLNhlcxQZJSm94bHWijx9DKOX-a3HcG0WN")
# Derby Con 2019
#confPlaylist("Derbycon 9", "", 4, "", True, "",
#    "2019", "2019-9-6", "https://www.youtube.com/watch?v=Fd_z-u5V7BA&list=PLNhlcxQZJSm_ZDJBksg97I5q1XsdQcyN5")
# DEF CON 27
'''
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Wireless Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, wireless",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=3eSo5v35rpw&list=PL9fPq3eQfaaAKl_BhOwzeWlGe6yJMk-b0")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Voting Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, voting, politics",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=lfYqNObOhNU&list=PL9fPq3eQfaaCtvsxPgP1y_5P3HIyS18n0")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Red Team Offensive Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, red team",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=1D1HiV4Afpg&list=PL9fPq3eQfaaChXmQKpp1YO19Gw-6SxBDs")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "BioHacking Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, biohacks",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=OKrdzv9Yx54&list=PL9fPq3eQfaaCMz4YGIBhOaMbLGUk2wI1o")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Aviation Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, aviation",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=bydy7lbFyFU&list=PL9fPq3eQfaaBqpu32JLE215tVt9N8ap-1")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Appsec Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, appsec",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=nVX33Cs5f2c&list=PL9fPq3eQfaaAhMTXgUcQv9aRrJUh4p1xp")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Blockchain Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, blockchain",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=ItBRStAD2hA&list=PL9fPq3eQfaaCi3xCMqdz4v0Y4BVjAPCBY")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Blue Team Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, blue team",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=yf6J8XO_wpY&list=PL9fPq3eQfaaCcSaZJVJoNBlyNZ9EBGSdg")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Car Hacking Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, car hacks",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=CiKhrmrRNU4&list=PL9fPq3eQfaaDvMO7vLSVVSPEfB7OHHEjy")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Cloud Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, cloud",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=tJc_CNQMh5k&list=PL9fPq3eQfaaD2DeX60yFoL0-cxsyQmasi")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Crypto and Privacy Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, crypto, privacy",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=YG33kAaFs6Q&list=PL9fPq3eQfaaCnlC3NQR6j7pwvlg5gKJsr")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "DroneWars Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, drone hacks",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=52wbkGeRigM&list=PL9fPq3eQfaaDTlf14JgGHoPTX_oe-3ZKC")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Ethics Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, ethics",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=7O3d6YaDa88&list=PL9fPq3eQfaaAXCSKlZzxdCRbbb2Ii9Nbc")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Hack the Sea Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, marine hacks",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=2SBSHM1fR3w&list=PL9fPq3eQfaaAq-su0FRSRPrlrnsGO96px")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Hardware Hacking Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, hardware",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=WFgY0h8zcjM&list=PL9fPq3eQfaaC63jDN7llPTXNblAIjiRrP")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "ICS Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, ICS",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=lggrDCYsVpw&list=PL9fPq3eQfaaC1Yc1tNmJrE2ZRPPlI71YV")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "IoT Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, IoT",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=jEX9YMbzFXs&list=PL9fPq3eQfaaCtaCDvE2FdrB5lwbWYG77W")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Monero Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, blockchain, cryptocurrency",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=87joZVWCJEo&list=PL9fPq3eQfaaBiCOF12ZYejtj21sI1jm0I")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Packet Hacking Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, network",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=4AtmC7P0vzc&list=PL9fPq3eQfaaButbVrT4iuAGpdLhCjEjM_")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "Recon Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, OSINT",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=yDvcBeP5ekI&list=PL9fPq3eQfaaCkpP6XOD4uCQB6NpGrbujo")
confPlaylist("DEF CON 27", "DEF CON 27", 2, "AI Village", False, "DEFCON, DEF CON, DEFCON27, DEF CON 27, AI",
    "2019", "2019-08-09", "https://www.youtube.com/watch?v=XOBUeyzop5E&list=PL9fPq3eQfaaBy_EIgmLzo45NLo9o9dAHZ")
'''
# AppSec Cali 2019
#confPlaylist("AppSec Cali 2019", "AppSecCali 2019", 1, "", True, "",
#    "2019", "2019-01-22", "https://www.youtube.com/watch?v=hqui975ee9c&list=PLpr-xdpM8wG-bXotGh7OcWk9Xrc1b4pIJ")


