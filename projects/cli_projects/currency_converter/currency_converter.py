import aiohttp
import asyncio
from typing import Dict, Any, Optional


async def get_countries_list() -> Optional[Dict[str, str]]:
    """Fetch the list of countries and their currency names."""
    CURRENCY_CODE_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.min.json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(CURRENCY_CODE_URL) as response:
                response.raise_for_status()
                data: Dict[str, str] = await response.json()
                filtered_data: Dict[str, str] = {}

                for code, name in data.items():
                    if name and name.strip() not in filtered_data.values():
                        filtered_data[code] = name

                return filtered_data

    except aiohttp.ClientConnectorError:
        print("Network error — check your internet connection.")
    except aiohttp.ClientResponseError as e:
        print(f"HTTP error occurred: {e.status} {e.message}")
    except asyncio.TimeoutError:
        print("Request timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


async def get_rates(url: str) -> Optional[Dict[str, Any]]:
    """Fetch exchange rates from the API."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                data: Dict[str, Any] = await response.json()
                return data

    except aiohttp.ClientConnectorError:
        print("Network error — check your internet connection.")
    except aiohttp.ClientResponseError as e:
        print(f"HTTP error occurred: {e.status} {e.message}")
    except asyncio.TimeoutError:
        print("Request timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


async def get_currency_rates(base: str, url: str) -> Optional[Dict[str, float]]:
    """Fetch and display currency rates for a base currency."""
    data = await get_rates(url)
    if not data:
        print("Failed to retrieve currency rates.")
        return None

    rates: Dict[str, float] = data.get(base)
    if not rates:
        print(f"No exchange rates found for base currency '{base.upper()}'.")
        return None

    countries = await get_countries_list() or {}

    print("=" * 60)
    print(f"{'Exchange Rates (Base: ' + base.upper() + ')':^60}")
    print("=" * 60)
    print(f"{'Country':<30} {'Code':<10} {'Rate':>10}")
    print("-" * 60)

    for code, rate in rates.items():
        country_name = countries.get(code, code)
        print(f"{country_name:<30} {code:<10} {rate:>10.4f}")

    print("=" * 60)
    return rates


async def main():
    base = input("Enter Base Currency: ").lower()
    BASE_URL = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2025-11-06/v1/currencies/{base}.json"

    rates = await get_currency_rates(base=base, url=BASE_URL)
    if not rates:
        return

    to_curr = input("Enter Target Currency Code: ").upper()
    if to_curr.lower() not in rates:
        print(f"Currency code '{to_curr}' not found in rates.")
        return

    to_amount = float(input(f"Enter amount in {base.upper()}: "))
    ask_rate = rates[to_curr.lower()]

    print("\n" + "=" * 60)
    print(f"1.0 {base.upper()} = {ask_rate:.4f} {to_curr}")
    print(f"{to_amount} {base.upper()} = {ask_rate * to_amount:.4f} {to_curr}")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
