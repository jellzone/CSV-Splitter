import csv

def split_csv(filename, total_rows, num_files):
    # 计算每个文件大概需要多少行数据
    rows_per_file = total_rows // num_files
    # 如果不能整除，则最后一个文件会有一些额外的行
    remainder = total_rows % num_files

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i in range(1, num_files + 1):
            # 计算当前文件需要多少行
            current_rows = rows_per_file + 1 if i <= remainder else rows_per_file
            
            with open(f'split_{str(i).zfill(2)}.csv', 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                for _ in range(current_rows):
                    try:
                        row = next(reader)
                        writer.writerow(row)
                    except StopIteration:
                        # 如果数据已经读取完，则停止写入
                        break

if __name__ == '__main__':
    # 输入行数和需要拆分的文件数量
    total_rows = int(input('请输入总行数: '))
    num_files = int(input('请输入需要拆分的文件数量: '))
    
    split_csv('full.csv', total_rows, num_files)
