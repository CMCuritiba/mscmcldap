# Aplicação Micro Services LDAP CMC

Aplicação django que fornece micro serviços para os sistemas da Câmara Municipal de Curitiba

[<img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg">](https://github.com/pydanny/cookiecutter-django/) [<img src="https://travis-ci.org/CMCuritiba/mscmcldap.svg?branch=master">](https://travis-ci.org/CMCuritiba/mscmcldap) [<img src="https://codecov.io/gh/CMCuritiba/mscmcldap/coverage.svg?branch=master">](https://codecov.io/gh/CMCuritiba/mscmcldap/)

| License | MIT |
|---------|-----|

## Aplicação com containers

Para subir a aplicação em um container:

1. Instale os pacotes do docker:

   ```shell
   apt install docker.io docker-compose-v2 docker-buildx
   ```

2. Configure as variáveis de ambiente de acordo com o
   [docker compose](./docker-compose.yml);
3. Suba o cluster (isto também irá fazer o build da imagem):

   ```shell
   docker compose up
   ```

4. Para fazer o build da imagem sem utilizar o compose:

   ```shell
   docker build -t mscmc:latest .
   ```

5. Para desfazer o cluster:

   ```shell
   docker compose down
   ```

> [!WARNING]  
> As migrations não são realizadas no script de entrypoint.

As migrations podem ser executadas manualmente sob demanda dentro do container:

```shell
# Acesse o container:
docker container exec -it mscmcldap-mscmc-1 bash
# Rode as migrations dentro do container:
python3 manage.py makemigrations --settings=config.settings.production
python3 manage.py makemigrations api --settings=config.settings.production
python3 manage.py migrate api --settings=config.settings.production
```
