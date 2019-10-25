from mock_base._firestore._db import Doc
import unittest


class TestDoc(unittest.TestCase):
    
    def test_square_bracket(self):
        d = Doc()
        d.data = {"hello": "hello"}
        self.assertEqual(d["hello"], "hello")