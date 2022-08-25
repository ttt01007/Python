import decimal
import unittest
import requests
from decimal import *


class requestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @classmethod
    def setUp(self) -> None:
        pass

    def test_01_cpu(self):
        # 访问node_exporter，获取瞬时数据
        r = requests.get('http://101.43.160.228:9100/metrics')
        # 获取返回值
        r_text = r.text
        # 按行组装数列
        r_text_list = r_text.splitlines()
        # cpu空闲值
        cpu_idl = 0
        # cpu总值
        cpu_all = 0
        # mem空闲值
        mem_idl = 0
        # mem总量
        men_all = 0
        # disk空闲值
        disk_idl = 0
        # disk总量
        disk_all = 0
        # net空闲值
        net_idl = 0
        # net总量
        net_all = 0

        # 循环返回数列，获取有用数据
        for i in r_text_list:
            # 剔除#开头为注释的行
            if '#' == i[0]:
                continue
            # 每一行根据空格装入新数列
            j = i.split(' ')
            # 获取cpu相关信息，开头以node_cpu_seconds_total
            if j[0].__contains__('node_cpu_seconds_total'):
                # 获取空闲值
                if j[0].__contains__('idle'):
                    cpu_idl = decimal.Decimal(j[1])
                # 计算总cpu值
                cpu_all += decimal.Decimal(j[1])
            # 获取men相关信息，内存空闲量：node_memory_MemAvailable_bytes，
            elif 'node_memory_MemAvailable_bytes' == j[0]:
                mem_idl += decimal.Decimal(j[1])
            # 内存总量：node_memory_MemTotal_bytes
            elif 'node_memory_MemTotal_bytes' == j[0]:
                men_all += decimal.Decimal(j[1])
            # 磁盘读取：node_disk_read_bytes_total
            elif j[0].__contains__('node_disk_reads_completed_total'):
                disk_idl += decimal.Decimal(j[1])
                # print(disk_idl)
            # 磁盘写入：node_disk_written_bytes_total
            elif j[0].__contains__('node_disk_writes_completed_total'):
                disk_all += decimal.Decimal(j[1])
                # print(disk_all)
            # 下载宽带：node_network_receive_bytes_total
            elif j[0].__contains__('node_network_receive_bytes_total'):
                if j[0].__contains__('eth0'):
                    net_idl += decimal.Decimal(j[1]) * 8
                # print(net_idl)
            # 上行宽带：node_network_transmit_bytes_total
            elif j[0].__contains__('node_network_transmit_bytes_total'):
                if j[0].__contains__('eth0'):
                    net_all += decimal.Decimal(j[1]) * 8
                # print(net_all)

        print(cpu_idl)
        print(cpu_all)
        # 精确计算小数位4位
        getcontext().prec = 4
        # 计算cpu空闲率
        cpu_use = cpu_idl / cpu_all
        # 计算cpu使用率
        cpu_unuse = 1 - cpu_use
        # 方便输出统计报告，百分比
        cpu_info = cpu_unuse * 100

        mem_use = mem_idl / men_all
        mem_unuse = 1 - mem_use
        mem_info = mem_unuse * 100

        print('cpu_info:', cpu_info)
        print('mem_info:', mem_info)
        print(disk_idl)
        print(disk_all)
        print(net_idl)
        print(net_all)
        print((disk_idl + disk_all) / 1024 / 1024)
        print((net_idl + net_all) / 1024 / 1024 / 1024)