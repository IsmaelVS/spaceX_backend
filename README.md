# spaceX_backend
----------------------------------
API do spaceX em django, tem o objetivo de exibir informações de lançamentos de foguetes.

## Requisitos

É necessário clonar o projeto seguindo o comando a baixo:
```bash
$ git clone https://github.com/IsmaelVS/spaceX_backend.git
```

Após o clone, é necessário instalar os `requirements.txt`.
###### Obs: No meu caso utilizo um ambiente virtual como boa prática.Para ativar o ambiente virtual`(opcional)`:
```bash
$ pipenv shell
```
## Build
Antes de iniciarmos o projeto é necessário rodar um comando para instalação do requiriments.txt.
```bash
$ pip install -r requeriments.txt
```
Após isso, execute o projeto com:

```bash
$ python3 api/manage.py runserver
```

### Como utilizar?

Devemos acesar via navegador, ou realizando requisições. Endpoints criados:
1. https://django-spacex.herokuapp.com/all_capsules
2. https://django-spacex.herokuapp.com/past_capsules
3. https://django-spacex.herokuapp.com/past_capsule
4. https://django-spacex.herokuapp.com/upcoming_capsules
5. https://django-spacex.herokuapp.com/upcoming_capsule

#### Obs: tem uma aplicação web consumindo esta API, pode ser utilizado por lá, através do link:


```
https://frontend-spacex.herokuapp.com/
```
