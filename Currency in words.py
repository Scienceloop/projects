import requests
import num2words

def convert_ccy_to_inr(ccy_amount, ccy):
    # Get the latest exchange rate for the specified currency
    r = requests.get(f"https://api.exchangerate-api.com/v4/latest/{ccy}")
    exchange_rate = r.json()["rates"]["INR"]

    # Convert the currency amount to INR using the exchange rate
    inr_amount = ccy_amount * exchange_rate
    inr_rupees, inr_paisa = "{:.2f}".format(inr_amount).split(".")
    # Convert the INR amount to words in the Indian numbering system
    inr_amount_words = num2words.num2words(inr_rupees, lang='en_IN')
    inr_paisa_amount_words = num2words.num2words(inr_paisa, lang='en_IN')

    return [inr_amount_words, inr_paisa_amount_words]

# Accept user input for the currency amount and currency code
ccy_amount = float(input("Enter the currency amount: "))
ccy = input("Enter the currency code (e.g. USD, GBP, EUR): ")

# Convert the currency amount to INR and display the result
inr_rupees_amount_words = convert_ccy_to_inr(ccy_amount, ccy)[0].replace(",","").replace("and","")
inr_paisa_amount_words = convert_ccy_to_inr(ccy_amount, ccy)[1].replace(",","")

print(f"{ccy_amount} {ccy} is equivalent to {inr_rupees_amount_words} rupees and {inr_paisa_amount_words} paisa")
