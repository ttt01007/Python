import decimal


class getBaseInfo():
    @classmethod
    def getBaseInfo(self, info):
        # 数据字典
        data = dict()
        # 按行组装数列
        r_text_list = info.splitlines()
        for i in r_text_list:
            if '#' == i[0]:
                continue
            j = i.split(' ')
            data[j[0]] = j[1]
        return data
    @classmethod
    def getBaseFinalInfo(self, finalInfo, netCard=None):
        # cpu空闲值
        cpu_idl = 0
        # cpu总值
        cpu_all = 0
        # mem空闲值
        mem_idl = 0
        # mem总量
        men_all = 0
        # disk下载
        disk_idl = 0
        # disk上传
        disk_all = 0
        # net下载
        net_idl = 0
        # net上传
        net_all = 0
        for i in finalInfo.keys():
            if 'node_cpu_seconds_total{cpu="0",mode="idle"}' == i:
                cpu_idl = decimal.Decimal(finalInfo[i])
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="iowait"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="irq"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="nice"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="softirq"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="steal"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="system"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_cpu_seconds_total{cpu="0",mode="user"}' == i:
                cpu_all += decimal.Decimal(finalInfo[i])
            elif 'node_memory_MemAvailable_bytes' == i:
                mem_idl = decimal.Decimal(finalInfo[i])
            elif 'node_memory_MemTotal_bytes ' == i:
                men_all = decimal.Decimal(finalInfo[i])
            elif i.__contains__('node_disk_read_bytes_total'):
                disk_idl += decimal.Decimal(finalInfo[1])
            elif i.__contains__('node_disk_written_bytes_total'):
                disk_all += decimal.Decimal(finalInfo[1])
            elif i.__contains__('node_network_receive_bytes_total'):
                if netCard == None:
                    net_idl += decimal.Decimal(finalInfo[1]) * 8
                else:
                    if i.__contains__(netCard):
                        net_idl += decimal.Decimal(finalInfo[1]) * 8
            # 上行宽带：node_network_transmit_bytes_total
            elif i.__contains__('node_network_transmit_bytes_total'):
                if netCard == None:
                    net_all += decimal.Decimal(finalInfo[1]) * 8
                else:
                    if i.__contains__(netCard):
                        net_all += decimal.Decimal(finalInfo[1]) * 8

        # print(cpu_idl)
        # print(cpu_all)
        # 精确计算小数位4位
        decimal.getcontext().prec = 4
        # 计算cpu空闲率
        cpu_use = cpu_idl / cpu_all
        # 计算cpu使用率
        cpu_unuse = 1 - cpu_use
        # 方便输出统计报告，百分比
        cpu_info = cpu_unuse * 100

        mem_use = mem_idl / men_all
        mem_unuse = 1 - mem_use
        mem_info = mem_unuse * 100

        # print('cpu_info:', cpu_info)
        # print('mem_info:', mem_info)
        # print(disk_idl)
        # print(disk_all)
        # print(net_idl)
        # print(net_all)
        # print((disk_idl + disk_all) / 1024 / 1024)
        # print((net_idl + net_all) / 1024 / 1024 / 1024)

        return [cpu_info, mem_info, (disk_idl + disk_all) / 1024 / 1024, (net_idl + net_all) / 1024 / 1024 / 1024]

    # if j[0].__contains__('node_cpu_seconds_total'):
    #     # 获取空闲值
    #     if j[0].__contains__('idle'):
    #         cpu_idl = decimal.Decimal(j[1])
    #     # 计算总cpu值
    #     cpu_all += decimal.Decimal(j[1])
    # # 获取men相关信息，内存空闲量：node_memory_MemAvailable_bytes，
    # elif 'node_memory_MemAvailable_bytes' == j[0]:
    #     mem_idl += decimal.Decimal(j[1])
    # # 内存总量：node_memory_MemTotal_bytes
    # elif 'node_memory_MemTotal_bytes' == j[0]:
    #     men_all += decimal.Decimal(j[1])
    # # 磁盘读取：node_disk_read_bytes_total
    # elif j[0].__contains__('node_disk_reads_completed_total'):
    #     disk_idl += decimal.Decimal(j[1])
    # # 磁盘写入：node_disk_written_bytes_total
    # elif j[0].__contains__('node_disk_writes_completed_total'):
    #     disk_all += decimal.Decimal(j[1])
    # # 下载宽带：node_network_receive_bytes_total
    # elif j[0].__contains__('node_network_receive_bytes_total'):
    #     if j[0].__contains__('eth0'):
    #         net_idl += decimal.Decimal(j[1]) * 8
    # # 上行宽带：node_network_transmit_bytes_total
    # elif j[0].__contains__('node_network_transmit_bytes_total'):
    #     if j[0].__contains__('eth0'):
    #         net_all += decimal.Decimal(j[1]) * 8
