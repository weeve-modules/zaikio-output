"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import requests
from os import getenv
from logging import getLogger

log = getLogger("module")

TOKEN = getenv("PERSONAL_ACCESS_TOKEN").strip()
METHOD = getenv("ENDPOINT", "POST /jobs").split(' ')[0]
URL = getenv("ZAIKIO_SERVER", "https://mc.sandbox.zaikio.com/api/v1") + getenv("ENDPOINT").split(" ")[1]
if "{job_id}" in URL:
    URL = URL.replace("{job_id}", getenv("OBJECT_ID").strip())
elif "{execution_id}" in URL:
    URL = URL.replace("{execution_id}", getenv("OBJECT_ID").strip())


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        log.info(f"Request: {METHOD} to URL: {URL}")
        if METHOD == 'POST':
            resp = requests.post(
                url=URL,
                json=received_data,
                headers={
                    'Authorization': f'Bearer {TOKEN}',
                    'Content-Type': 'application/json'
                }
            )
            if resp.status_code != 201:
                log.error(f"Error when sending request: {resp.json()}")
        elif METHOD == 'GET':
            resp = requests.get(
                url=URL,
                headers={
                    'Authorization': f'Bearer {TOKEN}',
                    'Content-Type': 'application/json'
                }
            )
            if resp.status_code == 200:
                log.info(f"Fetched data: {resp.json()}")
            else:
                log.error(f"Error when sending request: {resp.json()}")
        elif METHOD == 'PATCH':
            resp = requests.patch(
                url=URL,
                json=received_data,
                headers={
                    'Authorization': f'Bearer {TOKEN}',
                    'Content-Type': 'application/json'
                }
            )
            if resp.status_code != 200:
                log.error(f"Error when sending request: {resp.json()}")
        else: # METHOD == 'DELETE'
            resp = requests.delete(
                url=URL,
                headers={
                    'Authorization': f'Bearer {TOKEN}',
                    'Content-Type': 'application/json'
                }
            )
            if resp.status_code != 204:
                log.error(f"Error when sending request: {resp.json()}")

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
