# 资产方定义。值代表拥有的资产数
assets = [10, 20, 30, 40]
# 资金方定义，值代表拥有的资金数
funds = [20, 10, 30]
# 关联关系定义，从资产 -> 资金
relationsa2f = [[0, 2], [0, 1, 2], [2], []]
# 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
relationsf2a = [[0, 1], [1], [0, 1, 2]]
# 最大单笔支付比例（0,1]
max_single_ratio = 0.5


def do_match(assets, funds, relationsa2f, relationsf2a):
    # 先检查关联关系
    if relationsa2f is None or len(relationsa2f) == 0:
        return []

    # 保存资金方付款记录映射数组+Map
    funds_pay = []
    # 保存每个需求方，每份资金金额
    asset_per_demand = []
    # 遍历资产方（资金需求方），计算份数和每份资金数
    for index in range(len(assets)):
        # 需求资金
        a_val = assets[index]
        # 关联资金数组
        a_relations = relationsa2f[index]
        # 份数
        share_count = len(a_relations)
        # 每份资金数
        a_per_val = a_val / share_count
        asset_per_demand.append(a_per_val)

    # 遍历资金方，计算被需求金额，并与自身资金量比较
    for index in range(len(funds)):
        # 资金量
        f_val = funds[index]
        # 关联需求方数组
        f_relations = relationsf2a[index]
        # 遍历关联数组，计算给每个需求放款数量。这里有一个调优参数，最大单笔支付比例。
        for f_rela in f_relations:
            # TODO
            print(1)

print(do_match(assets, funds, relationsa2f, relationsf2a))
