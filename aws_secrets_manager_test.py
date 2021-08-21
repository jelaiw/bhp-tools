import boto3
import botocore
import pprint

secrets_manager = boto3.session.Session().client("secretsmanager")
# See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html.
secrets = secrets_manager.list_secrets()
#pprint.pprint(secrets)

# See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html.
response = secrets_manager.get_random_password(PasswordLength=22)
#pprint.pprint(response)

# See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html.
#admin_password = secrets_manager.create_secret(Name="admin_password", SecretString=response['RandomPassword'])

# Confirm secret is created.
secrets = secrets_manager.list_secrets()
pprint.pprint(secrets)

response = secrets_manager.get_secret_value(SecretId="admin_password")
#pprint.pprint(response)
pprint.pprint(response['SecretString'])
