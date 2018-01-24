import best_match
from decimal import Decimal

################### 用例1 ###################
# 实际存在资金剩余2的分配方案
is_print_detail = False
# 资产方定义。值代表拥有的资产数
assets = [Decimal(14), Decimal(8), Decimal(18)]
# 资金方定义，值代表拥有的资金数
funds = [Decimal(10), Decimal(10), Decimal(20)]
# 关联关系定义，从资产 -> 资金
relationsa2f = [[0, 2], [0, 1, 2], [2]]
# 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
relationsf2a = [[0, 1], [1], [0, 1, 2]]
match_result = best_match.do_run(assets, funds, relationsa2f, relationsf2a, is_print_detail)
print()
print("用例【1】系统推荐方案")
print(match_result)
print()

################### 用例2 ###################
is_print_detail = False
# 资产方定义。值代表拥有的资产数
assets = [Decimal(14), Decimal(8), Decimal(18)]
# 资金方定义，值代表拥有的资金数
funds = [Decimal(10), Decimal(10), Decimal(2000)]
# 关联关系定义，从资产 -> 资金
relationsa2f = [[0, 2], [0, 1, 2], [2]]
# 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
relationsf2a = [[0, 1], [1], [0, 1, 2]]
match_result = best_match.do_run(assets, funds, relationsa2f, relationsf2a, is_print_detail)
print()
print("用例【2】系统推荐方案")
print(match_result)
print()

################### 用例3 ###################
is_print_detail = True
# 资产方定义。值代表拥有的资产数
assets = [Decimal(18), Decimal(8), Decimal(120)]
# 资金方定义，值代表拥有的资金数
funds = [Decimal(10), Decimal(10), Decimal(20)]
# 关联关系定义，从资产 -> 资金
relationsa2f = [[0, 2], [0, 1, 2], [0, 2]]
# 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
relationsf2a = [[0, 1, 2], [1], [0, 1, 2]]
match_result = best_match.do_run(assets, funds, relationsa2f, relationsf2a, is_print_detail)
print()
print("用例【3】系统推荐方案")
print(match_result)
print()
