# Text Generator

---

[Final Release](https://github.com/matiasto/text_generator/releases/tag/loppupalautus)

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Introduction

This app is the tiralabra course project. The app is a text generator that uses Markov Chain and Trie data structure to imitate natural language generation.

## Getting Started

1. Clone the [repository]()
2. In the project folder, run
    ```bash
    poetry install
    ````
3. Start the application,
    ```bash
    poetry run invoke start
    ````

For detailed instructions visit [instructions](./docs/instructions.md)

---

## Testing

- Run tests
    ```bash
    poetry run invoke test
    ````
- Run performance tests
    ```bash
    poetry run invoke performance
    ````
- Generate coverage report
    ```bash
    poetry run invoke coverage-report
    ````
- Perform pylint quality inspection
    ```bash
    poetry run invoke lint
    ````
- Execute autopep8 format
    ```bash
    poetry run invoke format
    ````

---

## Documentation

- [Architecture](./docs/architecture.md)
- [Instructions](./docs/instructions.md)
- [Record of Working Hours](./docs/record_of_working_hours.md)
- [Requirements Specification](./docs/requirements_specification.md)
- [Testing](./docs/testing.md)
- [Weekly Reports](./docs/weekly_reports/)
    - [Week 1](./docs/weekly_reports/week_1.md)
    - [Week 2](./docs/weekly_reports/week_2.md)
    - [Week 3](./docs/weekly_reports/week_3.md)
    - [Week 4](./docs/weekly_reports/week_4.md)
    - [Week 5](./docs/weekly_reports/week_5.md)
    - [Week 6](./docs/weekly_reports/week_6.md)
