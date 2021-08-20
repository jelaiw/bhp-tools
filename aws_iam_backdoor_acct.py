import boto3
import botocore
import pprint

iam = boto3.session.Session(region_name="us-east-2").client('iam')

# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateUser.html.
sys_user = iam.create_user(UserName="sys")
pprint.pprint(sys_user)
# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateLoginProfile.html.
login_profile = iam.create_login_profile(UserName="sys", Password="hack3r!1")
pprint.pprint(login_profile)

# See https://docs.aws.amazon.com/IAM/latest/APIReference/API_AddUserToGroup.html.
#admins_group = iam.add_user_to_group(UserName="sys", GroupName="admins")


