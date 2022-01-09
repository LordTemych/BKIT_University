import unittest
import sys, os
sys.path.append(os.getcwd())
from main import *


class Test(unittest.TestCase):
    def test_B1(self):
        one_to_many = [(g.name, g.page_num, c.name_p)
                       for g in docums
                       for c in parts
                       if g.part_id == c.id]
        self.assertEqual(B1(one_to_many), [('Запрет продажи алкоголя', 31, 'Нормативный акт'), ('О внутреннем распорядке', 16, 'Устав организации'), ('Об образовании', 20, 'Федеральный закон'), ('Организация труда', 10, 'Устав организации'), ('Уголовный', 15, 'Кодекс')])


    def test_B2(self):
        one_to_many = [(g.name, g.page_num, c.name_p)
                       for g in docums
                       for c in parts
                       if g.part_id == c.id]
        self.assertEqual(B2(one_to_many), [('Нормативный акт', 31), ('Устав организации', 26), ('Федеральный закон', 20), ('Кодекс', 15)])

    def test_B3(self):
        many_to_many_temp = [(c.name_p, gc_s.part_id, gc_s.docum_id)
                             for c in parts
                             for gc_s in part_docs
                             if c.id == gc_s.part_id]
        many_to_many = [(g.name, g.page_num, part_name)
                        for part_name, part_id, docum_id in many_to_many_temp
                        for g in docums if g.id == docum_id]
        self.assertEqual(B3(many_to_many),{ 'Кодекс': ['Уголовный', 'Запрет продажи алкоголя'], 'Устав организации': ['Организация труда', 'О внутреннем распорядке'], 'Федеральный закон': ['Об образовании'], 'Нормативный акт': []})

if __name__ == '__main__':
    unittest.main()