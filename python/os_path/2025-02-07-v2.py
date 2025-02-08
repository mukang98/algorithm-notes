#[核心思想]：将需要 [import模块的绝对地址] 加入 [sys.path] 
#[实现框架] - 实现主要借助os.path的api能力:os.path.[dirname/abspath/join]
#[步骤]：1.找到当前脚本的绝对路径 2.找到目标模块的绝对路径 3. 加入sys.path
import os, sys
current_path = os.path.dirname(os.path.abspath(__file__)) #1
src_path_up = os.path.join(os.path.abspath(os.path.join(current_path,'..','..')),"module")#2 向上回溯
src_path_down = os.path.abspath(os.path.join(current_path,"module1","module2"))#2 向下回溯
sys.path.append(src_path_up)#3
sys.path.append(src_path_down)#3