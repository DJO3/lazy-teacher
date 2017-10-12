import httplib2
import os
import re
from pprint import pprint

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


class Drive:
    """
    A class for interacting with Google Docs
    """

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/drive-lazy-teacher.json

    def __init__(self):

        # If modifying these scopes, delete your previously saved credentials
        # at ~/.credentials/drive-lazy-teacher.json
        self.scope = 'https://www.googleapis.com/auth/drive.readonly'
        self.client_secret_file = 'client_secret.json'
        self.app_name = 'Lazy Teacher'
        self.credentials = None
        self.service = None

    def get_credentials(self):
        """
        Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_name = 'drive-lazy-teacher.json'
        credential_path = os.path.join(credential_dir, credential_name)

        store = Storage(credential_path)
        self.credentials = store.get()
        if not self.credentials or self.credentials.invalid:
            flow = client.flow_from_clientsecrets(self.client_secret_file, self.scope)
            flow.user_agent = self.app_name
            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)
            self.credentials = credentials
        return self.credentials

    def set_service(self, credentials):
        """
        Connects to Drive with credentials
        """

        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('drive', 'v3', http=http)

        return self.service


    def get_service(self):
        """
        Validates that credentials have been set and connects to Drive
        """

        if not self.credentials:
            self.credentials = self.get_credentials()
        
        if not self.service:
            self.service = self.set_service(self.credentials)

        return self.service

    def get_files(self):
        """
        Lists files in Drive directory
        """

        # Get Drive service
        service = self.get_service()

        page_token = None
        # q="'0BzVL1e-d-7fVNUxIVXhjSFFDSmc' in parents"
        # q="mimeType='application/vnd.google-apps.folder' AND name='Papers'"
        folder_query = "mimeType='application/vnd.google-apps.folder' AND name='Papers'"
        folder_fields = 'files(id, name)'
        folder = service.files().list(q=folder_query,fields=folder_fields).execute()
        folder_id = folder['files'][0]['id']

        papers_query = f"mimeType='application/vnd.google-apps.document' AND '{folder_id}' in parents"
        papers = service.files().list(q=papers_query,
                                      fields='nextPageToken, files(id, name)',
                                      pageToken=page_token).execute()

        return papers['files']

    def get_text(self, file_id, mime_type):
        """
        Gets byte string of drive content
        """

        # Get Drive service
        service = self.get_service()

        text = service.files().export_media(fileId=file_id, mimeType=mime_type).execute()
        return text
