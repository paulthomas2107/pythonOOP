import os
import shutil

import pytest

import DoubleIt


class TestDoubleIt(object):

    numbers_file_template = 'testnums_template.txt'
    numbers_file_testor = 'testnums.txt'

    def setup_class(self):
        shutil.copy(TestDoubleIt.numbers_file_template, TestDoubleIt.numbers_file_testor)

    def teardown_class(self):
        os.remove(TestDoubleIt.numbers_file_testor)

    def test_doubleLines(self):
        DoubleIt.doubleLines(TestDoubleIt.numbers_file_testor)
        old_vals = [int(line) for line in open(TestDoubleIt.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleIt.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit_value(self):
        assert DoubleIt.doubleIt(10) == 20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            DoubleIt.doubleIt('hello')


