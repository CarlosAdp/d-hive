#!/usr/bin/env python3
import os

from dotenv import load_dotenv
import aws_cdk as cdk

from d_hive_api.d_hive_api_stack import DHiveApiStack

load_dotenv()

app = cdk.App()
DHiveApiStack(
    app,
    "DHiveApiStack",
    env=cdk.Environment(
        account=os.getenv('CDK_ACCOUNT'), region=os.getenv('CDK_REGION')
    )
)

app.synth()
