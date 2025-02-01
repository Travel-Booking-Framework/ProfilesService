# User-Service: Profiles MicroService

## Introduction

**ProfilesService** is a core microservice of the **Travel-Booking-Framework** that provides a Management system for Profiles, like Create - Update - Delete with **with Service Layer Design Pattern**.
This service is developed using **Django**, **PostgreSQL** and **REST API**. This Project has **92%** Coverage Tests.

## Features

- **Profiles CUD**: Add, Update and Delete Profiles Models with Service Layer Design Pattern.
- **Profiles Simple Queries**: Filter Profiles by Simple Queries with Service Layer Design Pattern.


## Prerequisites

- **Python 3.x**
- **Django**
- **PostgreSQL**

## Installation and Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Travel-Booking-Framework/User-Service.git
   cd ProfilesService
   ```

2. **Create and Activate a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup PostgreSQL**: Ensure **PostgreSQL** is installed and running. Update your (`settings.py`) with the correct database credentials.

5. **Setup REST API**: Ensure that **DjangoRestFramework** is installed and running on your system. Update the Django settings (`settings.py`) with the correct DjangoRestFramework configuration.

## Project Structure

- **ProfilesService/**: Contains the core settings and configurations for Django.
- **Profile/**: Manages Profile-related operations and functionalities.
- **Class-Diagram/**: Provides class diagrams for understanding the project architecture.
- **logs/**: Contains logs files.

## Contribution Guidelines

We welcome contributions from the community! To contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Commit** your changes.
4. **Submit a Pull Request**.


## Additional Notes

- **Create a Superuser**: To create an admin account, use the command:
  ```bash
  python manage.py createsuperuser
  ```

- **REST API Support**: This project includes GraphQL capabilities, which can be accessed at `/api/`.