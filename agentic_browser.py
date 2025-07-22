"""
agentic_browser.py

A minimal agentic browser scaffold using Playwright for browser automation.
Designed to be extended with agentic/LLM reasoning and planning.

Requirements:
    pip install playwright
    playwright install

Usage:
    from agentic_browser import AgenticBrowser
    import asyncio

    async def main():
        async with AgenticBrowser(headless=True) as browser:
            await browser.goto("https://example.com")
            text = await browser.extract_text("h1")
            print(text)

    asyncio.run(main())
"""

import asyncio
from typing import Optional

try:
    from playwright.async_api import async_playwright, Page, Browser, BrowserContext
except ImportError as e:
    raise ImportError(
        "Playwright is required. "
        "Install it with: pip install playwright && playwright install"
    ) from e

class AgenticBrowser:
    """
    A programmable browser automation agent.
    Extend this class with LLM/agentic logic for advanced workflows.
    """

    def __init__(self, headless: bool = True):
        self.headless = headless
        self._playwright = None
        self._browser: Optional[Browser] = None
        self._context: Optional[BrowserContext] = None
        self._page: Optional[Page] = None

    async def __aenter__(self):
        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(headless=self.headless)
        self._context = await self._browser.new_context()
        self._page = await self._context.new_page()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._context:
            await self._context.close()
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()

    async def goto(self, url: str):
        """Navigate to a URL."""
        await self._page.goto(url)

    async def click(self, selector: str):
        """Click an element matching the selector."""
        await self._page.click(selector)

    async def type(self, selector: str, text: str, delay: int = 50):
        """Type text into an input field specified by the selector."""
        await self._page.fill(selector, "")
        await self._page.type(selector, text, delay=delay)

    async def extract_text(self, selector: str) -> str:
        """Extract and return the text content of an element."""
        return await self._page.text_content(selector)

    async def screenshot(self, path: str = "screenshot.png"):
        """Take a screenshot of the current page."""
        await self._page.screenshot(path=path)

    # === Placeholder for agentic/LLM-driven logic ===
    # def run_agentic_workflow(self, goal: str):
    #     """
    #     Plan and execute a workflow to achieve the given goal using LLMs.
    #     TODO: Integrate with LLM for reasoning, planning, and tool use.
    #     """
    #     pass

# === Example usage (can be removed/commented out in production) ===
if __name__ == "__main__":
    async def main():
        async with AgenticBrowser(headless=True) as browser:
            await browser.goto("https://example.com")
            print(await browser.extract_text("h1"))

    asyncio.run(main())