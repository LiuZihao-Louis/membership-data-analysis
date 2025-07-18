from src.preprocessing import load_customer_data
from src.membership_analysis import (
    plot_monthly_growth,
    plot_membership_levels,
    plot_level_ratio_by_month,
    plot_total_level_ratio,
    plot_source_distribution
)

def main():
    filepath = 'data/会员信息查询.xlsx'
    customer_info = load_customer_data(filepath)

    # 图表展示
    plot_monthly_growth(customer_info)
    plot_membership_levels(customer_info)
    plot_level_ratio_by_month(customer_info)
    plot_total_level_ratio(customer_info)
    plot_source_distribution(customer_info)

if __name__ == '__main__':
    main()
