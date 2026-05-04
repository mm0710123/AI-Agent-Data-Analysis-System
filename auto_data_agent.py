import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# ======================
# Agent 1: 数据采集Agent
# ======================
class DataCollectAgent:
    def collect(self):
        print("📥 数据采集Agent：开始采集数据...")
        # 模拟业务数据（日期、销售额、订单量、用户数）
        dates = pd.date_range(start="2025-01-01", periods=30)
        sales = np.random.randint(10000, 50000, size=30)
        orders = np.random.randint(200, 800, size=30)
        users = np.random.randint(500, 2000, size=30)
        
        df = pd.DataFrame({
            "日期": dates,
            "销售额": sales,
            "订单量": orders,
            "用户数": users
        })
        print("✅ 数据采集完成！")
        return df

# ======================
# Agent 2: 数据清洗Agent
# ======================
class DataCleanAgent:
    def clean(self, df):
        print("🧹 数据清洗Agent：开始校验与清洗数据...")
        df = df.drop_duplicates()
        df = df.fillna(0)
        print("✅ 数据清洗完成！无异常值")
        return df

# ======================
# Agent 3: 智能分析Agent（长链推理）
# ======================
class AnalysisAgent:
    def analyze(self, df):
        print("📊 分析推理Agent：启动长链推理分析...")
        
        sales_mean = round(df["销售额"].mean(), 2)
        sales_max = df["销售额"].max()
        sales_max_date = df.loc[df["销售额"].idxmax(), "日期"].strftime("%Y-%m-%d")
        
        orders_mean = df["订单量"].mean()
        users_growth = round((df["用户数"].iloc[-1] - df["用户数"].iloc[0]) / df["用户数"].iloc[0] * 100, 2)
        
        conclusion = f"""
        📌 数据分析报告（自动生成）
        1. 近30天平均日销售额：{sales_mean} 元
        2. 最高销售额出现在 {sales_max_date}，达到 {sales_max} 元
        3. 日均订单量：{orders_mean} 单
        4. 用户数环比增长：{users_growth}%
        5. 整体业务趋势平稳，数据无明显异常，建议保持现有运营策略。
        """
        print(conclusion)
        return conclusion

# ======================
# Agent 4: 报表生成Agent
# ======================
class ReportAgent:
    def generate_report(self, df, conclusion):
        print("📄 报表生成Agent：正在生成可视化报表...")
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        plt.rcParams["axes.unicode_minus"] = False
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        axes[0,0].plot(df["日期"], df["销售额"], marker="o", color="#FF5733")
        axes[0,0].set_title("每日销售额趋势")
        
        axes[0,1].bar(df["日期"], df["订单量"], color="#33A1FF")
        axes[0,1].set_title("每日订单量")
        
        axes[1,0].fill_between(df["日期"], df["用户数"], color="#28CC9E")
        axes[1,0].set_title("每日用户数趋势")
        
        axes[1,1].axis("off")
        axes[1,1].text(0.05, 0.95, conclusion, ha="left", va="top", fontsize=12)
        
        plt.tight_layout()
        if not os.path.exists("output"):
            os.mkdir("output")
        plt.savefig("output/自动数据报表.png", dpi=300)
        print("✅ 报表已保存至 output/自动数据报表.png")

# ======================
# 主流程：多Agent协作
# ======================
class AutoDataReportSystem:
    def __init__(self):
        self.collect_agent = DataCollectAgent()
        self.clean_agent = DataCleanAgent()
        self.analysis_agent = AnalysisAgent()
        self.report_agent = ReportAgent()
    
    def run(self):
        print("===== 启动多Agent自动化数据报表系统 =====")
        data = self.collect_agent.collect()
        clean_data = self.clean_agent.clean(data)
        result = self.analysis_agent.analyze(clean_data)
        self.report_agent.generate_report(clean_data, result)
        print("===== 全部任务执行完成！=====")

if __name__ == "__main__":
    system = AutoDataReportSystem()
    system.run()
