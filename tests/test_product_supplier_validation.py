# This file is part product_supplier_validation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import doctest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite
from trytond.tests.test_tryton import doctest_teardown, doctest_checker


class ProductSupplierValidationTestCase(ModuleTestCase):
    'Test Product Supplier Validation module'
    module = 'product_supplier_validation'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProductSupplierValidationTestCase))
    suite.addTests(doctest.DocFileSuite('scenario_product_supplier_validation.rst',
            tearDown=doctest_teardown, encoding='UTF-8',
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE,
            checker=doctest_checker))
    return suite
