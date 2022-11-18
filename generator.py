import random
amount_list = [
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads, is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data and thus infer your contacts?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads, is used to infer WHEN large/small amount transactions are made with the help of other transaction data and thus infer your purchasing patterns?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Maps and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Crisis Reports?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Crisis Reports and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Crisis Reports and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Crisis Reports and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and it is used to infer WHEN large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to government agencies ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to government agencies and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to government agencies and it is used to infer WHEN large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to government agencies and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing its user experience?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and it is used to infer WHEN large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to shopping websites (like Amazon) and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is deleted automatically after 15 days?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing its user experience?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is used to infer WHEN large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties ?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties and it is used to measure frequency of large transactions?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties and it is used to infer WHEN large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to political parties and there is a data breach?",
"How comfortable will you be if the AMOUNT in the transaction shown is leaked in a data breach?"
]

amount_compulsory_list = [
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Ads, is used to measure frequency of large transactions and thus infer your purchasing power?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Maps and it is used to infer WHERE large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Crisis Reports and it is used for personalizing Google Crisis Reports's user experience?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Shopping and it is used to infer WHEN large/small amount transactions are made and is used to show targeted ads during that time?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to Google Pay and it is used for personalizing coupons and offers shown on Google Pay?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to government agencies and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
"How comfortable will you be if the AMOUNT in the transaction shown is sent to social media websites (like Facebook) and it is used to infer TO WHOM large/small amount transactions are made with the help of other transaction data?",
]

date_and_time_list = [
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and it is used for personalizing Google Ads's user experience?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Ads and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and it is used for personalizing Google Maps's user experience?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and is used to infer the exact location where the transaction was made (using your location history)?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Maps and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and is used to infer the exact location where the transaction was made (using your location history)?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Youtube and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Pay and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to government agencies ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to government agencies and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to government agencies and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to government agencies and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and it is deleted automatically after 15 days?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and is used to infer the exact location where the transaction was made (using your location history)?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to social media websites (like Facebook) and there is a data breach?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties ?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties and is used to infer the exact location where the transaction was made (using your location history)?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to political parties and there is a data breach?"
]

date_and_time_compulsory_list = [
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to Google Shopping and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to government agencies and is used to infer the exact location where the transaction was made (using your location history)?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and it is used to infer special occasions/events for you or others with the help of other transaction data?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and it is used to associate spending patterns with date/time?",
"How comfortable will you be if the DATE and TIME in the transaction shown is sent to shopping websites (like Amazon) and is used to infer the exact location where the transaction was made (using your location history)?"
]

group_expenses_list = [
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is used for personalizing Google Ads's user experience?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Crisis Reports ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Crisis Reports and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Crisis Reports and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to government agencies ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to government agencies and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to government agencies and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to government agencies and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is deleted automatically after 15 days?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used for personalizing social media websites (like Facebook)'s user experience?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and you can delete it anytime from the Google data dashboard?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to political parties ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to political parties and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to political parties and it is used to infer circles to whom large amounts are paid using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to political parties and it is used to infer close friend circles using other transaction data?"
]

group_expenses_compulsory_list  = [
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Crisis Reports and it is used to infer close friend circles using other transaction data?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Youtube and it is used for personalizing Youtube's user experience?"
]

voucher_data_list = [
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Ads and it is used to selectively advertise companies whose coupons are about to expire?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Shopping and it is used to selectively advertise companies whose coupons are about to expire?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to Google Pay and it is used to selectively advertise companies whose coupons are about to expire?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to shopping websites (like Amazon) and it is used to selectively advertise companies whose coupons are about to expire?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the GROUP EXPENSE shown is sent to social media websites (like Facebook) and it is used to selectively advertise companies whose coupons are about to expire?"
]

voucher_data_compulsory_list = []

receiver_individual_list = [
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Ads ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Ads and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Maps ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Crisis Reports ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Crisis Reports and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Crisis Reports and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Shopping ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Shopping and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Shopping and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Youtube ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Youtube and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Youtube and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Pay ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Pay and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Pay and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to government agencies ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to government agencies and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to government agencies and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the INDIVIDUAL shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to shopping websites (like Amazon) and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the INDIVIDUAL shown is sent to social media websites (like Facebook) and it is used for personalizing its user experience?",
"How comfortable will you be if the INDIVIDUAL shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to social media websites (like Facebook) and is used to determine close acquaintances via such transactions?",
"How comfortable will you be if the INDIVIDUAL shown is sent to political parties ?",
"How comfortable will you be if the INDIVIDUAL shown is sent to political parties and is used to gauge the frequency of transactions made to this individual?",
"How comfortable will you be if the INDIVIDUAL shown is sent to political parties and is used to determine close acquaintances via such transactions?",
]

