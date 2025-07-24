## Base template for study web-development with FastAPI

This project is designed to demonstrate the process of developing a software product and implements a chat for communication

Study plan [link](https://docs.google.com/document/d/1xcSVSRqYZ_Cjb5ZU_IrroJNyz4EWtotie_vG_t7HDZk)

### Project structure

- package manager is poetry
- core framework is FastAPI
- database Postgres

```
my-app/
├── alembic/ - store migrations
├──── env.py - functions for running migrations
├── app/
├──── app/
├────── api/ - handle all routes in separite files
├──────── __init__.py
├────── __init__.py
├────── app.py - accumulate all routes
├──── db/ - store models for database
├──── modules/ - provide buistes logic
├──── schemas/ - store data schemas
├──── services/ - provide buisnes logic
├── __init__.py
├── __main__.py - mane file that run app
├── .env - contains environment variables like creds
├── .gitignore
├── .dockerignore
├── .alembic.ini - config file for alembic
├── .docker-compose.yml
├── poetry.lock
└── pyproject.toml
```

Each web-app is an application that modify some data. Data is a core element that describe all system and any operations is a process of data transformation into new specific format

So data is a core of any application and any project starts from the questions
1. What data we are going to handle
2. How they are going to describe ower system

The answers to the questions lie in the list of requirements and ideas that customers put forward.
For this project core idea is

`Develop some messanger for secure communication beetwing customers and workers, handle some personal informations. Allow integrate different bots.`

Requirements are:
1. Messaging in private and group chats
2. Personal information about client
3. Role played system
4. Notifications
5. Bot integration

Once this answer has been obtained, we can define the data we are working with.

### Database

Database we are going to use is postgres as the most popular database

Tables:
1. Users - store creds and basic info about user
2. Chats - private, group
3. Messages - text messages, photo or video, file
4. Roles - client, admin, worker
5. User profile
6. Notifications

All picies of data are related to other. For example User is a person that create chats, send messages, receive notifications and so on
So we should connect all data to each other and receive some diagram. It's called conceptual diagram.

```markdown
       +-----------------+          +-----------+          +----------------+
       |  Roles          | <------  |  Users    | <------- |  UserProfiles  |
       +-----------------+          +-----------+          +----------------+

       +-----------------+         +---------------+         +---------+
       |  Chats          |<------->|  ChatMembers  |<------->|  Users  |
       +-----------------+         +---------------+         +---------+

       +-----------------+       +---------+
       |                 |-----> |  Chats  |
       |   Messages      |       +---------+
       |                 |       +---------+
       |                 |-----> |  Users  |
       +-----------------+       +---------+

       +-----------------+       +---------+
       |  Notifications  |-----> |  Users  |
       +-----------------+       +---------+
```
