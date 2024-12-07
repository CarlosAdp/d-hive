from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_lambda as _lambda
)
from constructs import Construct


class HiveDjBotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = apigateway.RestApi(
            self, 'HiveDjBotApi',
            rest_api_name='HiveDjBotApi',
            description='This service receives Discord bot commands to the '
            'HiveDJBot',
        )

        event = api.root.add_resource(
            'event',
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_methods=['GET', 'POST'],
                allow_origins=apigateway.Cors.ALL_ORIGINS,
            ),
        )

        event_handler_lambda = _lambda.Function(
            self, 'HiveDjBotEventHandler',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('lambda'),
            handler='event_handler.handler',
        )

        event.add_method(
            'POST',
            apigateway.LambdaIntegration(event_handler_lambda),
        )
