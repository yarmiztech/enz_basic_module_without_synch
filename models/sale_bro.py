import requests

from odoo import http
from odoo.http import request
from datetime import datetime
from num2words import num2words
import urllib.parse as urlparse
from urllib.parse import parse_qs
from odoo import models, fields, api
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    basic_synch_partner = fields.Char(string="Basic Synch Partner")


class ExecutiveAreaWise(models.Model):
    _inherit = 'executive.area.wise'

    basic_synch_area = fields.Char(string="Sync Area")


class ProductTemplate(models.Model):
    _inherit = "product.template"
    basic_synch_product = fields.Char(string='Sync Product')


class PinInformation(models.Model):
    _inherit = "pin.information"
    basic_synch_pin = fields.Char(string='Sync Pin')


class TransportationDeatails(models.Model):
    _inherit = "transportation.details"
    basic_synch_transporter = fields.Char(string='Sync Transporter')


class EwayConfiguration(models.Model):
    _inherit = "eway.configuration"
    basic_synch_eway = fields.Char(string='Sync Eway')


class EInvoiceConfiguration(models.Model):
    _inherit = "einvoice.configuration"
    basic_synch_einvoice = fields.Char(string='Sync Einvoice')


class ResUsers(models.Model):
    _inherit = "res.users"
    basic_synch_users = fields.Char(string='Sync Users')


class CompanyBranches(models.Model):
    _inherit = "company.branches"
    basic_synch_branch = fields.Char(string='Sync Branch')


class ResCompany(models.Model):
    _inherit = "res.company"
    basic_synch_company = fields.Char(string='Sync Company')


# class ResSubPartners(models.Model):
#     _inherit = "res.sub.partner"
#
#     basic_synch_sub_partner = fields.Char(string='Sync Company')


class SaleEstimate(models.Model):
    _inherit = 'sale.estimate'

    basic_synch_estimate = fields.Char(string='Sync estimate')
    basic_synch_estimate_approve = fields.Boolean(default=False)
    basic_synch_estimate_send_owner = fields.Boolean(default=False)
    basic_synch_estimate_cancel = fields.Boolean(default=False)
    basic_synch_estimate_approved = fields.Boolean(default=False)
    basic_synch_estimate_rejected = fields.Boolean(default=False)



class EstimateDippo(models.Model):
    _inherit = 'estimate.dippo'

    basic_synch_dippo = fields.Char(string='Sync Dippo')


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    basic_synch_vehicle = fields.Char(string='Sync vehicle')
    basic_synch_vehicle_mark = fields.Boolean(default=False)



class SalesExecutiveCollections(models.Model):
    _inherit = "executive.collection"

    basic_synch_collection = fields.Char(string='Sync Collection')
    basic_synch_cash_colled = fields.Boolean(string='Sync Collection')
    basic_synch_cash_confirm = fields.Boolean(string='Sync Collection')
    basic_synch_cash_reversed = fields.Boolean(string='Sync Collection')


class SalesExecutiveCheque(models.Model):
    _inherit = "executive.cheque.collection"

    basic_synch_check_collection = fields.Char(string='Sync Collection')
    basic_synch_check_colled = fields.Boolean(string='Sync Collection')


class TodayCheques(models.Model):
    _inherit = "today.cheques"

    basic_synch_today_cheques = fields.Char(string='Sync Collection')
    basic_synch_tocheques_button = fields.Boolean(string='Sync Collection')



class AmountWithdraw(models.Model):
    _inherit = "amount.withdraw"

    basic_synch_withdraw = fields.Char(string='Sync withdraw')
    basic_synch_withdraw_button = fields.Boolean(string='Sync Collection')
    basic_synch_withdreverse_button = fields.Boolean(string='Sync Collection')



class CashToBank(models.Model):
    _inherit = 'cash.to.bank'

    basic_synch_to_bank = fields.Char(string='Sync to Bank')
    basic_synch_to_bank_button = fields.Boolean(string='Sync to bank')
    basic_synch_to_reverbutton = fields.Boolean(string='Sync Collection')


class InternalAmountTransfer(models.Model):
    _inherit = 'internal.amount.transfer'

    basic_synch_bank_transf = fields.Char(string='Sync to Bank')
    basic_synch_bank_transf_button = fields.Boolean(string='Sync to bank')
    basic_synch_to_reverbutton = fields.Boolean(string='Sync Collection')

class FundTransferBTCompanies(models.Model):
    _inherit = "fund.transfer.companies"

    basic_synch_fund_transf = fields.Char(string='Sync to Bank')
    basic_synch_fund_transf_button = fields.Boolean(string='Sync to bank')
    basic_synch_fund_t_ref_button = fields.Boolean(string='Sync to bank')




