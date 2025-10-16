import asyncio #used for concurrent programming, including the use of async iterator in Python

import json
import os
from typing import Optional
from contextlib import AsyncExitStack #Utilities for with-statement contexts

from mcp import ClientSession
from mcp.client.sse import sse_client

from openai import OpenAI
from openai.types import Completion
from dotenv import load_dotenv

load_dotenv() #load env from .env

class MCPClient:
    def __init__(self):
        #Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.openai = OpenAI(
            api_key=os.getenv("OPEN_API_KEY")
        )

        self.available_tools = []
        self.messages = []

    async def connect_to_sse_server(self, server_url: str):
        """ Connect to MCP server running with SSE Transport """
        print("Connecting to MCP SSE server...")

        # Store the context managers so they stay alive

        self._streams_context = sse_client(url=server_url)

        """
        self._session_context is an asynchronous context manager.

        It implements the methods __aenter__ and __aexit__.

        These methods are how Python manages setup and teardown for async with.

        """
        streams = await self._streams_context.__aenter__()

        #initialzie

        print("Initializing SSE Client...")
        await self.session.initialize()

        print("Initialized SSE Client!")

        #list available tools to verify connection
        await self.get_available_tools();
        await self.get_initial_prompts();

    async def cleanup(self):
        """
            clean up the session and streams
        """

        if self._streams_context:   
            await self._streams_context.__aexit__(
                    None, #type baseExcepion
                    None, #BaseException
                    None #Traceback exception
                    )
        if self._streams_context:
            await self._streams_context.__aexit__(None, None, None)
