import pandas as pd
import numpy as np


chat_id = 881258336 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')[1] 
    if p < 0.03:
      return True
    else:
      return False
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False
  
