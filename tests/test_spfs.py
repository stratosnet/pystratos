import pytest

from pystratos.spfs import AsyncSpfsClient


@pytest.mark.asyncio
async def test_encrypt_and_decrypt():
    async with AsyncSpfsClient(timeout=10) as client:
        encryption_key = b"test_key_12345678901234567890"
        data = b"test data"
        resp = await client.add(data, filename="test", encryption_key=encryption_key)
        assert resp["Hash"] is not None, "File should be added successfully"

        content = await client.cat(resp["Hash"], encryption_key=encryption_key)
        assert content == data, "Decrypted content should match original data"


@pytest.mark.asyncio
async def test_no_encryption():
    async with AsyncSpfsClient(timeout=10) as client:
        data = b"test data"
        resp = await client.add(data, filename="test")
        assert resp["Hash"] is not None, "File should be added successfully"

        content = await client.cat(resp["Hash"])
        assert content == data, "Content should match original data"
