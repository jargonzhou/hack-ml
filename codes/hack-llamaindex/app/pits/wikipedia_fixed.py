"""
Workaround /w/api.php 403.

see also: https://www.mediawiki.org/wiki/API
"""

import requests
from llama_index.core import Document
from llama_index.readers.wikipedia import WikipediaReader
import wikipedia

wikipedia.set_user_agent(
    "EnterpriseDataPipeline/2.0 (contact@yourcompany.com; bot) Requests/Internal")


class FixedWikipediaReader(WikipediaReader):
  def load_data(self, pages, lang_prefix="en", **kwargs):
    """Direct API injection bypasses the faulty library middleware wrapper."""
    results = []
    session = requests.Session()

    # Explicit headers complying with Wikimedia Foundation Policy
    session.headers.update({
        "User-Agent": "EnterpriseDataPipeline/2.0 (contact@yourcompany.com; bot) Requests/Internal",
        "Accept-Encoding": "gzip"
    })

    for page in pages:
      # Explicitly route directly to the localized Wikipedia API endpoint
      url = f"https://{lang_prefix}.wikipedia.org/w/api.php"
      params = {
          "action": "query",
          "format": "json",
          "prop": "extracts",
          "titles": page,
          "explaintext": True,
          "exlimit": "max"
      }

      response = session.get(url, params=params)
      if response.status_code == 403:
        raise PermissionError(
            f"Wikipedia still returned 403. Details: {response.text}")

      data = response.json()
      pages_dict = data.get("query", {}).get("pages", {})

      for page_id, page_data in pages_dict.items():
        if page_id != "-1" and "extract" in page_data:
          wp = self.get_wikipedia_content_by_id(
              session=session, page_id=page_id)
          # print(wp)
          results.append(Document(
              text=wp["content"],
              extra_info={"title": wp["title"], "page_id": page_id}
          ))
    return results

  def get_wikipedia_content_by_id(self, session, page_id, lang="en"):
    """Get page by pageid."""
    url = f"https://{lang}.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "pageids": page_id,
        "explaintext": True,  # Strips HTML/MediaWiki syntax into raw text
        "exlimit": "max"      # Returns the full text, not a summary snippet
    }

    response = session.get(url, params=params)

    if response.status_code != 200:
      print(f"HTTP Error: {response.status_code}")
      return None

    data = response.json()

    # Extract data safely from the nested JSON response
    pages = data.get("query", {}).get("pages", {})

    # Convert page_id to string since JSON keys are always strings
    page_data = pages.get(str(page_id))

    if not page_data or "-1" in pages:
      print(f"Page ID {page_id} not found.")
      return None

    return {
        "title": page_data.get("title"),
        "content": page_data.get("extract", "").strip()
    }


#
# test
#
# reader = FixedWikipediaReader()
# documents = reader.load_data(pages=['Artificial intelligence'])
# # documents = reader.load_data(pages=['Messi Lionel']) # No data
# print(documents)
# print(f"Success! Loaded {len(documents)} page securely.")
