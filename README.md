# ideal-succotash

demo to figure out server-sent events with bottle and rpyc

## to run

```sh
pipenv install
```

in one (`pipenv`) shell

```sh
python server.py
```

in another (`pipenv`) shell

```sh
python client.py
```

go to <http://localhost:8080/>

submit the form

watch the real-time log file streamed to the browser window

## notes

`gevent` server is needed with bottle; the WSGIRefServer did not handle the `yield`s well
