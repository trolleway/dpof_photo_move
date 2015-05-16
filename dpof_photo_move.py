#Move your photos in two folders by DPOF file.
#Usage: Copy photos from camera and /MICS/AUTPRINT.MRK file and this python file in one folder. Then python dpof_photo_move.py

import os
import fileinput
import re
import shutil

AUTPRINT_PATH=''

filelist=[]
AUTPRINT = open( AUTPRINT_PATH+'AUTPRINT.MRK', 'r' )
for line in AUTPRINT.xreadlines():
	if line.find('.JPG')>-1 or line.find('.DFF')>-1:
		
		#str=str(line).strip()
		startpos=line.rfind(r'/')
		endpos=line.rfind(r'""')
		file = line[startpos+1:endpos-2]
		#print file
		filelist.append(str(file).strip())
		
AUTPRINT.close

OK_FOLDERNAME='dpof_ok'
SKIP_FOLDERNAME='dpof_skip'

if not os.path.exists(OK_FOLDERNAME):
    os.makedirs(OK_FOLDERNAME)

if not os.path.exists(SKIP_FOLDERNAME):
    os.makedirs(SKIP_FOLDERNAME)
	
#print 'getcwd='+	os.getcwd()

#put ok file to ok folder
for file in filelist:
	if os.path.isfile(file):
		src=os.path.join(os.getcwd(),file)
		dst=os.path.join(os.getcwd(),OK_FOLDERNAME,file)
		#print src +'   >     '+dst
		os.rename(src, dst)
		
		
#put all files in skip folder		
for dirpath, dnames, fnames in os.walk(os.getcwd()):
    for file in fnames:
		if os.path.isfile(file):
			if file.endswith(".JPG"):
				src = os.path.join(os.getcwd(),file)
				dst=os.path.join(os.getcwd(),SKIP_FOLDERNAME,file)
				#print src +'   >     '+dst
				os.rename(src, dst)
