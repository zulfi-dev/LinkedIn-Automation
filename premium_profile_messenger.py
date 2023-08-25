from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip
import time

def send_connection_message(driver, url):
    driver.get(url)

    try:
        name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-heading-xlarge")))
        fname = name_element.text.split()[0]

        header_message = "Seeking IT Job Opportunity"
        body_message = f"Hey {fname},\n\nHope you are doing well, i am a UX Designer & Software developer with 4+ years of experience leading tech teams and working with professionals.\n\nMy skills vary from Figma, Sketch, Adobe XD, Photoshop etc in designing and HTML/CSS, Javascript, ReactJs, NextJs, Typescript, VueJs, AngularJs, NodeJs etc in development\n\nPlease consider my profile for any potent job openings.\n\nresume : https://zulfi.me/resume.pdf\nEmail : zulfiqar.uxd@gmail.com\nPh : +971 547752698\n\nThankyou,\nMohammed Zulfiqar\nSeeking IT Job Opportunity"
        # body_message = f"Dear {fname},\n\nI trust this message finds you well. My name is Mohammed Zulfiqar, and I am reaching out to express my interest in potential job openings within your esteemed organization.\n\nWith over four years of hands-on experience, I have successfully led tech teams and collaborated with professionals in the fields of UX Design and Software Development.\n\nMy proficiency spans across a range of design tools such as Figma, Sketch, Adobe XD, and Photoshop, enabling me to create intuitive and user-centric designs. On the development front, I possess expertise in HTML, CSS, Javascript, ReactJs, NextJs, Typescript, VueJs, AngularJs, and NodeJs, allowing me to translate design concepts into fully functional and responsive digital solutions.\n\nI have attached my comprehensive CV for your review, detailing my career journey and accomplishments. Should there be any relevant opportunities within your organization, I would greatly appreciate your consideration of my profile.\n\nFeel free to reach out to me via email: zulfiqar.uxd@gmail.com\nphone: +971 547752698\n\nThank you for your time and consideration. Looking forward to the possibility of contributing my skills and experience to your team.\n\nBest regards,\nMohammed Zulfiqar"

        pyperclip.copy(body_message)
        
        time.sleep(2)
        try:
            while True:
                driver.execute_script('document.querySelector(".msg-overlay-bubble-header__controls li-icon[type=\'close\']").click();')
                time.sleep(1)
        except Exception as e:
            print(e)

        time.sleep(1)
        message_button = driver.find_element(By.CSS_SELECTOR, ".entry-point.pvs-profile-actions__action button")
        message_button.click()
        
        time.sleep(1)
        header_input = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--input")
        header_input.send_keys(header_message)

        time.sleep(1)
        pyautogui.click(2200, 1000, button='left')  # Left-click
        time.sleep(0.3)
        pyautogui.click(2200, 1000, button='right')  # Right-click
        time.sleep(0.3)
        pyautogui.moveTo(2300, 1340)  # Move to paste opt position
        time.sleep(0.3)
        pyautogui.click(button='left')  # Left-click

        time.sleep(1)
        send_button = driver.find_element(By.CSS_SELECTOR, ".msg-form__send-button")
        send_button.click()

        time.sleep(2)
        print(f"Message sent to {fname}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

    urlIndex = 1190
    with open("data_cleaned.txt", "r") as file:
        urls = file.readlines()[urlIndex:]

    for url in urls:
        url = url.strip()
        print(urlIndex)
        send_connection_message(driver, url)        
        urlIndex = urlIndex + 1

    driver.quit()