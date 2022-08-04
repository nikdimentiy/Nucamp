import re

# regex for credit card validation - American Express


def credit_card_validation_american_express(credit_card):
    regex = r'^3[47][0-9]{13}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - BCGlobal


def credit_card_validation_BCGlobal(credit_card):
    regex = r'^(6541|6556)[0-9]{12}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Carte Blanche


def credit_card_validation_carte_blanche(credit_card):
    regex = r'^389[0-9]{11}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Dankort


def credit_card_validation_dankort(credit_card):
    regex = r'^(5019|4175|4571|4)\d{12}|^(5019|4175|4571|4)\d{14}|^(5019|4175|4571|4)\d{16}|^(5019|4175|4571|4)\d{18}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Diners Club


def credit_card_validation_diners_club(credit_card):
    regex = r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Discover


def credit_card_validation_discover(credit_card):
    regex = r'^65[4-9][0-9]{13}|64[4-9][0-9]{13}|6011[0-9]{12}|(622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9][0-9]|9[01][0-9]|92[0-5])[0-9]{10})$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Insta Payment


def credit_card_validation_insta_payment(credit_card):
    regex = r'^63[7-9][0-9]{13}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - JCB


def credit_card_validation_JCB(credit_card):
    regex = r'^(?:2131|1800|35\d{3})\d{11}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Korean Local


def credit_card_validation_korean_local(credit_card):
    regex = r'^9[0-9]{15}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Laser


def credit_card_validation_laser(credit_card):
    regex = r'^(6304|6706|6709|6771)[0-9]{12,15}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Maestro


def credit_card_validation_maestro(credit_card):
    regex = r'^(5018|5020|5038|6304|6759|6761|6763)[0-9]{8,15}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Mastercard


def credit_card_validation_mastercard(credit_card):
    regex = r'^5[1-5][0-9]{14}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Solo


def credit_card_validation_solo(credit_card):
    regex = r'^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - UnionPay


def credit_card_validation_unionPay(credit_card):
    regex = r'^(62[0-9]{14,17})$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Visa


def credit_card_validation_visa(credit_card):
    regex = r'^(?:4[0-9]{12}(?:[0-9]{3})?$'
    return bool(re.fullmatch(regex, credit_card))

# regex for credit card validation - Visa Mastercard


def credit_card_validation_visa_mastercard(credit_card):
    regex = r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$'
    return bool(re.fullmatch(regex, credit_card))

# driver function for credit card validation


def credit_card_validation(credit_card):
    credit_card_validation_dict = {
        'american_express': credit_card_validation_american_express,
        'BCGlobal': credit_card_validation_BCGlobal,
        'carte_blanche': credit_card_validation_carte_blanche,
        'dankort': credit_card_validation_dankort,
        'diners_club': credit_card_validation_diners_club,
        'discover': credit_card_validation_discover,
        'insta_payment': credit_card_validation_insta_payment,
        'JCB': credit_card_validation_JCB,
        'korean_local': credit_card_validation_korean_local,
        'laser': credit_card_validation_laser,
        'maestro': credit_card_validation_maestro,
        'mastercard': credit_card_validation_mastercard,
        'solo': credit_card_validation_solo,
        'unionPay': credit_card_validation_unionPay,
        'visa': credit_card_validation_visa,
        'visa_mastercard': credit_card_validation_visa_mastercard
    }
    for key, value in credit_card_validation_dict.items():
        if value(credit_card):
            return key
    else:
        return 'Unknown'
