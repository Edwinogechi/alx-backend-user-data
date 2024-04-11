
Project Title: 0x00-personal_data

Description:
The "0x00-personal_data" project is dedicated to ensuring the secure handling and protection of personal data within a specific application or system. This project focuses on implementing best practices for managing personal data to safeguard user privacy and comply with relevant data protection regulations.

Key Features:

User Authentication: The project includes robust mechanisms for user authentication to ensure that only authorized users can access sensitive personal data.

Data Encryption: Personal data is encrypted using strong cryptographic algorithms to prevent unauthorized access and protect user privacy.

Data Masking/Obfuscation: Sensitive personal data is masked or obfuscated to prevent exposure in logs or other non-secure storage mediums.

Data Access Controls: Access controls are implemented to restrict access to personal data only to authorized personnel with legitimate reasons for accessing it.

Data Retention Policies: The project defines clear data retention policies to ensure that personal data is not stored longer than necessary and is securely disposed of when no longer needed.

Compliance with Regulations: The project ensures compliance with relevant data protection regulations, such as GDPR, HIPAA, or CCPA, by implementing necessary security measures and privacy controls.

Usage:

To use the "0x00-personal_data" project, follow these steps:

Clone the repository to your local environment.
Configure the project settings according to your specific application requirements.
Integrate the project components into your application's backend infrastructure.
Follow the provided documentation and guidelines to ensure proper handling and protection of personal data.
Contributing:

Contributions to the "0x00-personal_data" project are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or open an issue on GitHub.

License:

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments:

Special thanks to all contributors and supporters of the "0x00-personal_data" project for their valuable contributions and feedback.

Contact:

For inquiries or further information about the "0x00-personal_data" project, please contact projectmaintainer@example.com.

Disclaimer:

The "0x00-personal_data" project is provided as-is without any warranty. Use it at your own risk. The project maintainers are not liable for any damages or liabilities resulting from the use or misuse of this software. Always adhere to best practices and regulations when handling personal data.


links:
1. https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg
2. https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw
3. https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw
4. https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA


Tasks
0. Regex-ing
mandatory
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
The function should use a regex to replace occurrences of certain field values.
filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

Copy the following code into filtered_logger.py.

import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
Update the class to accept a list of strings fields constructor argument.

Implement the format method to filter values in incoming log records using filter_datum. Values for fields in fields should be filtered.

DO NOT extrapolate FORMAT manually. The format method should be less than 5 lines long.


3. 2. Create logger
mandatory
Use user_data.csv for this task

Implement a get_logger function that takes no arguments and returns a logging.Logger object.

The logger should be named "user_data" and only log up to logging.INFO level. It should not propagate messages to other loggers. It should have a StreamHandler with RedactingFormatter as formatter.

Create a tuple PII_FIELDS constant at the root of the module containing the fields from user_data.csv that are considered PII. PII_FIELDS can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter.

Tips:

What Is PII, non-PII, and personal data?
Uncovering Password Habits


3. Connect to secure database
mandatory
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure holberton database to read a users table. The database is protected by a username and password that are set as environment variables on the server named PERSONAL_DATA_DB_USERNAME (set the default as “root”), PERSONAL_DATA_DB_PASSWORD (set the default as an empty string) and PERSONAL_DATA_DB_HOST (set the default as “localhost”).

The database name is stored in PERSONAL_DATA_DB_NAME.

Implement a get_db function that returns a connector to the database (mysql.connector.connection.MySQLConnection object).

Use the os module to obtain credentials from the environment
Use the module mysql-connector-python to connect to the MySQL database (pip3 install mysql-connector-python)

4. Read and filter data
mandatory
Implement a main function that takes no arguments and returns nothing.

The function will obtain a database connection using get_db and retrieve all rows in the users table and display each row under a filtered format like this:

[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
Filtered fields:

name
email
phone
ssn
password
Only your main function should run when the module is executed.


5. Encrypting passwords
mandatory
User passwords should NEVER be stored in plain text in a database.

Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).


6. Check valid password
mandatory
Implement an is_valid function that expects 2 arguments and returns a boolean.

Arguments:

hashed_password: bytes type
password: string type
Use bcrypt to validate that the provided password matches the hashed password.
