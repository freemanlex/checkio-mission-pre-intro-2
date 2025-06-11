init_code = """
if not "robots" in USER_GLOBAL:
    raise NotImplementedError("Where is 'robots' variable?")

robots = USER_GLOBAL['robots']
    
if not isinstance(robots, int):
    raise TypeError("'robots' variable must be an integer")
    
if not "droids" in USER_GLOBAL:
    raise NotImplementedError("Where is 'droids' variable?")
    
droids = USER_GLOBAL['droids']

if not isinstance(droids, int):
    raise TypeError("'droids' variable must be an integer")

    
if not "add" in USER_GLOBAL:
    raise NotImplementedError("Where is 'add' variable?")

add = USER_GLOBAL['add']

if not isinstance(add, int):
    raise TypeError("'add' variable must be an integer")

if add != robots + droids:
    raise ValueError("'add' variable must be a sum of 'robots' and 'droids'")    

if not "multi" in USER_GLOBAL:
    raise NotImplementedError("Where is 'multi' variable?")

multi = USER_GLOBAL['multi']

if not isinstance(multi, int):
    raise TypeError("'multi' variable must be an integer")

if multi != robots * droids:
    raise ValueError("'multi' variable must be a product of 'robots' and 'droids'")
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="",
                     answer=""),
        ]
    }