receiver_individual_compulsory_list = [
"How comfortable will you be if the INDIVIDUAL shown is sent to Google Ads and is used to determine close acquaintances via such transactions?"
]

receiver_ecommerce_list = [
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to recommend products on this website via targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to advertise products when discounts and offers are available on this website?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Maps ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Crisis Reports ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Youtube and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Youtube and is used to recommend products on this website via targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to recommend products on this website via targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to advertise products when discounts and offers are available on this website?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to government agencies ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing its user experience?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing its user experience?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to recommend products on this website via targeted ads?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to advertise products when discounts and offers are available on this website?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to political parties ?",
"How comfortable will you be if the ECOMMERCE WEBSITE (receiver) in the transaction shown is sent to political parties and it is used for showing targeted ads?"
]

receiver_ecommerce_compulsory_list = []

receiver_food_list = [
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Ads and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Ads and is used to recommend food items in this food joint via targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Ads and is used to advertise this food joint when discounts and offers are available in it?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Maps ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Maps and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Maps and it is used for personalizing Google Maps's user experience?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Maps and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Maps and is used to advertise this food joint when discounts and offers are available in it?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping and is used to recommend food items in this food joint via targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Shopping and is used to advertise this food joint when discounts and offers are available in it?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Youtube and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Youtube and is used to recommend food items in this food joint via targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay and is used to recommend food items in this food joint via targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay and is used to advertise this food joint when discounts and offers are available in it?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Pay and is used to provide vouchers of this food joint on Google Pay?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to government agencies ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing its user experience?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing its user experience?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this food joint for showing better search results?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to recommend food items in this food joint via targeted ads?",
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to political parties ?"
]

receiver_food_compulsory_list = [
"How comfortable will you be if the FOOD JOINT (receiver) in the transaction shown is sent to Google Ads and it is used for showing targeted ads?"
]

receiver_food_del_list = [
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads and it is used for personalizing Google Ads's user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to recommend restaurants available in this food delivery website via targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to advertise this website discounts and offers are available in it?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Maps ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Maps and it is used for personalizing Google Maps's user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Maps and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and it is used for personalizing Google Shopping's user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to recommend restaurants available in this food delivery website via targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to advertise this website discounts and offers are available in it?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Youtube and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to government agencies ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing its user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to advertise this website discounts and offers are available in it?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing its user experience?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to recommend restaurants available in this food delivery website via targeted ads?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to advertise this website discounts and offers are available in it?",
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to political parties ?"
]

receiver_food_del_compulsory_list = [
"How comfortable will you be if the FOOD DELIVERY WEBSITE (receiver) in the transaction shown is sent to Google Ads and it is used for showing targeted ads?"
]

receiver_travel_list = [
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to advertise this website when discounts and offers are available in it?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Maps and it is used for personalizing Google Maps's user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Crisis Reports ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Crisis Reports and it is used for personalizing Google Crisis Reports's user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to advertise this website when discounts and offers are available in it?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Youtube and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Youtube and is used to recommend travel plans on this website via targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Pay and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Pay and it is used for personalizing Google Pay's user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to advertise this website when discounts and offers are available in it?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Pay and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing shopping websites (like Amazon)'s user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to recommend travel plans on this website via targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to advertise this website when discounts and offers are available in it?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to shopping websites (like Amazon) and is used to provide vouchers of this website on Google Pay?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing social media websites (like Facebook)'s user experience?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this website for showing better search results?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to recommend travel plans on this website via targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to advertise this website when discounts and offers are available in it?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to social media websites (like Facebook) and is used to provide vouchers of this website on Google Pay?"
]

receiver_travel_compulsory_list = [
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Ads and is used to recommend travel plans on this website via targeted ads?",
"How comfortable will you be if the TRAVEL WEBSITE (receiver) in the transaction shown is sent to Google Shopping and is used to provide vouchers of this website on Google Pay?"
]

