init_code = """
if not "a" in USER_GLOBAL:
    raise NotImplementedError("Where is 'a' variable?")

if not "b" in USER_GLOBAL:
    raise NotImplementedError("Where is 'b' variable?")
    
a = USER_GLOBAL['a']
b = USER_GLOBAL['b']

if not isinstance(a, int):
    raise TypeError("'a' variable must be an integer")

if not isinstance(b, int):
    raise TypeError("'b' variable must be an integer")

    
if not "add" in USER_GLOBAL:
    raise NotImplementedError("Where is 'add' variable?")

if not "multi" in USER_GLOBAL:
    raise NotImplementedError("Where is 'multi' variable?")

add = USER_GLOBAL['add']
multi = USER_GLOBAL['multi']

if not isinstance(add, int):
    raise TypeError("'add' variable must be an integer")

if not isinstance(multi, int):
    raise TypeError("'multi' variable must be an integer")

if add != a + b:
    raise ValueError("'add' variable must be a sum of 'a' and 'b'")

if multi != a * b:
    raise ValueError("'multi' variable must be a product of 'a' and 'b'")
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