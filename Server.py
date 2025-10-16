from typing import Any #adding type hints to your code
import httpx # provide sync and async API calls
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette #ightweight ASGI framework/toolkit, which is ideal for building async web services
from mcp.server import Server
from mcp.server.fastmcp.prompts import Prompt


import uvicorn # ASGI web server implementation for Python

#intialize MCP server for Weather tools (SSE)
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"


async def make_nws_request(url: str) -> dict[str, Any] | None:
    """ Make a request to NWS APIs with proper handling"""
    headers = {
        "User-Agent" : USER_AGENT,
        "Accept" : "application/geo+json"
    }

    async with httpx.AsyncClient as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def format_alert(feature: dict) -> str:
    """ Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
        Event: {props.get('event', 'Unknown')}
        Area: {props.get('areaDesc','Unknown')}
        Severity: {props.get('severity','Unknown')}
        Description: {props.get('description','No description available')}
        Instruction: {props.get('instruction','No specific instruction available')}

    """


@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get Weather aleart for US State
        Args: Two-letter US State Code (CA, WA)
    """

    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found"
    
    if not data["features"]:
        return "No active alerts for this state."
    
    alerts = [format_alert(feature) for feature in data["features"]]

    return "\n---\n".join(alerts)


##############################################################
##############################################################

@mcp.tool()
async def get_forecast(latitude: float, longtitude: float) -> str:
    """
        Get weather forecast for a location

        Args: Latitude : latitue of a location
              Longtitude: longtitude of a location
    """

    points_url = f"{NWS_API_BASE}/points/{latitude},{longtitude}"
    points_data = await make_nws_request(points_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast"
    
    periods = forecast_data["properties"][periods]
    forecasts = []
    for period in periods[:5]: #only show next 5 periods
        forecast = f"""
    {period['name']}:
    Temperature: {period['temperature']}{period['temperatureUnit']}
    Wind: {period['windSpeed']} {period['windDirectio']}
    Forecast: {period['detailedForecast']}

    """
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)


@mcp.prompt()
def get_initial_prompts()->list[base.Message]:
    return [
        base.UserMessage("You are a helpful assistant that can help with weather-related questions."),
    ]