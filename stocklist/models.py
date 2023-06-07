from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from portfolio.models import *

# Create your models here.

class StrategyTrading(models.Model):
    name = models.CharField(max_length=100)
    modified_date = models.DateTimeField(auto_now=True)
    risk = models.FloatField(default=0.03)
    description = models.CharField(max_length=200, null=True)
    nav = models.FloatField(default=10000000)
    commission = models.FloatField(default=0.0015)
    period= models.IntegerField(default=20)

    def __str__(self):
        return str(self.name) +str('_')+str(self.risk)
    


class Signaldaily(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()#auto_now_add=True)
    milestone = models.FloatField(default=0)
    signal = models.CharField(max_length=10)
    ratio_cutloss = models.FloatField(default=0)
    strategy = models.ForeignKey(StrategyTrading,on_delete=models.CASCADE, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.ticker) + str(self.strategy)
    
    # @property
    # def close(self):
    #     close = StockPriceFilter.objects.filter(ticker = self.ticker).order_by('-date').first().close
    #     return close
    
    # @property
    # def distance(self):
    #     return round((self.close/self.milestone-1)*100,0)
    
           

class OverviewBacktest(models.Model):
    ticker = models.CharField(max_length=15)
    strategy = models.ForeignKey(StrategyTrading,on_delete=models.CASCADE, null=True, blank=True)
    ratio_pln= models.FloatField(default=0)
    drawdown= models.FloatField(null=True)
    sharpe_ratio= models.FloatField(null=True)
    total_trades = models.IntegerField(null=True)
    total_open_trades = models.IntegerField(null=True)
    win_trade_ratio = models.FloatField(null=True)
    total_closed_trades = models.IntegerField(null=True)
    won_current_streak = models.IntegerField(null=True)
    won_longest_streak = models.IntegerField(null=True)
    lost_current_streak = models.IntegerField(null=True)
    lost_longest_streak = models.IntegerField(null=True)
    gross_average_pnl = models.FloatField(null=True)
    net_average_pnl = models.FloatField(null=True)
    won_total_trades = models.IntegerField(null=True)
    won_total_pnl = models.FloatField(null=True)
    won_average_pnl = models.FloatField(null=True)
    won_max_pnl = models.FloatField(null=True)
    lost_total_trades = models.IntegerField(null=True)
    lost_total_pnl = models.FloatField(null=True)
    lost_average_pnl = models.FloatField(null=True)
    lost_max_pnl = models.FloatField(null=True)
    # total_long_trades = models.IntegerField(null=True)
    # total_long_pnl = models.FloatField(null=True)
    # total_long_average_pnl = models.FloatField(null=True)
    # won_long_trades = models.IntegerField(null=True)
    # won_long_total_pnl = models.FloatField(null=True)
    # won_long_average_pnl = models.FloatField(null=True)
    # won_long_max_pnl = models.FloatField(null=True)
    # lost_long_trades = models.IntegerField(null=True)
    # lost_long_total_pnl = models.FloatField(null=True)
    # lost_long_average_pnl = models.FloatField(null=True)
    # lost_long_max_pnl = models.FloatField(null=True)
    # total_short_trades = models.IntegerField(null=True)
    # total_short_pnl = models.FloatField(null=True)
    # total_short_average_pnl = models.FloatField(null=True)
    # won_short_trades = models.IntegerField(null=True)
    # won_short_total_pnl = models.FloatField(null=True)
    # won_short_average_pnl = models.FloatField(null=True)
    # won_short_max_pnl = models.FloatField(null=True)
    # lost_short_trades = models.IntegerField(null=True)
    # lost_short_total_pnl = models.FloatField(null=True)
    # lost_short_average_pnl = models.FloatField(null=True)
    # lost_short_max_pnl = models.FloatField(null=True)
    total_trades_length = models.IntegerField(null=True)
    average_trades_per_day = models.FloatField(null=True)
    max_trades_per_day = models.IntegerField(null=True)
    min_trades_per_day = models.IntegerField(null=True)
    total_won_trades_length = models.IntegerField(null=True)
    average_won_trades_per_day = models.FloatField(null=True)
    max_won_trades_per_day = models.IntegerField(null=True)
    min_won_trades_per_day = models.IntegerField(null=True)
    total_lost_trades_length = models.IntegerField(null=True)
    average_lost_trades_per_day = models.FloatField(null=True)
    max_lost_trades_per_day = models.IntegerField(null=True)
    min_lost_trades_per_day = models.IntegerField(null=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ticker
    
class TransactionBacktest(models.Model):
    ticker = models.CharField(max_length=15)
    strategy = models.ForeignKey(StrategyTrading,on_delete=models.CASCADE, null=True, blank=True)
    nav =  models.FloatField()
    date_buy = models.DateField()
    qty =models.IntegerField()
    date_sell = models.DateField()
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    ratio_pln= models.FloatField()
    len_days = models.FloatField()
    stop_loss = models.FloatField()
    take_profit = models.FloatField()
    strategy = models.CharField(max_length=50)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker
    
class RatingStrategy(models.Model):
    strategy = models.ForeignKey(StrategyTrading,on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200, null=True)
    ratio_pln= models.FloatField()
    drawdown= models.FloatField(null=True)
    sharpe_ratio= models.FloatField(null=True)
    total_trades = models.IntegerField(null=True)
    total_open_trades = models.IntegerField(null=True)
    win_trade_ratio = models.FloatField(null=True)
    total_closed_trades = models.IntegerField(null=True)
    net_average_pnl = models.FloatField(null=True)
    won_total_trades = models.IntegerField(null=True)
    won_total_pnl = models.FloatField(null=True)
    won_average_pnl = models.FloatField(null=True)
    won_max_pnl = models.FloatField(null=True)
    lost_total_trades = models.IntegerField(null=True)
    lost_total_pnl = models.FloatField(null=True)
    lost_average_pnl = models.FloatField(null=True)
    lost_max_pnl = models.FloatField(null=True)
    total_trades_length = models.IntegerField(null=True)
    average_trades_per_day = models.FloatField(null=True)
    max_trades_per_day = models.IntegerField(null=True)
    min_trades_per_day = models.IntegerField(null=True)
    total_won_trades_length = models.IntegerField(null=True)
    average_won_trades_per_day = models.FloatField(null=True)
    max_won_trades_per_day = models.IntegerField(null=True)
    min_won_trades_per_day = models.IntegerField(null=True)
    total_lost_trades_length = models.IntegerField(null=True)
    average_lost_trades_per_day = models.FloatField(null=True)
    max_lost_trades_per_day = models.IntegerField(null=True)
    min_lost_trades_per_day = models.IntegerField(null=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.strategy
    
class ParamsOptimize(models.Model):  
    ticker = models.CharField(max_length=15)  
    strategy = models.ForeignKey(StrategyTrading,on_delete=models.CASCADE, null=True, blank=True)
    multiply_volumn = models.FloatField(default=2)
    rate_of_increase = models.FloatField(default=0.03)
    change_day = models.FloatField(default=0.015)
    ratio_cutloss= models.FloatField(default=0.05)
    sma = models.FloatField(default=20)

    def __str__(self):
        return self.ticker