import matplotlib.pyplot as plt
from pylab import mpl
import pandas as pd

# 中文显示
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 有时候，字体更改后，会导致坐标轴中的部分字符无法正常显示，此时需要更改
mpl.rcParams['axes.unicode_minus'] = False


# 需求：会员月增量和月存量
def plot_monthly_growth(customer_info):
    cus_count = customer_info.pivot_table(index='注册年月', values='会员卡号', aggfunc='count')
    cus_count.rename(columns={'会员卡号': '月增量'}, inplace=True)
    cus_count['月存量'] = cus_count['月增量'].cumsum()

    # 由于铂金会员、钻石会员的月增量相比于白银、黄金过小，所以前者的展示使用折线图，纵坐标使用不同的单位（右侧）
    cus_count["月增量"].plot(figsize=(10, 10), color="red", legend=True, secondary_y=True)
    cus_count["月存量"].plot(figsize=(10, 10), color="gray", legend=True, kind="bar")
    plt.title("会员月增量与存量")
    plt.show()

# 需求：统计月增量会员中-会员等级分布
def plot_membership_levels(customer_info):
    member_count = customer_info.pivot_table(index='注册年月', columns='会员等级', values='会员卡号', aggfunc='count')

    # 可视化
    fig, ax1 = plt.subplots(figsize=(8, 4), dpi=500)
    ax2 = ax1.twinx()

    member_count[["白银会员", "黄金会员"]].plot(kind="bar", ax=ax1, ylabel="白银黄金")
    member_count[["铂金会员", "钻石会员"]].plot(ax=ax2, color=["red", "blue"], ylabel="铂金钻石")

    ax1.legend(loc="upper left")
    ax1.grid(linestyle="-.", alpha=0.7)
    ax2.legend(loc="upper right")
    plt.title("会员等级分布")
    plt.show()

# 需求：每月增量中会员等级占比
def plot_level_ratio_by_month(customer_info):
    member_count = customer_info.pivot_table(index='注册年月', columns='会员等级', values='会员卡号', aggfunc='count')
    member_count['总人数'] = member_count.sum(axis=1)
    member_count["黄金会员_占比"] = member_count["黄金会员"] / member_count["总人数"]
    member_count["白银会员_占比"] = member_count["白银会员"] / member_count["总人数"]

    member_count[["黄金会员_占比", "白银会员_占比"]].plot(ylabel="会员等级占比", grid=True)
    plt.title("每月新增会员等级占比")
    plt.show()

# 需求：会员分析-整体等级占比
def plot_total_level_ratio(customer_info):
    member_rate = customer_info.pivot_table(index='会员等级', values='会员卡号', aggfunc='count')
    member_rate.rename(columns={'会员卡号': '人数'}, inplace=True)
    member_rate["总人数"] = member_rate["人数"].sum()
    member_rate["占比"] = member_rate["人数"] / member_rate["总人数"]

    # 由于铂金会员/钻石会员占比较低, 绘图之前先调整在数据中的顺序, 让铂金会员和钻石会员在数据中不要相邻
    member_rate.loc[["白银会员", "铂金会员", "黄金会员", "钻石会员"], "占比"].plot(
        kind="pie", autopct="%.2f%%", ylabel=""
    )
    plt.title("整体会员等级占比")
    plt.axis("equal")
    plt.show()

# 需求：会员分析-整体等级占比
def plot_source_distribution(customer_info):
    channel_count = customer_info.pivot_table(index="注册年月", columns="会员来源", values="会员卡号", aggfunc="count")
    channel_count.plot(legend=True, grid=True)
    plt.title("每月会员来源占比")
    plt.ylabel("人数")
    plt.show()
