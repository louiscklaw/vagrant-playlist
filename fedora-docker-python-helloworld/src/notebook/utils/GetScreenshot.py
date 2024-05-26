#!/usr/bin/env python
from playwright.async_api import async_playwright


def helloworld():
    print("helloworld")


async def getScreenshot_bmstatistics(url, file_path, timeout_s):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        await page.wait_for_timeout(timeout_s * 1000)
        # await page.waitForSelector('xpath=//*[contains(text(), "Total Goals")]');
        await page.get_by_text("Total Goals").click()

        await page.screenshot(path=file_path, full_page=True)

        await browser.close()


async def getScreenshot_bmrecentforms(url, file_path, timeout_s):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        elements = await page.locator('select.select-margin').all()
        with open('./result.txt','w') as fo:
            fo.write(str(len(elements)))
        await elements[0].select_option(label="Home Matches")
        await elements[1].select_option(label="Away Matches")

        await page.screenshot(path=file_path, full_page=True)

        await browser.close()


async def getScreenshot_standings(url, file_path, timeout_s):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(timeout_s * 1000)
        await page.screenshot(path=file_path, full_page=True)
        await browser.close()


async def getScreenshot(url, file_path, timeout_s):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        await page.wait_for_timeout(timeout_s * 1000)

        await page.screenshot(path=file_path, full_page=True)

        await browser.close()
