from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def book_tickets(username, password, num_tickets):
    # Replace 'path_to_chromedriver' with the path to your Chrome WebDriver executable
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')
    driver.maximize_window()

    # Example: Booking website URL
    booking_url = "https://www.example.com/ticket-booking"

    try:
        # Open the booking website
        driver.get(booking_url)

        # Log in (if required)
        login(username, password, driver)

        # Select the number of tickets
        select_num_tickets(num_tickets, driver)

        # Fill in other details like date, time, etc.

        # Click the 'Book Now' button
        book_now_button = driver.find_element(By.XPATH, "//button[text()='Book Now']")
        book_now_button.click()

        # Proceed to payment page

        # Handle payment process

        # Confirm booking

        print("Tickets booked successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        driver.quit()

def login(username, password, driver):
    # Find and fill in the login credentials
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    # Wait for the login to complete (you might need to modify the wait time)
    WebDriverWait(driver, 10).until(EC.title_contains("Home"))

def select_num_tickets(num_tickets, driver):
    # Find and select the desired number of tickets (if there's a drop-down menu, for example)
    tickets_dropdown = driver.find_element(By.ID, "num_tickets")
    tickets_dropdown.click()
    tickets_option = driver.find_element(By.XPATH, f"//option[text()='{num_tickets}']")
    tickets_option.click()

if __name__ == "__main__":
    # Replace with your credentials and the number of tickets you want to book
    username = "your_username"
    password = "your_password"
    num_tickets = 2

    book_tickets(username, password, num_tickets)
