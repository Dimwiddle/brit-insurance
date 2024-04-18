# Brit Insurance QA Test Task
Python Test Framework for the Technical Task

## Frameworks utilised
1. Scenario 1 - Playwright + Pytest
2. Scenario 2 - Requests + Pytest

## Pre-requisites

1. Python v3.11 (or later) installed.
2. Virtual env created with command: `python -m venv .venv`

## Setup Test Framework Guide

1. Activate your virtual environment
> source .venv/bin/activate

2. In the terminal - install dependancies from requirements.txt
> pip install -r requirements.txt

3. You are now ready to execute the tests
> pytest --html=report.html

## Discussion

### Reporting

Currently reporting is created with the **pytest-html** library as it provides a quick visual report for these tests.

In a more usual setting - I'd prefer to utilise a tool such as **Allure**. With this tool we can get more in-depth reporting for test methods as `allure.steps`, for example.

### API Testing Approach

Currently the API tests in Scenario 2 (`test/test_scenario_2.py`) are functional tests, validating some valid / invalid request scenarios and some edge cases.

In a more realistic business situation - the acceptance criteria / requirements of the endpoint would be clearer. Therefore we can create more robust scenarios for better coverage. The test data can also be controlled outside of the test case, if necessary.

Some other approaches to consider:

1. Integration testing - checking the interactions of underlying services are working together.

2. Security testing - we can check for vulnerabilities such as SQL injections, XSS and authentication.

3. Error handling - testing the errors provided are appropriate for the client with the correct status code and to make sure the error message is relevant to the request. Sensitive information shouldn't be exposed in the response message.

4. Performance testing - verify the API can handle higher loads, as well as checking the response time is appropriate for sent requests.

#### Exploratory Testing

There are more exploratory scenarios we could test of the given API, if we had more information on expected behaviour of the API Client and Server. 

Here are some examples:

1. We can test the boundary parameters of the request query.

2. Authentication mechanisms can be verified e.g. is a JWT token required for the endpoint.

3. Response time of each request, under different situations e.g. 
- Concurrent request handling of the system
- Varying the size of the payload to see how the API handles the underlying SQL query

4. Test other methods for the API e.g. GET, DELETE, PUT. Verify the response status code is appropriate to the acceptance criteria.

5. Test the API server under different network conditions (depending on the requirements.)

