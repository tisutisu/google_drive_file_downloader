import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import downloader

drive_service = downloader.get_drive_service()

def test_download_video_file_of_150MB():	
	rc = downloader.download_file(drive_service, '1IMcCzRpxvjQXkHJtt2qHhRs-eTB2Q-9m', 'downloads\\test_video_file.mts')
	assert rc == True