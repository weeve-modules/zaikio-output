# Zaikio Output

|           |                                                                      |
| --------- | -------------------------------------------------------------------- |
| Name      | Zaikio Output                                                        |
| Version   | v1.0.0                                                               |
| DockerHub | [zaikio-output](https://hub.docker.com/r/weevenetwork/zaikio-output) |
| Authors   | Jakub Grzelak                                                        |

- [Zaikio Output](#zaikio-output)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Send requests to [Zaikio API Mission Control](https://docs.zaikio.com/api/mission_control/api.html). At the moment, this module supports only Jobs, Jobs Finished Work and Execution operations. You will need [Personal Access Token to Zaikio Mission Control](https://docs.zaikio.com/guide/try-api/#step-1-generate-private-access-token)

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                  | Environment Variables | type   | Description                                                                                                                                                   |
| --------------------- | --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Personal Access Token | PERSONAL_ACCESS_TOKEN | string | Personal Access Token to Zaikio Mission Control. [Instructions how to generate.](https://docs.zaikio.com/guide/try-api/#step-1-generate-private-access-token) |
| Zaikio Server         | ZAIKIO_SERVER         | string | Zaikio server to send requests to. Production (https://mc.zaikio.com/api/v1) or Sandbox Test Server (https://mc.sandbox.zaikio.com/api/v1).                   |
| Endpoint              | ENDPOINT              | string | Zaikio API method and endpoint to send data to. See all methods [here](https://docs.zaikio.com/api/mission_control/api.html)                                  |
| Object ID             | OBJECT_ID             | string | Provide object's ID if the above endpoint request needs Job ID or Execution ID.                                                                               |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is:

-   JSON body single object. To create a new job by setting endpoint `POST /jobs` input data could be:

```json
{
    "job": {
        "name": "My first Job",
        "kind": "business_card",
        "source": "Mission Control Tutorial",
        "version": "1",
        "quantity": 1
    }
}
```

## Output

There is no output for this module.
