import pandas as pd

def load_customer_data(filepath):
    customer_info = pd.read_excel(filepath)
    # 提取注册年月
    customer_info['注册年月'] = customer_info['注册时间'].apply(lambda reg_time: reg_time.strftime('%Y-%m'))
    return customer_info