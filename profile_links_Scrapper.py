# cd C:\Program Files (x86)\Google\Chrome\Application
# chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\Asrunus$\Desktop\Linkedin Auto Connect & Message\chromeSession"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=opt)
total_links = 0
url =["https://www.linkedin.com/search/results/people/?geoUrn=%5B%22109227412%22%2C%22108354619%22%2C%22101025843%22%2C%22104524176%22%2C%22103720977%22%2C%22104305776%22%2C%22106204383%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=)I_","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22109227412%22%2C%22108354619%22%2C%22101025843%22%2C%22104524176%22%2C%22103720977%22%2C%22104305776%22%2C%22106204383%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=6nz","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%221810%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=man","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%22137%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=yx-","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%221912%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=(vu","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%22104%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=YH%3B","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%2296%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=Tlz","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&industry=%5B%224%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=%40BR","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22101025843%22%2C%22103720977%22%2C%22104305776%22%2C%22104524176%22%2C%22106204383%22%2C%22108354619%22%2C%22109227412%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=li%3A&talksAbout=%5B%22hiring%22%5D","https://www.linkedin.com/search/results/people/?geoUrn=%5B%22101025843%22%2C%22103720977%22%2C%22104305776%22%2C%22104524176%22%2C%22106204383%22%2C%22108354619%22%2C%22109227412%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=u2m&talksAbout=%5B%22talentacquisition%22%5D","https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%2C%221283%22%2C%223185%22%2C%2238373%22%2C%2267970111%22%2C%224824639%22%2C%22110163%22%2C%2218764209%22%2C%221009%22%2C%225042%22%2C%22163334%22%5D&geoUrn=%5B%22104305776%22%2C%22106204383%22%2C%22101025843%22%2C%22103720977%22%2C%22104524176%22%2C%22108354619%22%2C%22109227412%22%5D&keywords=talent%20acquisition%20manager&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&searchId=f25d24a7-d63b-465e-8b78-5f698f4d6939&sid=oXG"]

for search_url in url:
    for pgno in range(1, 101):
        print(f"Scrapping page {pgno} / 100")
        url = search_url + "&page=" + str(pgno)
        driver.get(url)

        premium_results = driver.find_elements(By.CSS_SELECTOR, ".reusable-search__result-container .entity-result__title-line li-icon")

        for index, result in enumerate(premium_results):
            nth_parent = result
            for _ in range(5):
                nth_parent = nth_parent.find_element(By.XPATH, "..")
            profile = nth_parent.find_element(By.XPATH, "./*")
            profile_link = profile.get_attribute("href")

            with open("profile_links.txt", "a") as file:
                file.write(profile_link + "\n")
            
            total_links = total_links + 1

        print(f"Total links scrapped : {total_links}")

driver.quit()