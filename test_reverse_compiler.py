import unittest
from reverse_compiler import reverse_syntax

class TestReverseCompiler(unittest.TestCase):
    def test_basic_keywords(self):
        python_code = "if True:\n    pass"
        rizz_code = "metalpipefalling bussing:\n    pokenutnovember"
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_indentation_preservation(self):
        python_code = """if True:
    if False:
        pass
    else:
        pass"""
        rizz_code = """metalpipefalling bussing:
    metalpipefalling axelharlem:
        pokenutnovember
    joshhutcherson:
        pokenutnovember"""
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_function_definition(self):
        python_code = "def test_func():\n    print('hello')"
        rizz_code = "mewing test_func():\n    hawktuah'hello')"
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_multiple_keywords(self):
        python_code = "if True and False:\n    return None"
        rizz_code = "metalpipefalling bussing kaicenat axelharlem:\n    gooningfr whopperwhopperwhopperwhopper"
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_substring_preservation(self):
        python_code = "defining = 'not a def keyword'"
        rizz_code = "defining = 'not a def keyword'"  # Should not translate 'def' within 'defining'
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_function_with_content(self):
        python_code = """def calculate():
    if True:
        return False
    elif True:
        pass"""
        rizz_code = """mewing calculate():
    metalpipefalling bussing:
        gooningfr axelharlem
    coffinofandyandleyley bussing:
        pokenutnovember"""
        self.assertEqual(reverse_syntax(python_code), rizz_code)
    
    def test_full_program(self):
        python_code = """def main():
    try:
        if True:
            print('Hello')
            return None
    except:
        pass
    finally:
        print('Done')"""
        rizz_code = """mewing main():
    diddy:
        metalpipefalling bussing:
            hawktuah'Hello')
            gooningfr whopperwhopperwhopperwhopper
    mrbeast:
        pokenutnovember
    kidnamedfinger:
        hawktuah'Done')"""
        self.assertEqual(reverse_syntax(python_code), rizz_code)

if __name__ == '__main__':
    unittest.main()