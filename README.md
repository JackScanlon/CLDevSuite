# Summary
Dockerised Django Boilerplate for my personal use.

Boilerplate includes (with examples):
  1. Django AllAuth
  2. SCSS processor
  3. Celery
  4. Redis
  5. ElasticSearch
  6. Gunicorn
  7. Nginx

Localisation & Internationalisation is included, but can be turned off in the ```./env/app.compose.env``` configuration file.

Leverages Gunicorn and Nginx for production builds.

# Superuser
> **Note:** The default params for this development account can be changed in ```./env/app.compose.env```, or you can make changes to the tool in ```./app/tools/create_superuser.py```

When ```Debug=1``` the app will create a superuser with the username of `admin` (admin@admin.com) and a password of `admin`.

# To develop
1. Create a virtual environment:
```sh
python -m venv venv
```
2. Install requirements
```pip
pip install -r requirements.txt
```
3. References to the assoc. packages will now be available in your editor and/or IDE.

# To run

> **Note:** ElasticSearch may complain that you do not have enough memory on your VM.
>
> If you're using Windows as your local machine, you can run the following command to solve this issue:
> ```
> wsl -d docker-desktop sysctl -w vm.max_map_count=262144
> ```

### Production
1. Change the env variables in ```./env```, esp. ensuring that ```DEBUG=0```
2. In the root directory of the repo, run the following:
```sh
docker-compose -f docker-compose.prod.yml build
```
3. Now run:
```sh
docker-compose -f docker-compose.prod.yml up
```
4. Navigate to http://localhost:8000

### Development
1. Change the env variables in ```./env```, esp. ensuring that ```DEBUG=1```
2. In the root directory of the repo, run the following:
```sh
docker-compose -f docker-compose.dev.yml build
```
3. Now run:
```sh
docker-compose -f docker-compose.dev.yml up
```
4. Navigate to http://localhost:8008

# To remove docker assoc. volumes/containers/images:

### Removing dev container
```sh
docker-compose -f docker-compose.dev.yml down
```

### Removing prod container
```sh
docker-compose -f docker-compose.prod.yml down
```

### Remove dangling images

> **Note:** The following will remove all dangling images, incl. those not assoc. with the boilerplate (be careful!)

```sh
docker rmi -f $(docker images -aq)
```

### Remove dangling volumes

> **Note:** The following will remove all dangling images, incl. those not assoc. with the boilerplate (be careful!)

```sh
docker volume rm $(docker volume ls -qf dangling=true)
```