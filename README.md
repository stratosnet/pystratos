# Pystratos

Pystratos is a fully-featured Python 3 client library for interacting with Stratos services.

Install Pystratos using pip:

```shell
$ pip install pystratos
```

## Documentation

https://pystratos.readthedocs.io/en/latest/

## Usage examples

Simple high-level interface for SPFS to upload:

```pycon
import asyncio

import pystratos

async def main():
    async with pystratos.AsyncSpfsClient(timeout=10) as client:
        data = b"test data"
        # upload the file
        await client.add(data, filename="test")

asyncio.run(main())
```

and for retrieving the file content:

```pycon
import asyncio

import pystratos

async def main():
    async with pystratos.AsyncSpfsClient(timeout=10) as client:
        cid = "Qmad1cvaBqojtaWW3ANjcEAYW7Zx8VKJeDGFxWTKPNivi1"
        # retrieve the file content
        content = await client.cat(cid, filename="test")
        print(f"{content=}")

asyncio.run(main())
```

or with file encryption

```pycon
import asyncio

import pystratos

async def main():
    async with pystratos.AsyncSpfsClient(timeout=10) as client:
        with open("<your_file_path>", "rb") as f:
            encryption_key = b"wZcZyNXewdPeFdpv19SAlOTgfsM4aBY27ZKREReuFfM="
            resp = await client.add(f, filename="test", encryption_key=encryption_key)
            content = await client.cat(resp["Hash"], encryption_key=encryption_key)
            print(f"{content=}")


asyncio.run(main())
```

NOTE: You need to install optional dep `pystratos[crypto]` for encryption
