# This file is part of the product_supplier_validation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Id


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'
    requires_validation_for_purchase = fields.Boolean(
        "Requires Validation for Purchase",
        states={
            'readonly': ~Eval('context', {}).get('groups', []).contains(
                Id('product_supplier_validation', 'group_purchase_validation'))
        })


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'


class ProductSupplier(metaclass=PoolMeta):
    __name__ = 'purchase.product_supplier'
    validated = fields.Boolean("Validated", states={
            'readonly': ~Eval('context', {}).get('groups', []).contains(
                Id('product_supplier_validation', 'group_purchase_validation'))
            })

    @classmethod
    def copy(cls, products, default=None):
        if default is None:
            default = {}
        else:
            default = default.copy()
        default.setdefault('validation_for_supplier', None)
        return super(ProductSupplier, cls).copy(products, default=default)
