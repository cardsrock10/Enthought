"""
Refactor Inventory
------------------

This script contains a copy of the inventory exercise solution. It also
contains 3 empty functions that should be used to 'refactor' the original
code. Refactoring some code means re-organizing it into functions (and those
functions into modules) that can be reused later for similar tasks.

1. Move the code from the script part into the functions.

2. Call the functions in order to achieve the same task.

Bonus:
~~~~~~
3. The log processing function is an example of a data processing function that
   can be re-used by other projects. Move it to its own file (data_process.py)
   and import it here to still be able to run the script.


See :ref:`refactor_inventory_solution`.
"""

##############################################################################
# Library of functions
##############################################################################


def process_log(log):
    """ Process a warehouse log string containing part names and counts.
    Return a list of transactions.
    """
    pass


def initialize_inventory(transactions):
    """Given a list of transactions, initialize and return a dictionary with
    keywords for all parts in the transaction list.
    """
    pass


def compute_inventory(initial_inventory, transactions):
    """Given an initial inventory dictionary and a list of transactions,
    compute and return the final inventory for each part.
    """
    pass

##############################################################################
# Data
##############################################################################

warehouse_log = """ frombicator      10
                    whitzlegidget    5
                    splatzleblock    12
                    frombicator      -3
                    frombicator      20
                    foozalator       40
                    whitzlegidget    -4
                    splatzleblock    -8
                """

###############################################################################
# Script
###############################################################################

# Remove any leading and trailing whitespace from the string::

warehouse_log = warehouse_log.strip()

# Create a list of transactions from the log with part as string.
# and count as integer::

transactions = []
for line in warehouse_log.split("\n"):
    part, count = line.split()
    transaction = (part, int(count))
    transactions.append(transaction)

# Process the transactions, keeping track of inventory::

# Initialize the inventory dictionary so that all the
# parts have a count of 0.
inventory = {}
for part, count in transactions:
    inventory[part] = 0

for part, count in transactions:
    # read the part and count out of the transaction line.
    inventory[part] += count

###############################################################################
# Output
###############################################################################

for part in inventory:
    print "%-20s %d" % (part, inventory[part])
