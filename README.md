python tracing
==============

A sample `python` web server app, with distributed tracing configured
and instrumented logging with using [automatic instrumentation](https://opentelemetry.io/docs/instrumentation/python/automatic/).


The app serves 2 routes:
* http://localhost:8000/. Returns "hello world".
* http://localhost:8000/nodejs. Returns "hello world" returned from a [nodejs](https://github.com/uishon/nodejs-tracing) backend.

Setup
-----
```
pip install -r requirements.txt
opentelemetry-bootstrap -a install 
```

Usage
-----

To start the app *without* instrumentation
```
python3 app.py
```

To start the app *with* instrumentation
```
export OTEL_PYTHON_LOG_CORRELATION=true  # add correlation ID to logged messages 
opentelemetry-instrument --traces_exporter console --metrics_exporter="" python app.py
```

To start the app *with* instrumentation exported to an otlp cloud service, `--traces_exporter console` should be replaced with the `--traces_exporter otlp`.
```
export OTEL_PYTHON_LOG_CORRELATION=true  # add correlation ID to logged messages 
opentelemetry-instrument --traces_exporter otlp --metrics_exporter= --exporter_otlp_endpoint http://localhost:4317 --exporter_otlp_traces_insecure true --service_name python python app.py
```


Log Shipping
------------
To make the logged output ready to be consumed by log shippers, logged output should be in
JSON-line formatted. This requires changing the python logging configuration to use a JSON handler
(e.g., [this](https://pypi.org/project/python-json-logger/)).

Exporting Traces
----------------
To ship traces to a cloud service

References
----------
1. Sample `python` app with distributed tracing on CNCF blog [here](https://www.cncf.io/blog/2022/04/22/opentelemetry-and-python-a-complete-instrumentation-guide/).
2. Official `python auto instrumentation [here](https://opentelemetry.io/docs/instrumentation/python/automatic/).
