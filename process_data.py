# 定义输入和输出文件路径
input_file = './data/A220bpm_SonR.TXT'
output_file = 'output_A220bpm_SonR.txt'

# 打开输入文件进行读取，输出文件进行写入
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # 逐行读取输入文件
    for line in infile:
        # 去除每行的空白字符（包括换行符）
        line = line.strip()
        
        # 检查每行是否是数字
        try:
            # 将数据转为浮动数值并乘以100
            num = float(line) * 1000000
            # 将结果写入输出文件
            outfile.write(f"{num:.3f}\n")
        except ValueError:
            # 如果某行无法转换为数字，跳过该行
            print(f"Warning: Skipping invalid line: {line}")
