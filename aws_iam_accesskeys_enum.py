import boto3
import botocore
import pprint

# See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html#session.
session = boto3.session.Session(profile_name="cg_scenario1")
iam = session.client("iam")

# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html.
response = iam.list_access_keys()
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKeyMetadata.html.
for metadata_record in response['AccessKeyMetadata']:
#	pprint.pprint(metadata_record)
	akey_id = metadata_record['AccessKeyId']
	user_name = metadata_record['UserName']
	print("Access Key ID = {0}, Username = {1}".format(akey_id, user_name))

