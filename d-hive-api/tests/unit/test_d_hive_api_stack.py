import aws_cdk as core
import aws_cdk.assertions as assertions

from d_hive_api.d_hive_api_stack import DHiveApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in d_hive_api/d_hive_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DHiveApiStack(app, "d-hive-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
