import pandas as pd
import re

# 读取 Excel 文件
df = pd.read_excel("对比.xlsx")

# 将缺失值替换为空字符串
df.fillna('', inplace=True)

# 生成新的 spec 列
df['型号'] = df['款式'] + df['系列'] + df['功能功效'] + df['修饰'] + df['尺寸规格'] + df['颜色'] + df['风格'] +df['适用范围']
df['命名'] = df['品牌'] +df['型号'] +df['产品']

# 删除除了数字、汉字和字母以外的符号
df['spec_from_name' \
   ''] = df['spec'].apply(lambda x: re.sub(r'[^\w\u4e00-\u9fa5]', '', x))

# 保存到新的 Excel 文件
df.to_excel("spec对比.xlsx", index=False)
