import boto3
import botocore
import pprint

# See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html#session.
session = boto3.session.Session(profile_name="cg_scenario1")
iam = session.client("iam")

# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html.
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_Group.html.
groups = iam.list_groups()
for group in groups['Groups']:
#	pprint.pprint(user['UserName'])
	pprint.pprint(group)

