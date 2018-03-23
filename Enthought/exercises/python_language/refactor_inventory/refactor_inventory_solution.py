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

"""
from data_process_solution import process_log

###############################################################################
# Library of functions
###############################################################################


def initialize_inventory(transactions):
    """Given a list of transactions, initialize and return a dictionary with
    keywords for all parts in the transaction list.
    """
    inventory = {}
    for part, count in transactions:
        inventory[part] = 0
    return inventory


def compute_inventory(inventory, transactions):
    """Given an initial inventory dictionary and a list of transactions,
    compute and return the final inventory for each part.
    """
    for part, count in transactions:
        inventory[part] += count

    return inventory

###############################################################################
# Data
###############################################################################

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

transactions = process_log(warehouse_log)
init_inventory = initialize_inventory(transactions)
inv = compute_inventory(init_inventory, transactions)

###############################################################################
# Output
###############################################################################

for part in inv:
    print "%-20s %d" % (part, inv[part])
