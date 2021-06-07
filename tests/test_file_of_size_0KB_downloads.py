import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import downloader

drive_service = downloader.get_drive_service()

def test_file_of_size_0KB_download():	
	rc = downloader.download_file(drive_service, '1hAhS3ppO8aGVmooMZzD1mprsSifoEVMj', 'downloads\\sample_0KB_file.txt')
	assert rc == True