from fastmcp import FastMCP
import httpx

mcp = FastMCP("Currency Converter")

API_URL = "https://open.er-api.com/v6/latest/{}"


@mcp.tool
async def convert_currency(amount: float, from_currency: str, to_currency: str):
    """
    Convert currency in real-time using open exchange rate API.
    - amount: amount to convert
    - from_currency: e.g., "USD", "INR"
    - to_currency: e.g., "EUR", "GBP"
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    try:
        # Fetch live exchange rates
        async with httpx.AsyncClient() as client:
            response = await client.get(API_URL.format(from_currency))

        if response.status_code != 200:
            return {"error": "Unable to fetch exchange rates"}

        data = response.json()

        if data.get("result") != "success":
            return {"error": data.get("error-type", "API error")}

        rates = data.get("rates", {})

        if to_currency not in rates:
            return {"error": f"Unsupported target currency: {to_currency}"}

        rate = rates[to_currency]
        converted_value = amount * rate

        return {
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "rate": rate,
            "converted_value": converted_value,
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
