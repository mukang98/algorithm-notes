#脚本传参
#[实现框架]分为1.sys.argv 2.argparse
#[框架1]
import sys
assert len(sys.argv) == 2
arg1 = sys.argv[1]
#[框架2] 更加地完备
import argparse
parser = argparse.ArgumentParser() #实例化
parser.add_argument("--date", type=str, required=True, default="20250207") #定义参数，default挺好用
args = parser.parse_args() #解析传参
arg1 = args.date # 赋值
