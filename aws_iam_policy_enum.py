import boto3
import botocore
import pprint

# See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#creating-clients.
# See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client.
# Note AWS profile is a CloudGoat scenario.
iam = boto3.session.Session(profile_name="cg_scenario1").client('iam')

# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html.
# Note RoleDetailList and UserDetailList in output (JSON format).
pprint.pprint(iam.get_account_authorization_details())

