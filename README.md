# Market-chain
## General Description
Python and SQL implementation software that manages supermarket chain using Python and SQLite.
Supermarket chain management software designed to efficiently handle the operations of supermarket chains. This Python project utilizes SQLite to manage a database that includes tables for employees, suppliers, products, branches, and activities. The system supports the management of a large number of employees, buying and selling of products, inventory management, and tracking of sales and deliveries for tax purposes.

## Method and Technical Description
### Database Structure:
The bgumart.db database includes the following tables:

Employees: Information about employees.
Suppliers: Information about suppliers.
Products: Information about products.
Branches: Information about branches.
Activities: Information about all activities, including sales and deliveries.

### initiate.py
This module initializes the database by building it and inserting initial data from the configuration file. To run the script, use the following command:
python3 initiate.py config.txt
If the database file already exists, it will be removed before creating a new one. The configuration file contains details about branches, employees, products, and suppliers.

### action.py
This module manages supermarket activities, such as sales and deliveries. To execute the module, provide an actions file as an argument:
python3 action.py actions.txt
The actions file includes details about each activity, whether it's a sale or a supply arrival. The script performs each action in the specified order, and it ensures that the quantity of the sold product is sufficient.

### printdb.py
This module prints the contents of the database in a specified format. To run the script, use the following command:
python3 printdb.py
The script prints each table's records in ascending order of the primary key, with specific instructions for the Activities table. It also generates a detailed report on employees and activities.

### Configuration File
Each line in the configuration file represents a record type (E, S, P, or B) followed by details about the entity (Employee, Supplier, Product, or Branch). 

## Action File
Each line in the action file represents an activity, either a sale or a supply arrival. The quantity determines the type of activity. The script ignores actions where the quantity exceeds the available product quantity.

## Development Environment
This project is developed using Python 3.9 (or above) and SQLite3.

For any feedback or questions please feel free to reach out!
