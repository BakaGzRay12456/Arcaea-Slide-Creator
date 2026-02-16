
import math
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
from typing import Union, List, Callable

class ArcAlgorithm:
    def laneToFloat(lane)->float:
        return format((2*lane-1)/8,'.3f')
    
import math
import numpy as np
import matplotlib.pyplot as plt

import math
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt

class Ease:
    """简单的缓动函数工具类"""
    
    @staticmethod
    def linear(t):
        return t
    
    @staticmethod
    def quad_in(t):
        return t * t
    
    @staticmethod
    def quad_out(t):
        return t * (2 - t)
    
    @staticmethod
    def quad_in_out(t):
        return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2
    
    @staticmethod
    def cubic_in(t):
        return t * t * t
    
    @staticmethod
    def cubic_out(t):
        return 1 - pow(1 - t, 3)
    
    @staticmethod
    def cubic_in_out(t):
        return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2
    
    @staticmethod
    def bounce_out(t):
        """弹跳效果"""
        if t < 1 / 2.75:
            return 7.5625 * t * t
        elif t < 2 / 2.75:
            t -= 1.5 / 2.75
            return 7.5625 * t * t + 0.75
        elif t < 2.5 / 2.75:
            t -= 2.25 / 2.75
            return 7.5625 * t * t + 0.9375
        else:
            t -= 2.625 / 2.75
            return 7.5625 * t * t + 0.984375

# 将插值函数移到类外面
def interpolate(start, end, t, ease_func=None):
    """
    在数值范围内进行插值
    
    Args:
        start: 起始值
        end: 结束值
        t: 进度 (0-1)
        ease_func: 缓动函数，默认使用线性
    
    Returns:
        插值结果
    """
    if not 0 <= t <= 1:
        raise ValueError("t must be between 0 and 1")
    
    if ease_func is None:
        ease_func = Ease.linear
    
    eased_t = ease_func(t)
    return start + (end - start) * eased_t

def interpolate_list(start, end, num_points, ease_func=None, include_end=True):
    """
    生成插值列表
    
    Args:
        start: 起始值
        end: 结束值
        num_points: 点数
        ease_func: 缓动函数，默认使用线性
        include_end: 是否包含终点
    
    Returns:
        插值结果列表
    """
    if ease_func is None:
        ease_func = Ease.linear
        
    if include_end:
        t_values = np.linspace(0, 1, num_points)
    else:
        t_values = np.linspace(0, 1, num_points, endpoint=False)
    
    return [interpolate(start, end, t, ease_func) for t in t_values]
EASE_FUNCTIONS = {
    "1": {"name": "线性", "func": Ease.linear},
    "2": {"name": "加速 (quad_in)", "func": Ease.quad_in},
    "3": {"name": "减速 (quad_out)", "func": Ease.quad_out},
    "4": {"name": "先加速后减速 (quad_in_out)", "func": Ease.quad_in_out},
    "5": {"name": "加速 (cubic_in)", "func": Ease.cubic_in},
    "6": {"name": "减速 (cubic_out)", "func": Ease.cubic_out},
    "7": {"name": "先加速后减速 (cubic_in_out)", "func": Ease.cubic_in_out},
    "8": {"name": "弹跳 (bounce_out)", "func": Ease.bounce_out},
}

def show_ease_menu():
    """显示缓动类型菜单"""
    print("\n=== 请选择缓动类型 ===")
    for key, value in EASE_FUNCTIONS.items():
        print(f"{key}. {value['name']}")

def get_ease_choice():
    """获取用户选择的缓动类型"""
    while True:
        try:
            choice = input("\n请输入数字选择: ").strip()
            if choice == "0":
                return None
            if choice in EASE_FUNCTIONS:
                return EASE_FUNCTIONS[choice]["func"]
            else:
                print("无效选择，请重新输入")
        except:
            print("输入错误，请重新输入")