receiver_bill_list = [
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and it is used for showing targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and it is used for personalizing Google Ads's user experience?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and is used to provide vouchers of this service provider on Google Pay?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Ads and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping and it is used for showing targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping and is used to provide vouchers of this service provider on Google Pay?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Shopping and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and it is used for showing targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and it is used for personalizing Youtube's user experience?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and is used to gauge the frequency of transactions made to this service provider for showing better search results?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Youtube and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay and is used to provide vouchers of this service provider on Google Pay?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to Google Pay and is used to give reminders for bill payments?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and it is used for showing targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and it is used for personalizing shopping websites (like Amazon)'s user experience?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to gauge the frequency of transactions made to this service provider for showing better search results?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to provide vouchers of this service provider on Google Pay?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to shopping websites (like Amazon) and is used to give reminders for bill payments?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) ?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and it is used for showing targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and it is used for personalizing social media websites (like Facebook)'s user experience?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and is used to gauge the frequency of transactions made to this service provider for showing better search results?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and is used to recommend specific service providers via targeted ads?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and is used to advertise service providers providing discounts and offers for utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and is used to provide vouchers of this service provider on Google Pay?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like Facebook) and is used to infer which service providers you are using for various utilities?",
"How comfortable will you be if the BILL PAYMENT in the transaction shown is sent to social media websites (like ,Facebook) and is used to give reminders for bill payments?"
]

receiver_bill_compulsory_list = []

mapper = {
    0 : (amount_list, amount_compulsory_list),
    1 : (date_and_time_list, date_and_time_compulsory_list),
    2 : (group_expenses_list, group_expenses_compulsory_list),
    3 : (voucher_data_list, voucher_data_compulsory_list),
    4 : (receiver_individual_list, receiver_individual_compulsory_list),
    5 : (receiver_ecommerce_list, receiver_ecommerce_compulsory_list),
    6 : (receiver_food_list, receiver_food_compulsory_list),
    7 : (receiver_food_del_list, receiver_food_del_compulsory_list),
    8 : (receiver_travel_list, receiver_travel_compulsory_list),
    9 : (receiver_bill_list, receiver_bill_compulsory_list),
   10 : (amount_list, amount_compulsory_list)
}

N = 15

def modify_list(question_list):
    res = []
    offset = 5
    for q in question_list:
        #print(type(q.find("send to")))
        #print()
        receiver_index = q.find("sent to")
        tpp = ""
        receiver = ""
        if(q[len(q)-2] == " "):
            tpp_index = len(q) - 1

        else:
            tpp_index = q.find("used")

            if tpp_index == -1:
                tpp_index = q.find("deleted")
                offset = offset + 3

            if tpp_index == -1:
                tpp_index = len(q)-1
                tpp = ""
            tpp = q[tpp_index+offset:]

        if receiver_index == -1:
            receiver_index = q.find("leaked")
            receiver = q[receiver_index+6:len(q)-2]
        else:
            receiver = q[receiver_index+5:tpp_index]
        
        #print(tpp_index)
        res_ele = (q, receiver, tpp)
        res.append(res_ele)

    return res

def modify_map(mapper):
    for key, tup in mapper.items():
        modified_list1 = modify_list(tup[0])
        modified_list2 = modify_list(tup[1])
        new_tup = (modified_list1, modified_list2)
        mapper[key] = new_tup

    return mapper

def func(typelist):
    res = []

    if(len(typelist)>3):
        return
    
    for t in typelist:
        if t == None:
            continue

        elif t in mapper.keys():
            tup = mapper[t]
            k = len(tup[1])
            rand_num = N - k 
            max_q_size = len(tup[0])

            for questions in tup[0]:
                res.append(questions)

            indices = random.sample(range(0, max_q_size-1), rand_num)

            for i in indices:
                res.append(tup[1][i])            
    
        
        else:
            print("Error, incorrect type returned\n")
            return []


    attention_check_question = "" 
    
    random.shuffle(res)
    attention_check_question = res[0]
    attention_check_question = attention_check_question[:4] + "un" + attention_check_question[4:]
    res.append(attention_check_question)
    
    return res


modify_map(mapper)

for key, tup in mapper.items():
    for q in tup[0]:
        print(q[0])
        print(q[1])
        print(q[2])
    print("\n\n")
    
    for q in tup[1]:
        print(q[0])
        print(q[1])
        print(q[2])
    print("\n\n_________________________________________________________________\n\n")