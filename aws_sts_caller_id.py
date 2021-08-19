import boto3
import botocore
import pprint

# See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#creating-clients.
# See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client.
# Note STS is AWS Security Token Service.
# Note AWS profile is a CloudGoat scenario.
sts = boto3.session.Session(profile_name="cg_scenario1").client("sts")

# See https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html.
pprint.pprint(sts.get_caller_identity())
