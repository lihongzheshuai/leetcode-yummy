from decimal import Decimal

# 保留几位小数
quantize = Decimal("0.00")


def do_match(assets, funds, relationsa2f, relationsf2a, max_single_pay_ration, if_sort_asset):
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
    need_continue = True
    # 可调参数
    iter_count = 10
    while iter_count > 0:
        iter_count -= 1
        need_continue = False
        # 遍历资产方（资金需求方），计算份数和每份资金数
        for index in sorted_assets.keys():
            # 需求资金
            a_val = assets_reaming[index]
            if a_val <= 0:
                continue
            # 关联资金数组
            a_relations = relationsa2f[index]
            # 份数
            share_count = len(a_relations)
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
                need_continue = True
                # 当前资金方单笔可支付最大金额
                cur_max_count = (cur_fund_val * get_real_ration(max_single_pay_ration, relationsf2a[index])).quantize(
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
def get_real_ration(max_ration, cur_fund2asset_relation):
    if max_ration > 0:
        return max_ration
    rela_count = len((cur_fund2asset_relation))
    if rela_count == 1:
        return Decimal(1)
    else:
        return Decimal(1 / (rela_count - 1))


# ration 最大单笔支付比例（0,1] 小于0代表按照资产关联份数自动调配
# is_sort 是否按照关联资金数排序
def do_test(ratio, is_sort):
    # 资产方定义。值代表拥有的资产数
    assets = [Decimal(10), Decimal(20), Decimal(30), Decimal(40)]
    # 资金方定义，值代表拥有的资金数
    funds = [Decimal(20), Decimal(10), Decimal(30)]
    # 关联关系定义，从资产 -> 资金
    relationsa2f = [[0, 2], [0, 1, 2], [2], []]
    # 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
    relationsf2a = [[0, 1], [1], [0, 1, 2]]
    detail_result = {}
    detail_result[str(ratio)] = do_match(assets, funds, relationsa2f, relationsf2a, ratio, is_sort)
    print(detail_result)
    return do_match(assets, funds, relationsa2f, relationsf2a, ratio, is_sort)


# TODO 排序资产方
import operator


def sort_assets(assets, relations_a2f, if_sort):
    sorted_assets_map = rela_count_map = {}
    for idx in range(len(relations_a2f)):
        rela_count_map[idx] = len(relations_a2f[idx])
    sorted_assets_map = rela_count_map
    if if_sort:
        sorted_assets_map = dict(sorted(rela_count_map.items(), key=operator.itemgetter(1)))
    return sorted_assets_map


# auto
# do_test(-1, False)
for i in range(1, 11):
    ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
    do_test(ratio, True)

# for i in range(1, 11):
#     ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
#     do_test(ratio, True)
