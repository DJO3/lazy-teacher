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
8. PENDING STEP - INTEGRATE WEB OAUTH - CURRENTLY NEEDS TO BE VALIDATED MANUALLY
9. `open http://localhost:5000`
