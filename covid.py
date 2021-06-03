#!/usr/bin/env python3
import json
import argparse
import boto3
import requests


def send_email(dest, source, year):
    client = boto3.client('ses',region_name="eu-west-1")
    client.send_email(
        Destination={
            'ToAddresses': [dest],
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
                'Data': f"{year} Covid jab",
            },
        },
        Source=source,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Covid")
    parser.add_argument("--year", required=True, type=str)
    parser.add_argument("--dest-email", required=True, type=str)
    parser.add_argument("--source-email", required=True, type=str)
    args = parser.parse_args()

    response = requests.get(f"https://user-api.coronatest.nl/vaccinatie/programma/bepaalbaar/{args.year}/NEE/NEE")
    if json.loads(response.content).get("success"):
        send_email(args.dest_email, args.source_email, args.year)
