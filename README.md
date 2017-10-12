# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Docker CE Version 17.09.0-ce-mac35 (19611)
    * Tested on macOS High Sierra 10.13.0

# Getting Started
1. Complete Step 1 at https://developers.google.com/drive/v3/web/quickstart/python.
2. Add a folder named `Papers` to your Google Drive
3. Add a document to the `Papers` folder containing text, e.g., Lorem Ipsum
4. `git clone https://github.com/DJO3/lazy-teacher.git`
5. `cd lazy-teacher` 
6. `docker-compose build`
7. `docker-compose up -d`
8. `docker exec -it lazy-teacher bash`
9. Run and complete auth setup `python setup_auth.py --noauth_local_webserver`
10. `exit`
11. `docker-compose restart && open http://localhost:5000`

# Known Issues
OAUTH integration is wonky, sorry! Still learning how to do it properly with a web redirect. 
