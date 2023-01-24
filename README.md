## API Endpoints

This API implements the following routes:

| **Endpoint**     	| **HTTP method**   | **CRUD method** 	| **Description**      	                            |
|-----------------	|----------------  	|---------------	|---------------------------------------------------|
| `/convert`     	| POST           	| CREATE        	| Calculate converted amount and mid-market rate    |
| `/history`     	| GET           	| READ        	    | List all previously made convertions              |
| `/currencies`     | GET           	| READ        	    | List all supported currencies              |


## Build and Run
To buld and run. This will also run migrations automatically.  

```bash
$ docker-compose build
```
To confirm that everything works, access the healthcheck endpoint with 

```
http://localhost:8000/healthcheck
```

## API documentation 

To access the swagger api documentation use.  
```
http://localhost:8000/docs
```

Alternatively, you can access the redoc documentation 

```
http://localhost:8000/redoc
```


## Run the Tests

The tests can be executed with:

```bash
$ docker-compose run --rm mid-market-rate pytest
```

## Check for Code Quality

To confirm proper code formatting use, black 

```bash
$ docker-compose run --rm mid-market-rate black . --check
```

## Things to Improve

1. Optimize convert endpoint by researching mid market rate volatiliy parterns and incorporating it in the implementation