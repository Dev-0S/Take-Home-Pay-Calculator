import locale
from django.shortcuts import render
from .forms import TaxForm

# Set locale for UK currency formatting
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

def format_currency(value):
    """Formats the value as £xx,xxx.xx"""
    return locale.currency(value, grouping=True)

def calculate_tax(request):
    result = None
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            income = form.cleaned_data['income']

            monthly_income = income / 12
            if monthly_income < 4189:
                ni = 0.08
            else:
                ni = 0.02

            # Subtract the personal allowance
            taxable_income = max(0, income - 12570)

            # Apply tax calculation based on UK PAYE tax bands
            if taxable_income <= 0:
                tax_amount = 0
            elif taxable_income <= 37700:  # Basic rate
                tax_amount = taxable_income * 0.2
            elif taxable_income <= 125140:  # Higher rate
                basic_tax = 37700 * 0.2
                higher_tax = (taxable_income - 37700) * 0.4
                tax_amount = basic_tax + higher_tax
            else:  # Additional rate
                basic_tax = 37700 * 0.2
                higher_tax = (125140 - 37700) * 0.4
                additional_tax = (taxable_income - 125140) * 0.45
                tax_amount = basic_tax + higher_tax + additional_tax

            # National Insurance Calculation
            ni_amount = ni * taxable_income

            # Take Home Pay
            take_home = income - tax_amount - ni_amount

            result = {
                'gross': format_currency(income),
                'gross_monthly': format_currency(income / 12),
                'gross_weekly': format_currency(income / 52),
                'gross_daily_work': format_currency(income / 253),
                'gross_daily': format_currency(income / 365),
                'gross_hourly': format_currency((income / 365) / 24),

                'taxable_income': format_currency(taxable_income),
                'taxable_income_monthly': format_currency(taxable_income / 12),
                'taxable_income_weekly': format_currency(taxable_income / 52),
                'taxable_income_daily': format_currency(taxable_income / 365),
                'taxable_income_hourly': format_currency((taxable_income / 365) / 24),

                'tax_paid': format_currency(tax_amount),
                'tax_paid_monthly': format_currency(tax_amount / 12),
                'tax_paid_weekly': format_currency(tax_amount / 52),
                'tax_paid_daily': format_currency(tax_amount / 365),
                'tax_paid_hourly': format_currency((tax_amount / 365) / 24),

                'NI': format_currency(ni_amount),
                'NI_monthly': format_currency(ni_amount / 12),
                'NI_weekly': format_currency(ni_amount / 52),
                'NI_daily': format_currency(ni_amount / 365),
                'NI_hourly': format_currency(ni_amount / 365 / 24),

                'take_home': format_currency(take_home),
                'take_home_monthly': format_currency(take_home / 12),
                'take_home_weekly': format_currency(take_home / 52),
                'take_home_daily': format_currency(take_home / 365),
                'take_home_hourly': format_currency(take_home / 365 / 24),
            }
    else:
        form = TaxForm()

    return render(request, 'calc/tax_calc.html', {'form': form, 'result': result})
