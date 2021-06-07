import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import downloader

drive_service = downloader.get_drive_service()

def test_download_with_not_existing_file_id():	
	rc = downloader.download_file(drive_service, '1l72diSxwK413K2i1ux5hNgHk7_jsjsj', 'downloads\\xyz.txt')
	assert rc == False