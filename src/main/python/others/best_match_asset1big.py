from decimal import Decimal

# 保留几位小数
quantize = Decimal("0.00")


def do_match(assets, funds, relationsa2f, relationsf2a, max_single_pay_ration, if_sort_asset, iter_count,
             pay_all_count):
    # 先检查关联关系
    if relationsa2f is None or len(relationsa2f) == 0:
        return []

    # 返回结果
    result = {}
    # 保存资金方付款记录映射数组+Map
    funds_pay = [None] * len(funds)
    # 保存每个需求方，每份资金金额
    asset_per_demand = [None] * len(assets)
    # 保存实时资金方余额
    funds_remaining = funds
    # 保存实时资产方需求余量
    assets_reaming = {}
    for idx in range(len(assets)):
        assets_reaming[idx] = assets[idx]
    # 如果按照关联资金方升序排列
    sorted_assets = sort_assets(assets_reaming, relationsa2f, if_sort_asset)
    # 可调参数
    while iter_count > 0:
        iter_count -= 1
        # 遍历资产方（资金需求方），计算份数和每份资金数
        for index in sorted_assets.keys():
            # 需求资金
            a_val = assets_reaming[index]
            if a_val <= 0:
                continue
            # 关联资金数组
            a_relations = relationsa2f[index]
            # 份数
            share_count = get_share_count(a_relations, funds_remaining)
            # 每份资金数
            if share_count != 0 and a_val > 0:
                asset_per_demand[index] = (Decimal(a_val) / Decimal(share_count)).quantize(quantize)
            else:
                asset_per_demand[index] = Decimal(0)
            # 遍历资金方，计算被需求金额，并与自身资金量比较
            for fund_index in a_relations:
                # 实时资金量
                cur_fund_val = funds_remaining[fund_index]
                if cur_fund_val <= 0:
                    continue
                # 当前资金方单笔可支付最大金额
                cur_max_count = (cur_fund_val * get_real_ration(max_single_pay_ration, relationsf2a[index],
                                                                iter_count, pay_all_count)).quantize(
                    quantize)
                # 定义Map保存付款映射关系
                cur_pay_map = {} if funds_pay[fund_index] is None else funds_pay[fund_index]
                cur_pay_count = 0
                if asset_per_demand[index] <= cur_max_count and asset_per_demand[index] <= cur_fund_val:
                    # 既小于余额又小于单笔自大限额，正常支付需求
                    cur_pay_count = asset_per_demand[index]
                elif asset_per_demand[index] > cur_max_count and asset_per_demand[index] <= cur_fund_val:
                    # 余额充足，但是大于大笔最大限额，按限额支付
                    cur_pay_count = cur_max_count
                else:
                    # 小于限额，但是余额不足了。全部支付
                    cur_pay_count = cur_fund_val
                # 保存支付结果到Map中
                if cur_pay_map.get(index) is None:
                    cur_pay_map[index] = cur_pay_count
                else:
                    cur_pay_map[index] += cur_pay_count
                assets_reaming[index] -= cur_pay_count
                funds_remaining[fund_index] -= cur_pay_count
                funds_pay[fund_index] = cur_pay_map
    result["资金剩余"] = funds_remaining
    result["资产需求未满足量"] = assets_reaming
    result["资金方支付"] = funds_pay
    return result


# 计算实际的单笔最大支付比例
# pay_all_count = 5 几轮以上全部支付
def get_real_ration(max_ration, cur_fund2asset_relation, iter_count, pay_all_count):
    if iter_count >= pay_all_count:
        return 1
    if max_ration > 0:
        return max_ration
    rela_count = len((cur_fund2asset_relation))
    if rela_count == 1:
        return Decimal(1)
    else:
        return Decimal(1 / (rela_count - 1))


# ration 最大单笔支付比例（0,1] 小于0代表按照资产关联份数自动调配
# is_sort 是否按照关联资金数排序
def do_test(ratio, is_sort, iter_count, pay_all_count):
    # 资产方定义。值代表拥有的资产数
    assets = [Decimal(120), Decimal(8), Decimal(18)]
    # 资金方定义，值代表拥有的资金数
    funds = [Decimal(10), Decimal(10), Decimal(20)]
    # 关联关系定义，从资产 -> 资金
    relationsa2f = [[0, 2], [0, 1, 2], [1, 2]]
    # 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
    relationsf2a = [[0, 1], [1, 2], [0, 1, 2]]
    detail_result = {}
    detail_result[str(ratio)] = do_match(assets, funds, relationsa2f, relationsf2a, ratio, is_sort, iter_count,
                                         pay_all_count)
    print(detail_result)
    return detail_result


import operator


def sort_assets(assets, relations_a2f, if_sort):
    sorted_assets_map = rela_count_map = {}
    for idx in range(len(relations_a2f)):
        rela_count_map[idx] = len(relations_a2f[idx])
    sorted_assets_map = rela_count_map
    if if_sort:
        sorted_assets_map = dict(sorted(rela_count_map.items(), key=operator.itemgetter(1)))
    return sorted_assets_map


def get_share_count(relations_a2f, funds_remaining):
    count = 0
    for fund_idx in relations_a2f:
        if funds_remaining[fund_idx] > 0:
            count += 1
    return count


def do_run():
    # 排序后
    print("排序后分配")
    recommend_result = {}
    max_score = 0
    for i in range(1, 11):
        ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
        result = do_test(ratio, True, 10, 5)
        cur_score = result_check(result[str(ratio)])
        if cur_score >= max_score:
            max_score = cur_score
            recommend_result = result
    # 排序加自动
    print("排序后加自动计算分配比例")
    result = do_test(-1, True, 10, 1)
    cur_score = result_check(result["-1"])
    if cur_score >= max_score:
        max_score = cur_score
        recommend_result = result
    # 未排序
    print("未排序分配")
    for i in range(1, 11):
        ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
        result = do_test(ratio, False, 3, 4)
        cur_score = result_check(result[str(ratio)])
        if cur_score >= max_score:
            max_score = cur_score
            recommend_result = result
    # 推荐结果
    print("系统推荐结果为")
    print(recommend_result)


def result_check(result):
    pay_list = list(result["资金方支付"])
    asset_unmap_remaining = dict(result["资产需求未满足量"])
    result = {}
    score = 0
    # 目前先检查是否每个资产方都得到满足，TODO 检查资金余额，分配均匀度等
    for asset_idx in asset_unmap_remaining.keys():
        for pay_map in pay_list:
            if pay_map.get(asset_idx) is not None:
                score += 1
    return score

do_run()
