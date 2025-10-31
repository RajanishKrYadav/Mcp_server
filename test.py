"""def main():
    print("Hello from expense-tracker-mcp-server!")


if __name__ == "__main__":
    main()"""

import random
from fastmcp import FastMCP
mcp = FastMCP(name="Demo server")

@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    """Roll a dice with the given number of sides and return the result."""
    return [random.randint(1,6)for _ in range(n_dice)]
@mcp.tool
def add(a: float,b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    mcp.run()
