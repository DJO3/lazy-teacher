"""
Class to interface to Google Drive
"""
import os

import httplib2
from apiclient import discovery


class Drive:
    """
    A class for interacting with Google Docs
    """

    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/drive-lazy-teacher.json

    def __init__(self, credentials=None):

        # If modifying these scopes, delete your previously saved credentials
        # at ~/.credentials/drive-lazy-teacher.json
        self.credentials = credentials
        self.service = None

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
