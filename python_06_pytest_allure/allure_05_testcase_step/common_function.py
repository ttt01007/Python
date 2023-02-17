import pytest


# 把每个缓解,写成函数

def login(username, password):
    '''登录'''
    print('前置操作:登录')


def open_goods():
    '''浏览商品'''
    print('浏览商品')


def add_shopping_cart(goods_id='10086'):
    '''添加购物车'''
    print('添加购物车')


def buy_goods():
    '''生成订单'''
    print('生成订单')


def pay_goods():
    '''支付'''
    print('支付')
