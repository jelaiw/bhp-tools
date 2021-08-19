import boto3
import botocore
import pprint

guardduty = boto3.session.Session(region_name="us-east-2").client("guardduty")
# See https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html.
response = guardduty.list_detectors()
#pprint.pprint(response)

guards = response['DetectorIds']
if len(guards) > 0:
	print(guards[0])
else:
	print("No guards on duty in this region.")
