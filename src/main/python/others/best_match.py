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
    # 保存资产方获得资金数映射
    assets_receive = [None] * len(assets)
    # 保存每个需求方，每份资金金额
    asset_per_demand = [None] * len(assets)
    # 保存实时资金方余额
    funds_remaining = list(funds)
    # 保存实时资产方需求余量
    assets_reaming = {}
    for idx in range(len(assets)):
        assets_reaming[idx] = assets[idx]
    # 如果按照关联资金方升序排列
    sorted_assets = sort_assets(assets_reaming, relationsa2f, if_sort_asset)
    # 迭代次数
    temp_count = 0
    while temp_count <= iter_count:
        temp_count += 1
        # 遍历资产方（资金需求方），计算份数和每份资金数
        for index in sorted_assets.keys():
            # 当前资产方获得资金映射map
            cur_asset_receive_map = {} if assets_receive[index] is None else assets_receive[index]
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
                cur_max_count = (cur_fund_val * get_real_ration(max_single_pay_ration, relationsf2a[fund_index],
                                                                temp_count, pay_all_count)).quantize(quantize)
                # 定义Map保存付款映射关系
                cur_pay_map = {} if funds_pay[fund_index] is None else funds_pay[fund_index]
                cur_pay_count = 0
                if asset_per_demand[index] <= cur_max_count and asset_per_demand[index] <= cur_fund_val:
                    # 既小于余额又小于单笔自大限额，正常支付需求
                    cur_pay_count = asset_per_demand[index]
                elif asset_per_demand[index] > cur_max_count:
                    # 大于限额，按限额和余额里较小值支付
                    cur_pay_count = cur_max_count if cur_max_count < cur_fund_val else cur_fund_val
                else:
                    # 小于限额，但是余额不足了。全部支付
                    cur_pay_count = cur_fund_val
                # 保存手续结果到Map中
                if cur_asset_receive_map.get(fund_index) is None:
                    cur_asset_receive_map[fund_index] = cur_pay_count
                else:
                    cur_asset_receive_map[fund_index] += cur_pay_count
                # 保存支付结果到Map中
                if cur_pay_map.get(index) is None:
                    cur_pay_map[index] = cur_pay_count
                else:
                    cur_pay_map[index] += cur_pay_count
                assets_reaming[index] -= cur_pay_count
                funds_remaining[fund_index] -= cur_pay_count
                funds_pay[fund_index] = cur_pay_map
            assets_receive[index] = cur_asset_receive_map
    result["资金剩余"] = funds_remaining
    result["资产需求未满足量"] = assets_reaming
    result["资金方支付"] = funds_pay
    result["资产方获得"] = assets_receive
    return result


# 计算实际的单笔最大支付比例
# pay_all_count = 5 几轮以上全部支付
def get_real_ration(max_ration, cur_fund2asset_relation, cur_count, pay_all_count):
    if cur_count >= pay_all_count:
        return 1
    if max_ration > 0:
        return max_ration
    rela_count = len((cur_fund2asset_relation))
    if rela_count == 1:
        return Decimal(1)
    else:
        return Decimal(1 / (rela_count - 1))


import operator


def sort_assets(assets, relations_a2f, if_sort):
    sorted_assets_map = rela_count_map = {}
    for idx in range(len(relations_a2f)):
        rela_count_map[idx] = len(relations_a2f[idx])
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


def do_run(assets, funds, relationsa2f, relationsf2a, is_print_detail):
    score_map = {}
    result_list = []
    # 排序后
    if is_print_detail:
        print("排序后分配")
    for i in range(1, 11):
        ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
        result = do_match(assets, funds, relationsa2f, relationsf2a, ratio, True, 10, 5)
        result_list.append(result)
        if is_print_detail:
            print("比例【" + ratio.to_eng_string() + "】, 排序【是】, 迭代【10-5】")
            print(result)

    # 排序加自动
    if is_print_detail:
        print()
        print("排序后加自动计算分配比例")
    result = do_match(assets, funds, relationsa2f, relationsf2a, -1, True, 10, 5)
    result_list.append(result)
    if is_print_detail:
        print("比例【自动】, 排序【是】, 迭代【10-5】")
        print(result)

    if is_print_detail:
        print()
        print("不排序加自动计算分配比例")
    result = do_match(assets, funds, relationsa2f, relationsf2a, -1, False, 10, 5)
    result_list.append(result)
    if is_print_detail:
        print("比例【自动】, 排序【否】, 迭代【10-5】")
        print(result)

    # 未排序
    if is_print_detail:
        print()
        print("未排序分配")
    for i in range(1, 11):
        ratio = Decimal(0.1 * i).quantize(Decimal("0.0"))
        result = do_match(assets, funds, relationsa2f, relationsf2a, ratio, False, 10, 5)
        result_list.append(result)
        if is_print_detail:
            print("比例【" + ratio.to_eng_string() + "】, 排序【否】, 迭代【10-5】")
            print(result)
    # 推荐结果
    return check_result(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail)


def check_result(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail):
    score_pay_balance(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail)
    result_score_map = score_pay_remaining(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail)
    score_map_keys_list = list(result_score_map.keys())
    if not score_map_keys_list:
        print("未找到合适方案。")
        return {}
    score_map_keys_list.sort()
    return result_list[result_score_map.get(score_map_keys_list[-1])[0]]


# 基于支付平衡性打分
def score_pay_balance(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail):
    for result_idx in range(len(result_list)):
        result = result_list[result_idx]
        pay_list = list(result["资金方支付"])
        asset_unmap_remaining = dict(result["资产需求未满足量"])
        asset_receive_map_list = list(result["资产方获得"])
        # 首先将资产方有关联却未获得投资的结果剔除
        skip = False
        for asset_idx in range(len(asset_receive_map_list)):
            a_r_map = dict(asset_receive_map_list[asset_idx])
            if (a_r_map is None or len(a_r_map) == 0) and relationsa2f[asset_idx]:
                skip = True
                if is_print_detail:
                    print("资产方【" + str(asset_idx) + "】存在资金关联，但未获得资金")
        if skip:
            continue
        score = 0
        # 目前先检查是否每个资产方都得到满足，关联的越多得分越高
        for asset_idx in asset_unmap_remaining.keys():
            for pay_map in pay_list:
                if pay_map is None:
                    continue
                if pay_map.get(asset_idx) is not None:
                    score += 1
        # 保存分值和结果索引
        if score_map.get(score) is None:
            score_map[score] = [result_idx]
        else:
            score_map.get(score).append(result_idx)


# 基于资金剩余量打分
def score_pay_remaining(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail):
    total_fund_volume = 0
    for fund_volume in funds:
        total_fund_volume += fund_volume
    score_key_list = list(score_map.keys())
    score_key_list.sort()
    for score_key in score_key_list[::-1]:
        score_result_idx_list = score_map.get(score_key)
        for r_idx in score_result_idx_list:
            cur_score = score_key
            cur_result = result_list[r_idx]
            fund_remaining = cur_result["资金剩余"]
            # 计算总剩余量，最少分最高。公式: (1 - 总剩余量/总量) * 100。因此分值很高，比重很大。
            total_remaining_volume = 0
            for f_r_volume in fund_remaining:
                total_remaining_volume += f_r_volume
            cur_score += (1 - Decimal(total_remaining_volume / total_fund_volume).quantize(quantize)) * 100
            # 保存分值和结果索引
            result_score_map = {}
            if result_score_map.get(cur_score) is None:
                result_score_map[cur_score] = [r_idx]
            else:
                result_score_map.get(cur_score).append(r_idx)
    return result_score_map
