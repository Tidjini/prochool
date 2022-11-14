# PROCHOOL

Simple management school system, to handle absences and presences, with memebership for students

## Contents

[TOC]

## Students

Student application contiane this folow models, packed all students behavior:

- Subscription
- Student detailed informaitons, like parents and establishments

## Database Sample

![database_diagram](./docs/images/database_diagram.png)

## CORS HEADERS

### Problems

Browser can hide you from resources from a different domain, (you can use just your domain or sub)
Cross-Origin Resources Sharing come to rescue

- Access-Control-Allow-Origin: to allow the use of our resources
- Access-Control-Allow-Headers: to allow the send requests with specifics headers
- Access-Control-Allow-Creadentials | 'true': to allow cockies

# Some todos for Tidjini:

- CRUD operations for all objects.
- useful queries ? don't know
- Business Logic:
  - open course
  - set student and presence
  - create a payment
  - confirm a payment (Barre Code)
  - cancel presence
  - cancel payment
  - reporting stuff
