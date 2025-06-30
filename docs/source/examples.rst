Usage examples
==============

Simple high-level interface for SPFS to upload:

.. code-block:: python

  import asyncio

  import pystratos

  async def main():
      async with pystratos.AsyncSpfsClient(timeout=10) as client:
          data = b"test data"
          # upload the file
          await client.add(data, filename="test")

  asyncio.run(main())

and for retrieving the file content:

.. code-block:: python

  import asyncio

  import pystratos

  async def main():
      async with pystratos.AsyncSpfsClient(timeout=10) as client:
          cid = "Qmad1cvaBqojtaWW3ANjcEAYW7Zx8VKJeDGFxWTKPNivi1"
          # retrieve the file content
          content = await client.cat(cid, filename="test")
          print(f"{content=}")

  asyncio.run(main())

or with file encryption:

.. code-block:: python

  import asyncio

  import pystratos

  async def main():
    async with pystratos.AsyncSpfsClient(timeout=10) as client:
        with open("<your_file_path>", "rb") as f:
            encryption_key = b"wZcZyNXewdPeFdpv19SAlOTgfsM4aBY27ZKREReuFfM="
            # upload the file with encryption
            resp = await client.add(f, filename="test", encryption_key=encryption_key)
            # retrieve the file content
            content = await client.cat(resp["Hash"], encryption_key=encryption_key)
            print(f"{content=}")

  asyncio.run(main())
