import aws_cdk as core
import aws_cdk.assertions as assertions

from hive_dj_bot.hive_dj_bot_stack import HiveDjBotStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hive_dj_bot/hive_dj_bot_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HiveDjBotStack(app, "hive-dj-bot")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
