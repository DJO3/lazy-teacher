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

    def __init__(self, credentials=None):

        self.credentials = credentials
        self.service = None

    def set_service(self, credentials, google_app='drive', version='v3'):
        """
        Connects to Drive with credentials
        """

        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build(google_app, version, http=http)

        return self.service

    def get_service(self):
        """
        Validates that credentials have been set and connects to Drive
        """
        
        if not self.service:
            self.service = self.set_service(self.credentials)

        return self.service

    def get_files(self, folder_name="Papers", page_size=None):
        """
        Lists files in Drive directory
        """

        # Get Drive service
        service = self.get_service()

        folder_query = f"mimeType='application/vnd.google-apps.folder' AND name='{folder_name}'"
        folder_fields = 'files(id, name)'
        folder = service.files().list(q=folder_query,fields=folder_fields).execute()
        folder_id = folder['files'][0]['id']

        papers_query = f"mimeType='application/vnd.google-apps.document' AND '{folder_id}' in parents"
        
        # Query for files within folder
        page_token = None
        papers = service.files().list(pageSize=page_size,
                                      q=papers_query, 
                                      fields='nextPageToken, files(id, name)',
                                      pageToken=page_token).execute()
        
        # Pagination
        if papers.get('nextPageToken'):
            page_token = papers['nextPageToken']
            while page_token:
                new_papers = service.files().list(pageSize=10,
                                                  q=papers_query, 
                                                  fields='nextPageToken, files(id, name)',
                                                  pageToken=page_token).execute()
                papers['files'] = papers['files'] + new_papers['files']
                if new_papers.get('nextPageToken'):
                    page_token = new_papers['nextPageToken']
                else:
                    page_token = False

        return papers['files']

    def get_folders(self):
        """
        Lists folders in Drive directory
        """

        # Get Drive service
        service = self.get_service()

        page_token = None

        folder_query = "mimeType='application/vnd.google-apps.folder'"
        folder_fields = 'files(id, name)'
        folders = service.files().list(q=folder_query,
                                       fields=folder_fields,
                                       pageToken=page_token).execute()

        return folders

    def get_text(self, file_id, mime_type):
        """
        Gets byte string of drive content
        """

        # Get Drive service
        service = self.get_service()

        text = service.files().export_media(fileId=file_id, mimeType=mime_type).execute()
        return text
