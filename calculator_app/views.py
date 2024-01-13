# calculator_app/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import PremiumCalculation


@csrf_exempt
def calculate_premium(request):
    if request.method == 'GET':
        plan_value = request.GET.get('plan_value', '933')
        sum_assured = request.GET.get('sum_assured', '100000')
        age = request.GET.get('age', '23')
        term = request.GET.get('term', '22')
        print("the values from the post request", plan_value, sum_assured, age, term)


        # Perform the premium calculation using Selenium
        calculated_premium = perform_premium_calculation(plan_value, sum_assured, age, term)

        # Save the calculation to the database
        PremiumCalculation.objects.create(
            plan_value=plan_value,
            sum_assured=sum_assured,
            age=age,
            term=term,
            calculated_premium=calculated_premium
        )

        return JsonResponse({'calculated_premium': str(calculated_premium)})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def perform_premium_calculation(plan_value, sum_assured, age, term):
    print("the values from the post request", plan_value, sum_assured, age, term)
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    # Setting up the Chrome driver with headless mode
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(options=chrome_options)


    try:
        # Navigate to the website
        driver.get("https://www.licpremiumcalculator.in/")
        
        
        # Wait for the dropdown to load
        wait = WebDriverWait(driver, 10)
        dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'custom-select')))
        
        # Select a plan from the dropdown
        select = Select(dropdown)
        select.select_by_value(plan_value)

        # Fill the input fields
        sum_assured_input = wait.until(EC.presence_of_element_located((By.ID, 'sa')))
        sum_assured_input.clear()
        sum_assured_input.send_keys(sum_assured)

        age_input = wait.until(EC.presence_of_element_located((By.ID, 'age')))
        # driver.execute_script("arguments[0].value = '';", age_input)
        age_input.send_keys(age)

        term_input = wait.until(EC.presence_of_element_located((By.ID, 'term')))
        term_input.send_keys(term)

        calculate_button = driver.find_element(By.ID, 'submit')
        # Scroll to the button
        driver.execute_script("arguments[0].scrollIntoView(true);", calculate_button)

        # Now try to click the "Calculate" button
        calculate_button.click()

        result_element = wait.until(EC.presence_of_element_located((By.ID, 'result')))
        wait.until(lambda driver: result_element.text.strip() != '')


        # Get the calculated value
        calculated_value = result_element.text.strip()
        print(calculated_value)

        return calculated_value

    finally:
        # Close the driver in the 'finally' block to ensure it is closed even if an exception occurs
        driver.quit()


