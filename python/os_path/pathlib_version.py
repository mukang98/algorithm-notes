from pathlib import Path
import sys

current_path = Path(__file__).resolve().parent  # 1
#C:\Users\wayne.yu\Desktop\个人项目\algorithm_notes\python\os_path\pathlib_version.py

src_path_up = (current_path / ".." / ".." / "module").resolve()        # 2 向上回溯
src_path_down = (current_path / "module1" / "module2").resolve()       # 2 向下回溯

sys.path.append(str(src_path_up))    # 3
sys.path.append(str(src_path_down))  # 3
