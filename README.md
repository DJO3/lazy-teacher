# Requirements
1. [Docker Community Edition](https://www.docker.com/community-edition)
    * Docker CE Version 17.09.0-ce-mac35 (19611)
    * Tested on macOS High Sierra 10.13.0

# Getting Started
1. Complete Step 1 at https://developers.google.com/drive/v3/web/quickstart/python.
2. `git clone https://github.com/DJO3/lazy-teacher.git`
3. `cd lazy-teacher` 
5. `docker-compose build`
6. `docker-compose up -d`
7. `docker exec lazy-teacher bash -c "python lazy-teacher/drive.py --noauth_local_webserver"`
