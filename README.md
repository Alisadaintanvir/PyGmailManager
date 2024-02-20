# PyGmailManager
#### This Python script allows users to manage their emails programmatically. It provides functionalities to log in to an IMAP email server, search for specific emails based on criteria, and delete emails matching the search criteria.

## Features
- **Login to IMAP Server:** The script allows users to log in to an IMAP email server securely.
- **Search Emails:** Users can search for emails based on specified criteria such as sender, subject, date, etc.
- **Delete Emails:** Users can choose to delete emails that match the search criteria.

## Prerequisites
- Python 3 installed on your system.
- Gmail account credentials (username and password).
  - must have to use the app password 
- Enable IMAP access in your Gmail settings.


## Installation
#### Clone the repository:

`git clone https://github.com/your_username/email-manager.git`

#### Navigate to the project directory:

`cd email-manager`
#### Install the required dependencies:

`pip install -r requirements.txt`

## Usage
1. Set up environment variables:

- Create a .env file in the project directory.

- Add the following lines to the .env file:

    - EMAIL=your_email@gmail.com
    - PASSWORD= your_password(Google App Password)
      - to get an app password, visit this link:-  [https://support.google.com/accounts/answer/185833?hl=en](url)
   
2. Modify the key and value variables in main.py according to your search criteria.

3. Run the script:

`python main.py`

4. Follow the on-screen prompts to manage your emails.

### Environment Variables

EMAIL: Your Gmail email address.

PASSWORD: Your Gmail account app password.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project was inspired by the need for a simple email management tool using Python.
