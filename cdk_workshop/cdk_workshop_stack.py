from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_sns_subscriptions as subs,
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_lambda = aws_lambda.Function(
            self, 'HelloHandler',
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            code=aws_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )
