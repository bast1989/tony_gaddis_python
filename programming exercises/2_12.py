commission = 0.03

shares_buy = 2000
price_buy = 40
buy = shares_buy * price_buy
commission_buy = buy * commission
total_buy = buy + commission_buy

shares_sale = 2000
price_sale = 42.75
sale = shares_sale * price_sale
commission_sale = sale * commission
total_sale = sale - commission_sale

print(f'При покупке за акции уплачено: {buy}',
      f'Комиссия брокера при покупке составила: {commission_buy}',
      f'Акции были проданы за: {sale}',
      f'Комиссия брокера при продаже составила: {commission_sale}',
      f'Итог выручки по операциям продажи акций составил: {total_sale - total_buy}', sep='\n')