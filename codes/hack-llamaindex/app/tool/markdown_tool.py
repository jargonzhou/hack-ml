from llama_index.core.tools import FunctionTool


def write_to_markdown_tool(content: str, filename: str = "output.md") -> str:
  """Writes the given text content directly into a local Markdown (.md) file."""
  try:
    # Ensure it ends with .md extension
    if not filename.endswith(".md"):
      filename += ".md"

    with open(filename, "w", encoding="utf-8") as f:
      f.write(content)
    return f"Successfully saved content to {filename}"
  except Exception as e:
    return f"Failed to save file due to error: {str(e)}"


# Convert the function into a LlamaIndex-compatible Tool
markdown_tool = FunctionTool.from_defaults(fn=write_to_markdown_tool)
