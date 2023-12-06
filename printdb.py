from persistence import *

def main():
    print('Activities')
    activities = repo.activities.find_all()
    activities.sort(key=lambda x: x.date)
    for activitie in activities:
        print(activitie)
    
    print('Branches')
    for branche in repo.branches.find_all():
        print(branche.__str__())

    print('Employees')
    for employee in repo.employees.find_all():
        print(employee.__str__())

    print('Products')
    for product in repo.products.find_all():
        print(product.__str__())

    print('Suppliers')
    for supplier in repo.suppliers.find_all():
        print(supplier.__str__())

    print("Employees report")
    employee_report_query = '''
    SELECT e.name, e.salary, b.location, SUM(a.quantity * p.price) as total_sales
    FROM employees e
    JOIN branches b ON e.branche = b.id
    LEFT JOIN activities a ON e.id = a.activator_id 
    LEFT JOIN products p ON a.product_id = p.id
    GROUP BY e.id
    ORDER BY e.name ASC
    '''
    for row in repo.execute_command(employee_report_query):
        name, salary, location, total_sales = row
        name = name.decode()
        location = location.decode()
        if total_sales is None:
            total_sales = 0
        print(f'{name} {salary} {location} {total_sales * -1}')

    print("Activity report")
    activity_report_query = '''
    SELECT a.date, p.description, a.quantity, e.name, s.name
    FROM activities a
    JOIN products p ON a.product_id = p.id
    LEFT JOIN employees e ON a.activator_id = e.id
    LEFT JOIN suppliers s ON a.activator_id = s.id
    ORDER BY a.date ASC
    '''
    for row in repo.execute_command(activity_report_query):
        date, item, quantity, seller, supplier = row
        if seller is not None:
            seller =  seller.decode()
            seller = "'" + seller + "'"
        if supplier is not None:
            supplier = supplier.decode()
            supplier = "'" + supplier + "'"
        print(f"(\'{date.decode()}\', \'{item.decode()}\', {quantity}, {seller}, {supplier})")

if __name__ == '__main__':
    main()
