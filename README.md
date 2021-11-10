# logger
127.0.0.1       log.io              =>
127.0.0.1       rabbitmq.dev.io     =>
127.0.0.1       dashboard.io        =>
127.0.0.1       api.dashboard.io    =>
127.0.0.1       portainer.dev.io    =>
## Queue
### Publisher

- Save log by endpoint
http://log.io/logs
```
{
    "name": "prueba7",
    "enviroment": "dev",
    "type": "error",
    "line": 102,
    "url": "https://app.es",
    "created_at": "2021-10-23T13:54:29.707984",
    "user": {
        "username": "user@email.es",
        "name": "Testuser"
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

## TO-DO
- Connect Symfony to rabbitMQ
- On production
    - Flask
    - RabbitMQ
### ```Team```
- Catch all js errors
- Create LogService on vue
- Create LogService on symfony
- Define objecto to save