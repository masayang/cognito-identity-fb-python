from __future__ import print_function
import boto3
import json
from settings import config
from jinja2 import Environment, FileSystemLoader
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

client = boto3.client('cognito-identity', region_name=config['AWS']['REGION'])

def get_id(token):
    logger.debug("Token = " + token)
    try:
        return client.get_id(
            AccountId=config["AWS"]["ACCOUNT_ID"],
            IdentityPoolId=config["AWS"]["IDENTITY_POOL_ID"],
            Logins= {
                'graph.facebook.com': token
            }
        )
    except Exception as e:
        return {
            "IdentityId": None,
            "Error": str(e)
        }

def create_policy(token):
    identity = get_id(token)
    logger.debug(json.dumps(identity))
    values = {}
    if identity["IdentityId"]:
        values['permission'] = "Allow"
    else:
        values['permission'] = "Deny"

    values['resouce_restricted'] = config["API"]["BASE_ARN"] + "*/authorized/*"
    values['resource_guest'] = config["API"]["BASE_ARN"] + "*/guest/*"

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.json')
    ret = template.render(values=values)
    logger.debug(ret)
    return json.loads(ret)


def lambda_handler(event, context):
    token = event['authorizationToken'].split(' ')[1]
    return create_policy(token)

if __name__ == '__main__':
    print(create_policy('EAAWyaqmqZCZB0BAGNebCvzvDJEaoVeJkjp1dAG939Gf8mnmh2fLPByUhUuetcPgM8keF9vn8PHvulc6eSmOQMkDXJeZCBZCx1CqMBeTIhbyKhIpev0dnV1lyN6u6x6GXhZCdL85rQDiJxiBfGvsriPJJef5S33LAN0ROehE3gcX0EnGHBCL7ZAczz3Bb6agshb9hsaajVeKVNilDax1T0I7T1fiNR4la0ZD'))