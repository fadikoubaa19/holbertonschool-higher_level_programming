#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    per = 0
    try:
        per = print('{:d}'.format(value))
        return(True)
    except Exception as per:
        print('Exception: {}'.format(str(per)), file=sys.stderr)
        return(False)
