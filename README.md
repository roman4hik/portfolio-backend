# Portfolio backend application

## Set up application


0. For development purposes install `pipenv` (for system, not for current environment)
1. Install docker and docker-compose
2. Create `.env` file where you need to define variables like in env.example file:
3. Create `postgres.env` file and specify next variables(necessary for configuring docker container with postgres):
 - `POSTGRES_USER`
 - `POSTGRES_PASSWORD`
 - `POSTGRES_DB`
 
 
Now when you have your `.env` file you can run you postgres db `docker-compose up -d postgres`,

Or you can use shortcuts:
 - `pipenv run postgres` - run container with DB