class CashBookClosing(models.Model):
    _inherit = "cash.book.closing"

    basic_synch_closing = fields.Char(string='Sync to closing')
    basic_synch_closing_button = fields.Boolean(string='Sync to closing')


class FreightDiscount(models.Model):
    _inherit = 'freight.disc'

    basic_synch_freight = fields.Char(string='Sync to freight')
    basic_synch_freight_button = fields.Boolean(string='Sync to freight')
    basic_synch_fund_t_ref_button = fields.Boolean(string='Sync to bank')


class PartyAdvanceLedger(models.Model):
    _inherit = "party.advance.ledger"

    basic_synch_advance = fields.Char(string='Sync to advance')
    basic_synch_advance_button = fields.Boolean(string='Sync to advance')


class CashierDirectCollection(models.Model):
    _inherit = "cashier.direct.collection"

    basic_synch_direct = fields.Char(string='Sync to direct')
    basic_synch_direct_button = fields.Boolean(string='Sync to direct')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')

class RtgsNeftCollections(models.Model):
    _inherit = "neft.rtgs.collection"

    basic_synch_neft = fields.Char(string='Sync to direct')
    basic_synch_neft_button = fields.Boolean(string='Sync to direct')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')


class ExpensesDiscount(models.Model):
    _inherit = 'expenses.disc'

    basic_synch_expen = fields.Char(string='Sync to expenses')
    basic_synch_expen_button = fields.Boolean(string='Sync to expenses')
    basic_synch_direct_rev_button = fields.Boolean(string='Sync to direct')



class PartyAdvanceLedger(models.Model):
    _inherit = "party.advance.ledger"

    basic_synch_party_advance = fields.Char(string='Sync to Advance')
    basic_synch_party_advance_button = fields.Boolean(string='Sync to Advance')


class AccountAccount(models.Model):
    _inherit = "account.account"

    basic_synch_account = fields.Char(string='Sync to Advance')
    basic_synch_account_button = fields.Boolean(string='Sync to Advance')


class EstimateOrders(models.Model):
    _inherit = 'estimate.orders'

    basic_synch_order = fields.Char(string='Sync to Order')
    basic_synch_order_button = fields.Boolean(string='Sync to Order')


class CompanySoPOTransfer(models.Model):
    _inherit = 'company.sopo.transfer'

    basic_synch_sopo = fields.Char(string='Sync to sopo')
    basic_synch_sopo_button = fields.Boolean(string='Sync to sopo')

class Location(models.Model):
    _inherit = "stock.location"

    basic_synch_location = fields.Char(string='Sync to location')
    # basic_synch_sopo_button = fields.Boolean(string='Sync to sopo')


class InterBranchTransfer(models.Model):
    _inherit = 'inter.branch.transfer'

    basic_synch_transfer = fields.Char(string='Sync to transfer')
    basic_synch_transfer_button = fields.Boolean(string='Sync to transfer')



class OpeningBalanceCustomers(models.Model):
    _inherit = "opening.balance.customers"

    basic_synch_opening = fields.Char(string='Sync to Opening')
    basic_synch_opening_button = fields.Boolean(string='Sync to Opening')



class OpenAccountBalance(models.Model):
    _inherit = 'open.account.balance'

    basic_synch_ac_balance = fields.Char(string='Sync to Balance')
    basic_synch_ac_balance_button = fields.Boolean(string='Sync to Balance')



class SalesReturn(models.Model):
    _inherit = 'sales.return'

    basic_synch_return = fields.Char(string='Sync to return')
    basic_synch_return_button = fields.Boolean(string='Sync to return')



class SalesInvoiceCancel(models.Model):
    _inherit = 'sales.invoice.cancel'

    basic_synch_cancel = fields.Char(string='Sync to return')
    basic_synch_cancel_button = fields.Boolean(string='Sync to return')



class CreditLimitRecord(models.Model):
    _inherit = "credit.limit.record"

    basic_synch_credit_limit = fields.Char(string='Sync to return')
    basic_synch_credit_limit_button = fields.Boolean(string='Sync to return')

    # @api.constrains('basic_synch_credit_limit_button')
    # def basic_basic_synch_credit_limit_button(self):
    #     if self.basic_synch_credit_limit_button:
    #         self.action_cancel_create()


class SalesIncentives(models.Model):
    _inherit = "sales.person.incentives"

    basic_synch_incentives = fields.Char(string='Sync to return')
    basic_synch_incentives_button = fields.Boolean(string='Sync to return')

