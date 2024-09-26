
# e-Learning platform

## Overview

This project is a Django web application. It uses Python 3.12.5 and includes the `Django` and `Pillow` packages. The development environment is managed using PyCharm 2024.2.2 Professional Edition on Windows 11.

## Requirements

- Python 3.12.5
- Django
- Pillow
- pip

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
    ```sh
    .\venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```sh
    source venv/bin/activate
    ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Apply the migrations**:
    ```sh
    python manage.py migrate
    ```

2. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

3. Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Pillow**: A Python Imaging Library (PIL) fork that adds image processing capabilities to your Python interpreter.

## Project Structure