## API Endpoints

This API implements the following routes:

| **Endpoint**     	| **HTTP method**   | **CRUD method** 	| **Description**      	                            |
|-----------------	|----------------  	|---------------	|---------------------------------------------------|
| `/convert`     	| POST           	| CREATE        	| Calculate converted amount and mid-market rate    |
| `/history`     	| GET           	| READ        	    | List all previously made convertions              |
| `/currencies`     | GET           	| READ        	    | List all supported currencies                     |


## Build and Run
To build and run. This will also run migrations automatically.  

```bash
$ docker-compose build
```
To confirm that everything works, access the healthcheck endpoint with 

```
curl -H "Authorization: Bearer 004cec70-142d-4535-961b-4919a5d58ad3" http://localhost:8000/healthcheck

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

## Some notes on the implemetation 

Since supported currencies are not expected to change much,
we store them in the db to cust down the response time for subsequent 
retrievals 

We could explore same logic for the conversion but we have to first 
figure out how how rapidly the rates changes over time. 



## Things to Improve

1. Optimize convert endpoint by researching mid market rate volatiliy parterns and incorporating it in the implementation
2. Improve logging 
