from mcp.server.fastmcp import FastMCP
import httpx
import fitz
import os

mcp = FastMCP('app_mcp')

################################################################
# Resource
################################################################
RESOURCE_FOLDER = 'data/'


@mcp.resource("text://{file_path}")
def get_file(file_path: str) -> str:
  """Get text file content."""
  p = os.path.abspath(RESOURCE_FOLDER+file_path)
  if not os.path.exists(p):
    raise FileNotFoundError(f"Error: File '{p}' not found!")
  with open(p, 'r', encoding='utf-8') as f:
    return f.read()


@mcp.resource("config://app")
def get_config() -> str:
  """Statci configuration data"""
  return "Version 0.1.0"


@mcp.resource("pdf://{file_path}")
def get_pdf_data(file_path: str) -> str:
  """Get PDF file content."""
  text = ""
  p = os.path.abspath(RESOURCE_FOLDER+file_path)
  if not os.path.exists(p):
    raise FileNotFoundError(f"Error: File {p} not found!")
  with fitz.open(p) as f:
    for page in f:
      text += page.get_text() + "\n"
  return text

################################################################
# Tool
################################################################


@mcp.tool()
async def fetch_weather(city: str = 'Shanghai') -> dict:
  """Fetch weather data."""
  async with httpx.AsyncClient() as client:
    response = await client.get('https://api.open-meteo.com/v1/forecast?latitude=31.23&longitude=121.47&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')
    if response.status_code == 200:
      data = response.json()
      return data
    else:
      return {
          "error": f"Weather data not avaiable. Status code: {response.status_code}",
          "message": response.text
      }


@mcp.tool()
def convert_temperature(temp: float,
                        from_unit: str,
                        to_unit: str) -> float:
  """Convert temperature."""
  if from_unit.lower() == "celsius":
    kelvin = temp + 273.15
  elif from_unit.lower() == "fahrenheit":
    kelvin = (temp + 459.67) * 5/9
  elif from_unit.lower() == "kelvin":
    kelvin = temp
  else:
    raise ValueError(f"Unsupported unit: {from_unit}")

  if to_unit.lower() == "celsius":
    return kelvin - 273.15
  elif to_unit.lower() == "fahrenheit":
    return kelvin * 9/5 - 459.67
  elif to_unit.lower() == "kelvin":
    return kelvin
  else:
    raise ValueError(f"Unsupported unit: {to_unit}")


@mcp.tool()
def get_pdf(file_path: str) -> str:
  """Get PDF file."""
  return get_pdf_data(file_path)


@mcp.tool()
def get_text(file_path: str) -> str:
  """Get text file."""
  return get_file(file_path)

################################################################
# Prompt
################################################################


@mcp.prompt()
def weather_report(city: str) -> str:
  """Weather report."""
  return f"""
  Please provide a weather report for {city}.
  
  You can use the fetch_weather tool to get current weather data.
  If needed, you can convert temperature units using the
  convert_temperature tool.
  Please include:
  - Current temperature
  - Weather conditions
  - Humidity
  - Wind speed
  - Any relevant weather advice for the conditions
  """


def main():
  """Main."""
  mcp.run(transport='stdio')
  # mcp.run(transport='streamable-http')


# the MCP Inspector
# uv run mcp dev app/mcp/app_mcp.py
#
# Claude Code MCP
# https://code.claude.com/docs/en/mcp
if __name__ == "__main__":
  main()
