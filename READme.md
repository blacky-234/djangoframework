### Docker running Postgresql

```bash
sudo docker run -it -p 5432:5432 --name djangoframework -e POSTGRES_USER=djangouser -e POSTGRES_PASSWORD=djangomypassword -e POSTGRES_DB=djangomydb -d fbd9a209d4e8 

```
### docker container ip address find 

```bash

docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>

```