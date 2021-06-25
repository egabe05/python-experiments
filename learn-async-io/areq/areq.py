import asyncio
import logging
import re
import sys
import urllib
from typing import IO, Mapping

import aiofiles
import aiohttp
from aiohttp import ClientSession

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')

async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
  resp = await session.request(method="GET", url=url, **kwargs)
  resp.raise_for_status()
  logger.info(f"Got response {resp.status} for URL: {url}")
  html = await resp.text()
  return html

async def parse(url: str, session: ClientSession, **kwargs) -> set:
  found = set()
  try:
    html = await fetch_html(url=url,session=session, **kwargs)
  except (aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as e:
    logger.error(f"aiohttp exception for {url} [{getattr(e, 'status', None)}]: {getattr(e, 'message', None)}")
    return found
  except Exception as e:
    logger.exception(f"Non-aiohttp exception occured: {getattr(e, '__dict__', {})}")
    return found
  else:
    for link in HREF_RE.findall(html):
      try:
        abslink = urllib.parse.urljoin(url, link)
      except (urllib.error.URLError, ValueError):
        logger.exception(f"Error parsing URL: {link}")
        pass
      else:
        found.add(abslink)
    logger.info(f"Found {len(found)} for {url}")
    return found

async def write_one(file: IO, url: str, **kwargs) -> None:
  res = await parse(url=url, **kwargs)
  if not res:
    return None
  async with aiofiles.open(file, "a") as f:
    for p in res:
      await f.write(f"{url}\t{p}\n")
    logger.info(f"Wrote results for source URL: {url}")


async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
  async with ClientSession() as session:
    tasks = []
    for url in urls:
      tasks.append(write_one(file=file, url=url, session=session, **kwargs))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
  import pathlib
  import sys

  assert sys.version_info >= (3, 7)
  here = pathlib.Path(__file__).parent

  with open(here.joinpath("urls.txt")) as infile:
    urls = set(map(str.strip, infile))

  outpath = here.joinpath("foundurls.txt")
  with open(outpath, "w") as outfile:
    outfile.write(f"source_url\tparsed_url\n")

  asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))
