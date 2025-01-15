from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import csv
import time

URL = "https://www.seek.com.au/jobs/in-Victoria"
driver = webdriver.Chrome()

def next_button_exists():
    try:
        driver.find_element(By.CSS_SELECTOR, "svg.snwpn00.y71xbo0.l1r11857.l1r1185f._10wmcdz0._10wmcdz2._10wmcdz3._10wmcdz4.y71xbo3")
        return True
    except NoSuchElementException:
        return False

def job_code_find(str_find):
    code = r"jobId=([^&]+)&"
    found = re.findall(code, str_find)
    return found

def main():
    csv_file = open("jobs.csv", mode="w", newline="", encoding="utf-8")
    fieldnames = [
        "job_code",
        "company",
        "address",
        "job_type",
        "time",
        "salary",
        "jobAdDetails",
        "Employer_questions",
    ]

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for page_num in range(1,26):
        if page_num == 1:
            page_url = URL
        else:
            page_url = f"{URL}?page={page_num}"

        print(f"current page: {page_url}")
        driver.get(page_url)
        time.sleep(2)
        jobs = driver.find_elements(By.CSS_SELECTOR,  "a[data-automation='job-list-item-link-overlay']")

        for job in jobs:
            driver.execute_script("arguments[0].click();", job)
            time.sleep(2)
            current_url = driver.current_url
            job_code = job_code_find(current_url)[0]
            company = driver.find_element(By.CSS_SELECTOR, "[data-automation='advertiser-name']").text
            job_details = driver.find_elements(By.CSS_SELECTOR, "a._10gphjh0")
            address = job_details[0].text if len(job_details) > 0 else None
            job_type = job_details[1].text if len(job_details) > 1 else None
            working_time = job_details[2].text if len(job_details) > 2 else None
            try:
                salary = driver.find_element(By.CSS_SELECTOR, "[data-automation='job-detail-salary']").text
            except NoSuchElementException:
                salary = "No detail."
            detail_paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.snwpn00._1t6jlrs0 p")
            job_ad_details = "\n".join([p.text for p in detail_paragraphs])
            question_paragraphs = driver.find_elements(By.CSS_SELECTOR,".snwpn00.snwpn03.l1r1185b.l1r118hf.l1r1186r.l1r118i7")
            employer_questions = "\n".join([p.text for p in question_paragraphs])
            job_data = {
                "job_code": job_code,
                "company": company,
                "address": address,
                "job_type": job_type,
                "time": working_time,
                "salary": salary,
                "jobAdDetails": job_ad_details,
                "Employer_questions": employer_questions,
            }
            writer.writerow(job_data)
            time.sleep(1)

        page_num += 1

    csv_file.close()
    driver.quit()
    print("Saved every data in 'jobs.csv' file.")

if __name__ == "__main__":
    main()
