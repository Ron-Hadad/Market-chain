from persistence import *

import sys

def main(args : list):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]
            c = repo._conn.cursor()
            c.execute(f'SELECT quantity FROM products WHERE id ={product_id}')
            result = c.fetchone()
            if result and int(quantity) + result[0] >= 0:
                repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
                c.execute('UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
                repo._conn.commit()
                             
if __name__ == '__main__':
    main(sys.argv)
