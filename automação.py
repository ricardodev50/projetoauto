from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("http://soulmv/mv/flex/AppletlessRunner.html?t=1694029174820#")
    pagina.fill('xpath=//*[@id="username"]', "RICARDOMC")
    pagina.fill('xpath=//*[@id="password"]', "@senha4848")
    pagina.locator('xpath=//*[@id="context_login"]/section[4]/input[7]').click()
    time.sleep(100000)
