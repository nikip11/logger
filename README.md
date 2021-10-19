# logger

## Queue
### Publisher

- Save log by endpoint
http://localhost:5000/logs
```
{
    "name": "prueba7",
    "enviroment": "dev",
    "type": "error",
    "line": 102,
    "url": "https://app.es",
    "user": {
        "username": "user@email.es",
        "name": "Ivan"
    },
    "browser": "brave",
    "ip": "localhost",
    "meta": {}
}
```

### Consumer

## Services

### Proxy and letsencrypt
```
.env
VIRTUAL_HOST= virtual host
VIRTUAL_PORT= expose port
VIRTUAL_NETWORK=proxy
```

### RabbitMQ
```
RABBITMQ_ERLANG_COOKIE=ASKKJDHAIEIDKCNVKKD
RABBITMQ_DEFAULT_USER=admin
RABBITMQ_DEFAULT_PASS=admin
RABBITMQ_DEFAULT_VHOST=/
```

### MongoDB