class AccountJournal(models.Model):
    _inherit = "account.journal"

    basic_synch_journal = fields.Char(string='Sync to journal')
    basic_synch_journal_button = fields.Boolean(string='Sync to journal')


class SetupBarBankConfigWizard(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'

    basic_synch_bank = fields.Char(string='Sync to bank')
    basic_synch_bank_button = fields.Boolean(string='Sync to bank')



class ResBank(models.Model):
    _inherit = "res.bank"

    basic_synch_res_bank = fields.Char(string='Sync to bank')
    basic_synch_res_bank_button = fields.Boolean(string='Sync to bank')


class PdcConfiguration(models.Model):
    _inherit = "pdc.configuration"

    basic_synch_pdc_bank = fields.Char(string='Sync to pdc')
    basic_synch_pdc_button = fields.Boolean(string='Sync to pdc')


class FreightDiscountConfig(models.Model):
    _inherit = 'freight.disc.config'


class BounceCheques(models.Model):
    _inherit = "bounce.cheques"

    basic_synch_bounce = fields.Char(string='Sync to bounce')
    basic_synch_bounce_button = fields.Boolean(string='Sync to bounce')


class AreaOffers(models.Model):
    _inherit = "area.offers"

    basic_synch_offers = fields.Char(string='Sync to offers')
    basic_synch_offers_button = fields.Boolean(string='Sync to offers')


class PurchaseOrderCustom(models.Model):
    _inherit = 'purchase.order.custom'

    basic_synch_purchase_req = fields.Char(string='Sync to Purchase Request')
    basic_synch_purchase_req_button = fields.Boolean(string='Sync to Purchase Request')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    basic_synch_purchase_order = fields.Char(string='Sync to Purchase Order')
    basic_synch_purchase_order_button = fields.Boolean(string='Sync to Purchase Order')
    basic_synch_po_invoice_button = fields.Boolean(string='Sync to Invoice Order')



class AccountInvoice(models.Model):
    _inherit = "account.move"

    basic_synch_account_move = fields.Char(string='Sync to Purchase Order')
    basic_synch_account_move_button = fields.Boolean(string='Sync to Purchase Order')


class PurchaseDiscounts(models.Model):
    _inherit = "purchase.discounts"

    basic_synch_po_discount = fields.Char(string='Sync to Purchase Order')
    basic_synch_po_discount_button = fields.Boolean(string='Sync to Purchase Order')
    basic_synch_po_discount_buttons = fields.Boolean(string='Sync to Purchase Order')

    # @api.constrains('basic_synch_po_discount_button')
    # def basic_basic_synch_po_discount_button(self):
    #     if self.basic_synch_po_discount_button:
    #         self.action_approve()



class BudgetReportFirst(models.Model):
    _inherit = "budget.report.first"

    basic_synch_bud_repo_first = fields.Char(string='Sync to Purchase Order')
    basic_synch_bud_repo_first_button = fields.Boolean(string='Sync to Purchase Order')


class BudgetReport(models.Model):
    _inherit = "budget.report"

    basic_synch_bud_repo = fields.Char(string='Sync to budget report')
    basic_synch_bud_repo_button = fields.Boolean(string='Sync to budget report')


class BudgetReportFilter(models.Model):
    _inherit = "budget.report.filter"

    basic_synch_bud_repo_filt = fields.Char(string='Sync to budget report Filter')
    basic_synch_bud_repo_filt_button = fields.Boolean(string='Sync to budget report Filter')


class PurchaseDateDiscounts(models.Model):
    _inherit = "purchase.date.discounts"

    basic_synch_po_date_discount = fields.Char(string='Sync to Purchase Order')
    basic_synch_po_date_discount_button = fields.Boolean(string='Sync to Purchase Order')

class BillDiscounts(models.Model):
    _inherit = "bill.discounts"

    basic_synch_bill_date_discount = fields.Char(string='Sync to bill Order')
    basic_synch_bill_date_discount_button = fields.Boolean(string='Sync to bill Order')



class SpecialDiscounts(models.Model):
    _inherit = "special.discounts"

    basic_synch_special_discount = fields.Char(string='Sync to Discount special')
    basic_synch_special_discount_button = fields.Boolean(string='Sync to Discount special')



class BankFeesStatement(models.Model):
    _inherit = "bank.fee.statement"

    basic_synch_bank_fee = fields.Char(string='Sync to Discount special')
    basic_synch_bank_fee_button = fields.Boolean(string='Sync to Discount special')


