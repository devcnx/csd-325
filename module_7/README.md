_**Institution**: Bellevue University_
_**Program**: BS in Software Development_
_**Term**: Spring 2025_
_**Course**: CSD325 Advanced Python_
_**Assignment**: Module 7.2 Test Cases_
_**Author**: Brittaney Perry-Morgan_
_**Date**: Sunday, June 29th, 2025_

# Module 7.2 Test Cases

This repository contains the source code for an assignment in the CSD325 course. The assignment is designed to demonstrate proficiency in advanced Python programming.

## Assignment Overview

#### Steps

##### Phase 1

- Write a function that accepts two parameters: a city name and a country name.
  - The function should return a single string in the format City, Country (e.g., Santiago, Chile).
- Store the function in a file named `city_functions.py`.
- In the same file, call the function at least three times using City, Country values.
- Execute `city_functions.py` and take a screenshot of the result.
- Paste that screenshot into your Word document.

##### Phase 2

- Create a file called `test_city_functions.py`.
  - This file stores the code used to test the `city_functions.py` file.
- Write a method called `test_City_country()` to verify that calling your function with values such as `santiago` and `chile` results in the correct string.
- Run `test_city_functions.py` and make sure `test_city_country()` passes.
- When it passes, take a screenshot of the result and paste it into your Word document.

##### Phase 3

- Modify your `city_country` function in `city_functions.py` so it requires a third parameter, population.
- It should now return a single string of the form City, Country - Population #, such as Santiago, Chile - Population 5,000,000.
- Run `test_city_functions.py`.
  - The test should fail.
- Take a screenshot of the result and paste it into your Word document.

##### Phase 4

- Modify your `city_country` function in `city_functions.py` so that the population parameter is optional.
- Run `test_city_functions.py` again.
  - It should pass.
- Take a screenshot of the result and paste it into your Word document.

##### Phase 5

- Modify your `city_country` function in `city_functions.py` so it requires a fourth parameter, language.
- It should now return a single string of the form City, Country - population xxx, Language, such as Santiago, Chile - population 5,000,000, Spanish.
- Run `test_city_functions.py` again.
  - It should fail.
- Take a screenshot of the result and paste it into your Word document.

##### Phase 6

- Modify your `city_country` function in `city_functions.py` so that the language parameter is optional.
- Run `test_city_functions.py` again.
  - It should pass.
- Take a screenshot of the result and paste it into your Word document.

##### Phase 7

- Run `city_functions.py`.
  - Call the function at least three times using a City, Country for one, City, Country, Population for the next and City, Country, Population, Language for the last.
- Execute `city_functions.py` and take a screenshot of the result.
- Paste that screenshot into your Word document.

### Assignment Deliverables

#### Results Document (Word or PDF)

- All code pasted directly into the document. - Include the **filename** at the top of each code block in the document. - Ensure proper formatting and indentation.
  - Screenshot(s) of the programming running successfully.
    - Must show **visible current timestamp** (e.g., system time/date in the corner).
      - **Full-screen** screenshots are preferred.
  - Screenshot(s) demonstrating 100% test coverage.
    - Run the program with **multiple inputs**, if necessary.
    - Make sure all input and output are clearly visible.
