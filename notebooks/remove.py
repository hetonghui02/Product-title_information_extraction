import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('spec对比.xlsx')

# 遍历每个单元格，并进行处理
for col in df.columns:
    for i, cell in enumerate(df[col]):
        if isinstance(cell, str):
            # 删除方括号、单引号和逗号
            cell = re.sub(r'[\[\]\',]', '', cell)

            # 更新单元格的值
            df.at[i, col] = cell

# 保存修改后的Excel文件
df.to_excel('spec对比_处理后.xlsx', index=False)
