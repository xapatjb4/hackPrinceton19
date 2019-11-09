from lib import lib

try:
    result = lib.waduphaitian.batnotif["@dev"](name='Dolores Abernathy')
except RuntimeError as err:
    # handle error
    print(err)
print(result)
