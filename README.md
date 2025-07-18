# 会员数据分析可视化项目

本项目基于Python使用Pandas与Matplotlib对会员注册数据进行分析，通过图表直观展示会员增长趋势、等级分布、会员来源渠道等关键业务指标。

## 项目结构

```
project/
├── data/                        # 数据存放目录
│   └── 会员信息查询.xlsx
│
├── src/                         # 核心代码模块
│   ├── preprocessing.py         # 数据加载与预处理
│   └── membership_analysis.py   # 数据分析与可视化
│
├── output/                      # 图表输出目录
│   ├── monthly_growth_and_stock.png
│   ├── membership_level_distribution.png
│   ├── monthly_level_ratio.png
│   ├── overall_level_ratio_pie.png
│   └── monthly_source_distribution.png
│
├── main.py                      # 主程序
└── README.md
```

## 分析功能与输出

| 功能                 | 描述                               | 输出图表                            |
| -------------------- | ---------------------------------- | ----------------------------------- |
| 会员月增量与月存量   | 分析会员增长趋势和总量变化         | `monthly_growth_and_stock.png`      |
| 会员等级分布         | 展示不同等级会员每月新增人数       | `membership_level_distribution.png` |
| 每月新增会员等级占比 | 统计各等级会员占当月新增会员的比例 | `monthly_level_ratio.png`           |
| 整体会员等级占比     | 饼图展示各等级会员总体占比         | `overall_level_ratio_pie.png`       |
| 每月会员来源渠道分布 | 分析不同来源渠道每月新增会员人数   | `monthly_source_distribution.png`   |

## 技术栈

- Python 3.x
- Pandas
- Matplotlib

## 数据字段说明

- `会员卡号`：用于统计人数
- `注册时间`：用于时间趋势分析
- `会员等级`：例如白银、黄金、铂金、钻石
- `会员来源`：例如线上、线下等

## 联系方式

欢迎交流反馈：

- Email: liuzihao2221@gmail.com
- GitHub: [LiuZihao-Louis](
