import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import downloader

drive_service = downloader.get_drive_service()

def test_text_file_download():	
	rc = downloader.download_file(drive_service, '1l72diSxwK413K2i1ux5hNgHk7_ZORebh', 'downloads\\xyz.txt')
	assert rc == True

def test_jpg_file_download():
	rc = downloader.download_file(drive_service, '1-dNrz5JlWxv2AhhgnzMx4RW1Ho4hfHo0', 'downloads\\photo.jpg')
	assert rc == True

def test_pdf_file_download():
	rc = downloader.download_file(drive_service, '1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH', 'downloads\\form_1_signed.pdf')
	assert rc == True
