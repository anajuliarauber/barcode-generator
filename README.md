# Barcode Generation Service with Flask

This project is a simple web application built with Flask. The application provides a service to generate barcode images based on a given product code using the Code128 standard.

## Features
- Generate barcode images in Code 128 format
- Save barcode images locally
- RESTful API with a POST endpoint for barcode generation

## Technologies Used
- Python
- Flask
- barcode (Code128 and ImageWriter)

## Installation

1. Clone this repository:

```bash
git clone git@github.com:anajuliarauber/barcode-generator.git
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

 ```bash
 pip install -r requirements.txt
 ```

## Usage

1. Run the Flask application:

```bash
flask --app app run 
```

