#!/bin/zsh
AWSREGION=TBD
CFNS3BUCKETNAME=TBD
STAGE=TBD
APINAME=TBD
LAYER_ARN=TBD

# Workaround to include only fastapi_serverless-folder in deployment package
mkdir ./../.sam-package
cp -r ./../fastapi_serverless ./../.sam-package

sam deploy --stack-name "${STAGE}-${APINAME}" \
    -t ./../sam/template.yaml \
    --region $AWSREGION \
    --s3-bucket $CFNS3BUCKETNAME \
    --s3-prefix ${APINAME} \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides \
        ParameterKey=Stage,ParameterValue=${STAGE} \
        ParameterKey=LayerARN,ParameterValue=${LAYER_ARN}

rm -r ./../.sam-package
