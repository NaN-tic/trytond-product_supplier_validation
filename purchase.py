# This file is part of the product_supplier_validation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.exceptions import UserError
from trytond.i18n import gettext


class Purchase(metaclass=PoolMeta):
    __name__ = 'purchase.purchase'

    @classmethod
    def quote(cls, purchases):
        for purchase in purchases:
            for line in purchase.lines:
                line._check_product_supplier_validation()
        super().quote(purchases)


class PurchaseLine(metaclass=PoolMeta):
    __name__ = 'purchase.line'

    def _check_product_supplier_validation(self):
        if ((self.type != 'line')
                or not self.product
                or not self.purchase
                or (self.product
                and not self.product.template.requires_validation_for_purchase)):
            return

        if not self.product_supplier or not self.product_supplier.validated:
            raise UserError(gettext(
                'product_supplier_validation.msg_product_supplier_validation',
                    purchase=self.purchase.rec_name,
                    product=self.product.rec_name,
                    supplier=self.purchase.party.rec_name,
                    ))
