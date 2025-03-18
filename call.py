def buy_call(stock_price, strike_price, premium):
    if stock_price>strike_price:
        return 100*stock_price - 100*strike_price - 100*premium, -(100*premium)
    else:
        return -(100*premium), -(100*premium)

def sell_call(stock_price, strike_price, premium):
    if stock_price>strike_price:
        return 100*stock_price - 100*strike_price + 100*premium, (100*premium)
    else:
        return (100*premium), (100*premium)
    
def buy_put(stock_price, strike_price, premium):
    if stock_price<strike_price:
        return 100*(strike_price - stock_price - premium), -(100*premium)
    else:
        return -(100*premium), -(100*premium)
    
def sell_put(stock_price, strike_price, premium):
    if stock_price<strike_price:
        return 100*(strike_price - stock_price + premium), (100*premium)
    else:
        return (100*premium), (100*premium)

# spread profit/loss
def spread_pl(*args):
    # ROS = Return on spread
    ROS = sum(profit for profit, _ in args)
    out_of_pocket = sum(out for _, out in args)
    if out_of_pocket != 0:
        percent_return = -(ROS/out_of_pocket) if (ROS < 0) else abs(ROS/out_of_pocket)
    else:
        percent_return = ROS
    PROFIT = ROS + out_of_pocket
    return {'RETURN ON SPREAD': ROS, 'MAX_LOSS':out_of_pocket, 'PERCENT PROFIT':100*percent_return, 'PROFIT': PROFIT}
# strike1 = 70
# premium1 = 7.5
# premium2 = 2.5
# strike2 = 80
# stock_price = 85


# Vertical Spread
# vertical_spread = spread_pl(buy_call(stock_price, strike1, premium1), sell_call(stock_price, strike2, premium2))
# print(vertical_spread)

# Iron Condor
# Idea is that teh stock price will be between strike1 and strike2
# strike3 and strike4 are safe guards
strike3 = 60
strike1 = 65
strike2 = 85
strike4 = 90
premium3 = 1
premium1 = 2
premium2 = 2
premium4 = 1
stock_price = 96
iron_condor = spread_pl(buy_put(stock_price, strike3, premium3),
                        sell_put(stock_price, strike1, premium1), 
                        sell_call(stock_price, strike2, premium2), 
                        buy_call(stock_price, strike4, premium4))
print(buy_put(stock_price, strike3, premium3))
print(sell_put(stock_price, strike1, premium1))
print(sell_call(stock_price, strike2, premium2))
print(buy_call(stock_price, strike4, premium4))
print(iron_condor)