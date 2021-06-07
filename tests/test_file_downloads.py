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

def test_audio_file_download():
	rc = downloader.download_file(drive_service, '1cR3A-nLzl01KkNDTkXrBa9vQdBmp95vE', 'downloads\\audio_sample_file.mp3')
	assert rc == True

def test_xl_file_download():
	rc = downloader.download_file(drive_service, '1TwBL3Bul8y0Fo6hx7uXdaEJpIwrz4CKv', 'downloads\\sample_xl_file.xlsx')
	assert rc == True

def test_word_doc_download():
	rc = downloader.download_file(drive_service, '1uD1SDwieY1sForVL9EJvi5IWm8DqlZq5', 'downloads\\sample_word_doc_file.docx')
	assert rc == True

def test_zip_file_download():
	rc = downloader.download_file(drive_service, '1g7Qn4fytaVUhfs5bcxInrQvuU6lBK12i', 'downloads\\sample_zip_file.zip')
	assert rc == True

def test_png_file_download():
	rc = downloader.download_file(drive_service, '1PzaLfYnJM2TjRbZfg3cbWsjqKXwJerou', 'downloads\\sample_png_file.png')
	assert rc == True
