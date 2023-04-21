# My Books Database Application

    This application provides a simple graphical user interface to manage your books collection. You can add, view, modify, and delete book records, which are stored in a MySQL database.


## Features

    - Add a new book record with title, author, and ISBN
    - View all book records in the database
    - Modify existing book records
    - Delete book records
    - Clear the screen of any input or selection
    - Exit the application


## Requirements

    - Python 3.7 or higher
    - Tkinter 8.6.10 or higher
    - PyMySQL 1.0.2 or higher


## Installation

    Before utulizing this app, be sure python3 and tkinter are pre-installed
    Normally tkinter should have downnloaded automatically besides of python3, but if doesn't, 
    type from terminal;

    to import tkinter-linux
    $ sudo apt-get install python3-tk

    to import tkinter-windows
    C:\> pip install tk

    1. Clone the repository:

    2. Change the working directory:

    3. Install the required Python packages:


## Configuration

    Update the `mysqlserver_config_orig.py` file with your MySQL server credentials:


    dbConfig = {
        'host': 'your_host',
        'user': 'your_user',
        'password': 'your_password',
        'database': 'your_database',
    }

    Table Structure:
    CREATE TABLE `books` (
      `ID` int NOT NULL AUTO_INCREMENT,
      `Title` varchar(255) DEFAULT NULL,
      `Author` varchar(255) DEFAULT NULL,
      `ISBN` varchar(20) DEFAULT NULL,
      PRIMARY KEY (`ID`)
    );


## Usage 

    Execute python file from your local directory

    for linux users:    
    $ python3 bookdb.py

    for windows users:
    C:> python bookdb.py

## Need to Be Upgraded

    1- Effects of operations on database doesn''t shown on listbox automatically. To see updated database on listbox based on users operations like deleting, adding or modifying records, user first need to use "Clear Screen" then "View all records" on app. So it is higtly recommend to use "Clear Screen" and "View all records" after each operations.

    2- Id number (registration order) is incrementing (1, 2, 3 ...)but fixed, if a record deleted, id numbers dont regenerated but continues in incrementing order next number.


### Contributing

    Contributions are welcome. Please open an issue or submit a pull request to suggest changes or improvements.


### Credits

    Mete Turkan
    linkedIn : linkedin.com/in/mete-turkan
    Inst : m_trkn46

