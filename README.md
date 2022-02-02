# What is Fastapi-Serverless?

Simple and basic example to demonstrate how to run FastAPI on AWS Lambda Serverless environment.

## Key tehcnology and components:

* AWS API Gateway and Lambda for REST API deployment and hosting
* [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) for AWS infra deployment
* [Fastapi](https://fastapi.tiangolo.com/) for enabling solutions for all above three challenges
* [Mangum](https://github.com/jordaneremieff/mangum) for enabling ASGI server on Lambda
* [Poetry](https://python-poetry.org/) for Python project and dependency management
* Docker for building AWS Lambda layer

### ASGI

* Python specific [standard](https://asgi.readthedocs.io/en/latest/specs/main.html), asyncronous successor for long lived WSGI
* Intends to provide a standard interface between async-capable Python web servers, frameworks, and applications
* Enables separating protocol specific server and application server concerns in to separate components

## User guide

NOTE: Precondition is to have Python and Poetry installed.

Install the project dependencies:
```
poetry install
```

Run FastAPI application locally:
```
poetry run uvicorn fastapi_serverless.app:app --reload
```

Access the interactive docs:
http://127.0.0.1:8000/docs

# Deployment to AWS

## Creating AWS Lambda Layer

Lambda Layer contains all the python dependencies. Using layer is optional but it's a convenient way to make lambda deployment more efficient.

Run the script to build lambda_layer.zip:
``` zsh
cd scripts
./make_layer.sh
```

Follow the [instructions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) on how to create Lambda Layer. Lambda Layer ARN is required in next step.

## Deploying FastAPI application to Lambda

Project root contains file deploy_TEMPLATE.sh. Update the placeholder attributes (e.g. Lambda Layer ARN) and run the deployment:
``` zsh
cd scripts
./deploy.sh
```

In AWS console navigate to API Gateway and find your newly deployed API (e.g. dev-fastapi-serverless). Under "Stages" find the "Invoke URL".

Access the interactive docs:
<Invoke URL>/docs

# Destroy AWS resources

Delete SAM deployment:
```zsh
sam delete --region <AWS_REGION> --stack-name <STACK_NAME>
```

Remember also delete the created AWS Lambda layer.

