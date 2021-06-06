# https://developers.google.com/drive/api/v3/quickstart/python
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
import os
import sys
import io
import argparse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    return service

def list_of_filename_and_fileId(service, size):
    # Call the Drive v3 API
    results = service.files().list(pageSize=size, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1}) {2}'.format(item['name'], item['id'], len(item['id'])))

def is_file_exists_in_drive(service, file_id):
	page_token = None
	while True:
		response = service.files().list(spaces='drive', fields='nextPageToken, files(id, name)', pageToken=page_token).execute()
		for file in response.get('files', []):
			if file.get('id') == file_id:
				#print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
				return True
		page_token = response.get('nextPageToken', None)
		if page_token is None:
			break
	return False

def get_filename_from_drive(service, file_id):
	page_token = None
	while True:
		response = service.files().list(spaces='drive', fields='nextPageToken, files(id, name, mimeType)', pageToken=page_token).execute()
		for file in response.get('files', []):
			if file.get('id') == file_id:
				return file.get('name'), file.get('mimeType')
		page_token = response.get('nextPageToken', None)
		if page_token is None:
			break
	return None, None

def download_file(service, file_id, local_file_path):
	if not is_file_exists_in_drive(service, file_id):
		print("File not found in drive")

	try:
		request = service.files().get_media(fileId=file_id)
		fh = io.BytesIO()
		downloader = MediaIoBaseDownload(fh, request)
		done = False
		while done is False:
			status, done = downloader.next_chunk()
			print("Download %d%%." % int(status.progress() * 100))
		
		with io.open(local_file_path, 'wb') as f:
			fh.seek(0)
			f.write(fh.read())

	except Exception as e:
		print('Exception while downloading file: {}'.format(e))

def upload_file(service, file_path, mtype):
	file_metadata = {'name': file_path.split('/')[-1]}
	media = MediaFileUpload(file_path, mimetype=mtype)
	file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

	print('File ID: {}'.format(file.get('id')))

def main():
	
	parser = argparse.ArgumentParser(description='Google Drive downloader')
	parser.add_argument("-i", "--file_id", type=str, action="store", help="Id of the file to download")
	parser.add_argument("-d", "--local_dir", type=str, action="store", default="downloads", help="Local folder to download the file")
	args = parser.parse_args()
	
	drive_service = get_drive_service()
	fileId = args.file_id

	if fileId != None:
		
		if len(fileId) != 33:
			sys.exit("File id is incorrect")
		file_name, mimetype = get_filename_from_drive(drive_service, fileId)
		if file_name == None:
			sys.exit("File not found in drive : {}".format(fileId))
		
		if mimetype == 'text/plain':
			print("Text File")
		elif mimetype == 'image/jpeg':
			print("Jpeg file")
		elif mimetype == 'application/pdf':
			print("PDF File")
			file_name += '.pdf'
		else:
			print(mimetype)
		
		local_file_path = args.local_dir + os.sep + file_name 
		
		download_file(drive_service, fileId, local_file_path)

	#Download Test Sample
	# id : '1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH' name: form_1_signed.pdf
	# id : '1-dNrz5JlWxv2AhhgnzMx4RW1Ho4hfHo0' name: photo.jpg
	# id : '1l72diSxwK413K2i1ux5hNgHk7_ZORebh' name: xyz.txt

	#list_of_filename_and_fileId(drive_service, 10)
	#upload_file(drive_service, 'files/photo.jpg', 'image/jpeg')

if __name__ == '__main__':
	main()