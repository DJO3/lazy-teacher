# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Docker CE Version 17.09.0-ce-mac35 (19611)
    * Tested on macOS High Sierra 10.13.0

# Getting Started
1. Complete "Enable APIs for your project" and "Create authorization credentials" at https://developers.google.com/identity/protocols/OAuth2WebServer. **Make sure to specify the URI as `http://localhost:5000` and the redirect_uri as `http://localhost:5000/oauth2callback`.
2. Add a folder named `Papers` to your Google Drive
3. Add a document to the `Papers` folder containing text, e.g., Lorem Ipsum
4. `git clone https://github.com/DJO3/lazy-teacher.git`
5. `cd lazy-teacher` 
6. Save client_secrets.json from Step 1 to the root of lazy-teacher directory.
7. `docker-compose build`
8. `docker-compose up -d`
9. `open http://localhost:5000`

# Known Issues
1. Currently on indexes the first file found in `Papers` folder. 