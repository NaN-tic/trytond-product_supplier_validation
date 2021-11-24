# This file is part product_supplier_validation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product
from . import purchase

def register():
    Pool.register(
        product.Template,
        product.ProductSupplier,
        purchase.Purchase,
        purchase.PurchaseLine,
        module='product_supplier_validation', type_='model')
