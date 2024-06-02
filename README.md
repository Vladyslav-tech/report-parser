# Report Parser Service

A service for parsing and validating reports via specified criteria.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)

## Description

This project implements a service for:
1. Parsing the report content from the given url.
2. Validating the report content against specified criteria.

## Installation

To install the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/Vladyslav-tech/report-parser.git
    ```

2. Navigate to the project directory:
    ```sh
    cd report-parser
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To start the service, while in the `./report-parser` directory, run the command:

   ```sh
   uvicorn src.main:app --reload
   ```


The service will be available at

### API ###
`http://127.0.0.1:8000`

### URL docs ###
`http://127.0.0.1:8000/docs/`
