import unittest
from parameterized import parameterized
from SecretaryProgram import check_document_existance, get_doc_owner_name, delete_doc, add_new_shelf, get_doc_shelf


class TestSecretaryProgram(unittest.TestCase):
    def setUp(self):
        pass

    @parameterized.expand([
        ["2207 876234", True],
        ["11-2", True],
        ["10006", True],
        ["98876", False]
    ])
    def test_check_document_existance(self, input_, actual_):
        self.assertEqual(check_document_existance(input_), actual_)

    @parameterized.expand([
        ["11-2", "Геннадий Покемонов"],
        ["543210", None]
    ])
    def test_get_doc_owner_name(self, input_, actual_):
        self.assertEqual(get_doc_owner_name(input_), actual_)

    @parameterized.expand([
        ['2207 876234', ('2207 876234', True)],
        ['10006', ('10006', True)]
        ])
    def test_delete_doc(self, input_, actual_):
        self.assertEqual(delete_doc(input_), actual_)

    @parameterized.expand([
        ['10', ('10', True)],
        ['4', ('4', True)],
        ['2', ('2', False)]
    ])
    def test_add_new_shelf(self, input_, actual_):
        self.assertEqual(add_new_shelf(input_), actual_)

    @parameterized.expand([
        ["11-2", "1"],
        ["98876", None]
    ])
    def test_get_doc_shelf(self, input_, actual_):
        self.assertEqual(get_doc_shelf(input_), actual_)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()