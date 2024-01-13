# Premium Calculator API

This API calculates premium for insurance plans using Selenium and Django.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## Introduction

The Premium Calculator API is a Django project that utilizes Selenium for scraping premium calculations from an insurance premium calculator website. The calculated premium is then stored in a Django model.

## Features

- Premium calculation for insurance plans
- Integration with Selenium for web scraping
- Storage of calculated premiums in a Django model

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Django
- ChromeDriver (for Selenium)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/premium-calculator-api.git
   cd premium-calculator-api

2. Install dependencies:

    ```bash
    pip install -r requirements.txt

3. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Start the development server:

    ```bash
    python manage.py runserver

## Usage

1. Make a GET request to /api/calculate/ with the required parameters.

    ```bash
    curl -X GET http://localhost:8000/api/calculate/ -d "plan_value=933&sum_assured=100000&age=23&term=22"



