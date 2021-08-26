import unittest


class TextTestCase(unittest.TestCase):
    def test_replace_variables(self):
        from we_pyutils.t.text import VariablesReplaceHandler
        # 形式为：{{ Name }} 或 {{Name01}}
        pattern = r'{{[ ]*(?P<var_name>[a-zA-Z0-9]+)[ ]*}}'
        content = 'Hello {{ name }}, We are {{ doing }}, empty var is {{ empty }}.'
        content_r = 'Hello Karen, We are testing, empty var is .'
        var_dict = {
            'name': 'Karen',
            'doing': 'testing',
        }
        content_replaced = VariablesReplaceHandler(content, pattern, var_dict).replace()
        self.assertEqual(content_r, content_replaced)


if __name__ == '__main__':
    unittest.main()
