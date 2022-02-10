# -*- coding: UTF-8 -*-
"""
  迭代工具模块
  """
import itertools

# 产生ABCD的全排列
print(itertools.permutations('ABCD'))
# 产生ABCDE的五选三组合
print(itertools.combinations('ABCDE', 3))

# 产生ABCD和123的笛卡尔积
print(itertools.product('ABCD', '123'))

# 产生ABC的无限循环序列
print(itertools.cycle(('A', 'B', 'C')))



