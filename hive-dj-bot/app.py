#!/usr/bin/env python3
import os

from dotenv import load_dotenv
import aws_cdk as cdk

from hive_dj_bot.hive_dj_bot_stack import HiveDjBotStack

load_dotenv()

app = cdk.App()
HiveDjBotStack(
    app, "HiveDjBotStack", env=cdk.Environment(
        account=os.getenv('CDK_ACCOUNT'), region=os.getenv('CDK_REGION')
    )
)

app.synth()
