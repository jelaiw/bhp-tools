import boto3
import botocore
import pprint

# See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html#session.
session = boto3.session.Session(profile_name="cg_scenario2")
iam = session.client("iam")

INDENT = "  "

print("Users")
print("=====")
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListUsers.html.
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_User.html.
users = iam.list_users()
for user in users['Users']:
#	pprint.pprint(user)
	# See https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals.
	print(f"{INDENT}{user['UserName']}")

print() # Newline for space between sections.
print("Groups")
print("======")
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html.
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_Group.html.
groups = iam.list_groups()
for group in groups['Groups']:
#	pprint.pprint(group)
	print(f"{INDENT}{user['GroupName']}")

print() # Newline for space between sections.
print("Access Keys")
print("===========")
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccessKeys.html.
response = iam.list_access_keys()
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_AccessKeyMetadata.html.
for metadata_record in response['AccessKeyMetadata']:
#	pprint.pprint(metadata_record)
	akey_id = metadata_record['AccessKeyId']
	user_name = metadata_record['UserName']
	print(f"{INDENT}Access Key ID = {akey_id}, Username = {user_name}")
