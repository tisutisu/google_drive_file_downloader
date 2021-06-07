## Application to download google drive files from command line
This tool is for downloading files from google drive

### [Prerequisites]
you need the following prerequisites:

1. Python 3

2. Install the google client api libraries using :

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

3. Create a google cloud platform project and enable "Google Drive API". Refer :
https://developers.google.com/workspace/guides/create-project

4. Create Desktop application credentials. Refer :
https://developers.google.com/workspace/guides/create-credentials

    4a. Configure the OAuth consent screen with user type as "External". 
    
    4b. In Update scope section add "https://www.googleapis.com/auth/drive"
    
    4c. Add Test Users (email) for whom you want to allow the access of the API
    
    4d. After creating the Desktop application credentials and download the client secret file to this local repo directory and rename it as client_secrets.json
    

### [Usage]
 
Run the "downloader.py" script from command line as below:

python downloader.py --list <no_of_entries>

python downloader.py --file_id <file_id> --local_dir <destination_folder>

For example:

1. To list 10 files present in drive :

python downloader.py --list 10

2. To download a file with file_id = 1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH to default directory "downloads" in the current location : 

python downloader.py --file_id 1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH

2. To download a file with file_id = 1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH to location "C:\Users\sushanta\Desktop" :

python downloader.py --file_id 1FSwcfi4EYYwDsT7-yGBBc_9jY8xceeKH --local_dir "C:\Users\sushanta\Desktop"



#### Note:
If this is your first time running the script, the script opens a new window prompting you to authorize access to your data:

1. If you are not already signed in to your Google account, you are prompted to sign in. 
   If you are signed in to multiple Google accounts, you are asked to select one account to use for the authorization.
   Note: Authorization information is stored on the file system, so subsequent executions don't prompt for authorization.
2. Click Accept. The app is authorized to access your data.
