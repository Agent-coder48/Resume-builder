# Resume-builder Web application
This is a simple web application for building resumes. Users can input their personal information, education, experience, and skills to generate a professional-looking resume in PDF format.

## Features

- Input personal details including name, email, and phone number.
- Add education history.
- Add work experience.
- List skills.
- Generate a downloadable PDF resume.

## Requirements

- Python 3
- Flask
- pdfkit
- wkhtmltopdf

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Agent-coder48/resume-builder.git
cd resume-builder


2. Create and activate a virtual environment:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install the required Python packages:
bash
Copy code
pip install Flask pdfkit
Install wkhtmltopdf:
Ubuntu:
bash
Copy code
sudo apt-get install wkhtmltopdf
macOS:
bash
Copy code
brew install Caskroom/cask/wkhtmltopdf
Usage
Run the Flask application:
bash
Copy code
python app.py
