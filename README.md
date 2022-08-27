# streamlit-template
### Setup
```sh
$ poetry install
$ cd streamlit_sample
```

### Start at any address and port
```sh
$ poetry run streamlit run --server.address localhost --server.port 8501 Hello.py
```
### Dockerize
```sh
$ docker build -t sample/hello .
$ docker run --rm -d -p 8501:8501 sample/hello
#$ docker run --rm -d -v ${PWD}/:/opt/app -p 8501:8501 sample/hello
```