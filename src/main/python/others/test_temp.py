import best_match
from decimal import Decimal

################### test temp ###################
# 实际存在资金剩余2的分配方案
is_print_detail = True
# 资产方定义。值代表拥有的资产数
assets = [Decimal('0.01'), Decimal('380473671'), Decimal('250295001'), Decimal('110054020')]
# 资金方定义，值代表拥有的资金数
funds = [Decimal('345344171.66'), Decimal('142953652.00'), Decimal('216514753.34'), Decimal('950976554')]
# 关联关系定义，从资产 -> 资金
relationsa2f = [[0, 2], [], [], []]
# 关联关系定义 从资金 -> 资产，a2f和f2a关系必须一致不能矛盾
relationsf2a = [[0], [], [0], []]
match_result = best_match.do_run(assets, funds, relationsa2f, relationsf2a, is_print_detail)
print()
print("用例【test temp】系统推荐方案")
print(match_result)
print()

# Traceback (most recent call last):
#   File ".\test_main.py", line 39, in <module>
#     main.main(day)
#   File "C:\Users\gaoliang\Documents\Data\Python\main.py", line 774, in main
#     step4(cursor)
#   File "C:\Users\gaoliang\Documents\Data\Python\main.py", line 643, in step4
#     match_result = best_match.do_run(trip_asset_left_list, trip_fund_left_list, relationsa2f, relationsf2a, is_print_detail_for_hongzhe)
#   File "C:\Users\gaoliang\Documents\Data\Python\best_match.py", line 172, in do_run
#     return check_result(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail)
#   File "C:\Users\gaoliang\Documents\Data\Python\best_match.py", line 177, in check_result
#     score_pay_remaining(result_list, score_map, assets, funds, relationsa2f, relationsf2a, is_print_detail)
#   File "C:\Users\gaoliang\Documents\Data\Python\best_match.py", line 235, in score_pay_remaining
#     cur_score += (1 - Decimal(total_remaining_volume / total_fund_volume).quantize(quantize)) * 100
# KeyboardInterrupt