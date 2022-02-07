# Flask-APIX
an authentication Microservice/API

## Running MYSQL Docker
`docker run --rm -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=<password> -e MYSQL_DATABASE=apix -e MYSQL_USER=<user> -e MYSQL_PASSWORD=<password> mysql`

## Define Connection String
`export AUTHZ_DATABASE_URI=mysql+pymysql://<user>:<password>@localhost:3306/apix`

## DB Migration and Getting Started
`flask db init`

`flask db migrate -m "initial migrate" ` 

`flask db upgrade`

## Run Flask
`flask run`

## Create a User
`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/users -d ‘{“username”:”<username>”,”password”:”<password>”}’ `

`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/users -d ‘{“username”:”<username>”,”password”:”<password>”}’`

## Get a Token
`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/auth/tokens -d ‘{“username”:”<username>”,”password”:”<password>”}’ `

## Get List of Users
`curl -i -H 'Content-Type: application/json' localhost:5000/api/v1/auth/tokens -H 'X-Auth-Token: {token}’ `

