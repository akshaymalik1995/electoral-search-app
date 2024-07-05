# Electoral Search Application

This project is a simple web application that allows users to search for electoral information using their Epic Number and State Code. It also integrates a captcha verification step for added security. The application is built using Flask for the backend and HTML with Tailwind CSS for the frontend.

## Features

- **Captcha Generation**: Generates a captcha that users must solve to proceed with their electoral search.
- **Electoral Search**: Allows users to search for their electoral information by providing their Epic Number, State Code, and the solved captcha.
- **Responsive Design**: The frontend is designed to be responsive and user-friendly, making it accessible on various devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **APIs**: External APIs for captcha generation and electoral search

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/akshaymalik1995/electoral-search-app.git
   cd electoral-search-app
   ```

2. **Create and Activate Virtual Environment** (Optional but recommended)

   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

- Navigate to `http://127.0.0.1:5000/` in your web browser.
- The captcha image will be displayed. Enter the Epic Number, select the State, solve the captcha, and click on the "Submit" button.
- If the information is correct and the captcha is solved accurately, the electoral information will be displayed on the screen.

## Contributing

Contributions to the Electoral Search Application are welcome. Please ensure to follow the established coding standards and commit guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

```

```
