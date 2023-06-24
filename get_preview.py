from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def get_website_preview(url):
    # Configure Selenium webdriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    executable_path = "/path/to/chromedriver"  # Replace with the actual path to chromedriver
    

    # Start the webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Set the window size for the screenshot
        driver.set_window_size(1280, 720)

        # Open the website
        driver.get(url)

        # Take a screenshot of the page
        screenshot_path = "img.png"  # Provide the desired path to save the screenshot
        driver.save_screenshot(screenshot_path)

        # Close the webdriver
        driver.quit()

        # Return the path to the screenshot
        return screenshot_path
    except Exception as e:
        # Handle any exceptions that occur during the process
        print(f"An error occurred: {e}")
        driver.quit()  # Ensure the webdriver is closed
        return None


# Main function
def main():
    # Get the URL of the website from the user
    url = "https://aisearch.tool42.xyz/"

    # Call the get_website_preview function
    screenshot_path = get_website_preview(url)

    if screenshot_path:
        print(f"Website preview saved at: {screenshot_path}")
    else:
        print("Failed to capture website preview.")


# Entry point of the application
if __name__ == "__main__":
    main()
