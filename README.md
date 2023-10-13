# CSV-Splitter
简介
CSV Splitter 是一个简易但功能强大的 Python 工具，专为那些需要将大型 CSV 文件分割为多个较小文件的用户设计。无论你是为了处理超大数据集，还是为了并行处理，此工具都是理想选择。

开始之前
确保你的系统上已安装了 Python（版本 3.6 或更高）。

安装
克隆此存储库到本地，或直接下载 ZIP 文件并解压。
```
git clone https://github.com/your-username/csv-splitter.git
```
进入 csv-splitter 目录。

```
cd csv-splitter
```
使用
将你想要分割的 CSV 文件命名为 full.csv 并放到 csv-splitter 目录中。

在终端或命令提示符中，执行脚本：
```
python split_csv.py
```
根据提示，输入 CSV 文件的总行数和你希望的拆分文件数量。

结果
你的文件将被分割为多个较小的 CSV 文件，如 split_01.csv, split_02.csv 等。

常见问题
编码问题: 如果遇到 UnicodeDecodeError，请确保你的 CSV 文件使用 'utf-8' 编码。

文件不存在: 如果遇到 FileNotFoundError，请确保你的 CSV 文件已被正确命名为 full.csv 并已放置在正确的目录中。

贡献 & 反馈
我们欢迎任何形式的贡献和反馈。请通过 Issues 提交问题或建议。
