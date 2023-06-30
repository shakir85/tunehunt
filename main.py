from inventory import crud

obj = crud.Inventory()

obj.create_schema(artist='artist1', album='album1', tracks=['t1', 't2'])
