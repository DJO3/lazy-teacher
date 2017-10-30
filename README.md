# Summary
A simple project that combines a Flask API, Google Drive, Nginx, and Docker. Scaffolding for Vue.js is provided. Allows a user to list folders in their Google Drive and output an index of words found in documents. 

# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Docker CE Version 17.09.0-ce-mac35 (19611)
    * Tested on macOS High Sierra 10.13.0

# Getting Started
1. Complete "Enable APIs for your project" and "Create authorization credentials" at https://developers.google.com/identity/protocols/OAuth2WebServer. **Make sure to specify the URI as `http://localhost` and the redirect_uri as `http://localhost/oauth2callback`.
2. Add a folder named `Papers` to your Google Drive
3. Add a document to the `Papers` folder containing text, e.g., Lorem Ipsum
4. `git clone https://github.com/DJO3/lazy-teacher.git` and drop client_secret.json into the api folder
5. `cd lazy-teacher` 
6. Save client_secrets.json from Step 1 to the root of lazy-teacher directory.
7. `docker-compose build`
8. `docker-compose up -d`
9. `open http://localhost/api/folders` to authenticate and grab a grade_url.
10. Navigate to grade_url for `Papers` folder to see index of text.

# Known Issues
1. I should write a test...
2. But I need a gui...
3. Oh wow I really should add exceptions