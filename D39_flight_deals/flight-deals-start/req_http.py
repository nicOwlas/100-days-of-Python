"""Async http requests"""
import asyncio

import requests

# From: https://github.com/ArjanCodes/2022-asyncio/blob/main/req_http.py

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def http_get_sync(
    url: str, params: dict = None, headers: dict = None, timeout: int = 30
) -> JSONObject:
    """Sync requests get function"""
    response = requests.get(url, params, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()


async def http_get(
    url: str, params: dict = None, headers: dict = None, timeout: int = 30
) -> JSONObject:
    """Async requests get function"""
    return await asyncio.to_thread(http_get_sync, url, params, headers, timeout)
