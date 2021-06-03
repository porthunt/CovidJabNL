import json
import argparse
import boto3
import requests


def send_email(email):
    client = boto3.client('ses',region_name="eu-west-1")
    client.send_email(
        Destination={
            'ToAddresses': [email],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': "UTF-8",
                    'Data': "Go to https://coronatest.nl, you can get vaccinated",
                },
            },
            'Subject': {
                'Charset': "UTF-8",
                'Data': "Covid jab",
            },
        },
        Source="Covid <co@vid.com>",
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Covid")
    parser.add_argument("--year", required=True, type=str)
    parser.add_argument("--email", required=True, type=str)
    args = parser.parse_args()

    response = requests.get(f"https://user-api.coronatest.nl/vaccinatie/programma/bepaalbaar/{args.year}/NEE/NEE")
    if json.loads(response.content).get("success"):
        send_email(args.email)
