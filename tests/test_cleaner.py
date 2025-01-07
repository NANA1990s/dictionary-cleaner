import sys
import os

# 将项目根目录添加到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cleaner import DictionaryCleaner

def test_clean_dictionary():
    cleaner = DictionaryCleaner()
    
    test_cases = [
        # 基本例子
        (
            "abandon v. 抛弃；放弃：The captain refused to abandon his sinking ship. 船长拒绝弃船。",
            "abandon v. 抛弃；放弃"
        ),
        # 跨行例子（标记本来就在新行）
        (
            "word n. 词语：\nThis is an example.\n这是一个例子。\n[近义词] term",
            "word n. 词语\n[近义词] term"
        ),
        # 多种标记（标记在同一行）
        (
            "phrase v. 措辞：Choose your words carefully. 请谨慎用词。[用法说明] 常用于书面语【注】正式场合①书面语(多见于书面)",
            "phrase v. 措辞[用法说明] 常用于书面语【注】正式场合①书面语(多见于书面)"
        ),
        # 特殊标记（标记在同一行）
        (
            "test v. 测试 ||专业术语|| ①常用：This is a test. 这是测试。",
            "test v. 测试 ||专业术语|| ①常用"
        ),
        # 多个意思（标记在同一行）
        (
            "test v. ①测试，考查：This is a test. 这是一个测试。②检验，验证：Let's test this theory. 让我们验证这个理论。[近义词] examine",
            "test v. ①测试，考查②检验，验证[近义词] examine"
        ),
        # 复杂的多意思（标记在同一行）
        (
            "abandon v. ①抛弃；放弃：The captain refused to abandon his ship. 船长拒绝弃船。②停止：We had to abandon our plan. 我们不得不放弃计划。[近义词] desert, forsake",
            "abandon v. ①抛弃；放弃②停止[近义词] desert, forsake"
        )
    ]
    
    for input_text, expected in test_cases:
        cleaned = cleaner.clean_sentence(input_text)
        print(f"输入:\n{input_text}")
        print(f"\n清理后:\n{cleaned}")
        print(f"\n期望结果:\n{expected}")
        print(f"\n测试{'通过' if cleaned == expected else '失败'}")
        print("-" * 50)

if __name__ == "__main__":
    test_clean_dictionary()