import imaplib


class EmailManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.login()

    def login(self):
        try:
            login_result, _ = self.mail.login(self.username, self.password)
            if login_result == 'OK':
                print("Login successful.")
                self.mail.select('inbox')
            else:
                print("Login failed. Please check your credentials.")
        except Exception as e:
            print(f"An error occurred during login: {e}")

    def search(self, key, value):
        try:
            result, data = self.mail.search(None, f'({key} " {value}")')
            if result == 'OK':
                email_num = data[0].split()
                print(f"{len(email_num)} emails found ({key.lower()}: '{value}'). ")
                return True
            else:
                print(f"No emails found with subject '{value}'.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_email(self, key, value):
        try:
            result, data = self.mail.search(None, f'({key} "{value}")')
            if result == 'OK':
                for num in data[0].split():
                    self.mail.store(num, '+FLAGS', '\\Deleted')
                self.mail.expunge()
                print(f"Email  {key} '{value}' deleted successfully.")
            else:
                print(f"No emails found  {key} '{value}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def close_connection(self):
        self.mail.close()
        self.mail.logout()
