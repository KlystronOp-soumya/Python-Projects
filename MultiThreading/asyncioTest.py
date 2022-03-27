import asyncio
import pytest
import main

@pytest.mark.asyncio
async def test_main(capsys):
    await main.question()
    cpt = capsys.readouterr()
    assert cpt.out == """Is asyncio better for IO bound programs than the CPU bound ones?
Yes, it is!
Is async a keyword in the latest Python3?
Yes, it is!
Is event loop the heart of an asyncio program?
Yes, it is!
"""