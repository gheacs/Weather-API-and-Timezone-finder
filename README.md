# World Clock

This project is part of Lab 4 for the TECHIN 510 course. The purpose of this lab is to demonstrate several key concepts:

- World Clock: Create a world clock application that displays the current time in different locations around the world. Users can select different time zones to view the corresponding time.
- Weather Condition with GitHub Action: Implement a GitHub Action that periodically fetches the weather conditions for a given location. The weather data is then displayed alongside the current time in the world clock application.
- PostgreSQL Server on Azure: Set up a PostgreSQL server on the Azure cloud platform. This includes provisioning a database instance and configuring it for use within the project.  

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:

    ```bash
    streamlit run app.py
    ```  
## Dependencies

List of dependencies required to run the project:

- Streamlit
- Requests
- Timezonefinder
- Python-dotenv

## Self Reflection 
1. This week I have learned that despite it's user simplicity, streamlit can have many limitation on layout design.
2. The previous webscrapping for lab3 weather condition was unsuccessful in retrieving the weather data so I try to use API instead for this lab.
3. I learn on how to store API key properly before publishing in github

## Potential Future Improvement
If I have more time, I would definitely add more features aside from weather condition.
