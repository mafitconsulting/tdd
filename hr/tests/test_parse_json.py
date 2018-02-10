import pytest
import json
from hr import parse_json

import tempfile

from hr import inventory

def test_inventory_load():
    """
    `inventory.load` takes a path to a file and parses it as JSON
    """
    inv_file = tempfile.NamedTemporaryFile(delete=False)
    inv_file.write("""
    [
      {
        "name": "kevin",
        "groups": ["wheel", "dev"],
        "password": "password_one"
      },
      {
        "name": "lisa",
        "groups": ["wheel"],
        "password": "password_two"
      },
      {
        "name": "jim",
        "groups": [],
        "password": "password_three"
      }
    ]
    """)
    inv_file.close()
    users_list = inventory.load(inv_file.name)
    assert users_list[0] == {
       'name': 'kevin',
       'groups': ['wheel', 'dev'],
       'password': 'password_one'
    }
    assert users_list[1] == {
       'name': 'lisa',
       'groups': ['wheel'],
       'password': 'password_two'
    }
    assert users_list[2] == {
       'name': 'jim',
       'groups': [],
       'password': 'password_three'
    }
