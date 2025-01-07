# Word文档词典例句清理工具

# Dictionary Cleaner

## 功能描述
这是一个专门用于处理词典格式 Word 文档的工具，仅删除词义解释后的英文例句及其中文翻译，保留文档中的所有其他内容（如近反义词、词性说明、谚语等）。

词典清理工具，用于清理词典中的例句，保留重要信息。

## 文档内容说明
词典文档包含以下类型的内容：
1. 需要处理的内容：
   - 词义解释后的冒号（中英文冒号）
   - 冒号后的英文例句（以英文句号结束）
   - 例句的中文翻译（以中文句号结束）
   - 注意：例句和翻译可能跨行

2. 需要保留的内容（不作任何处理）：
   - 单词本身
   - 词性标注
   - 中文释义
   - 其他标记内容，包括但不限于：
     * 方括号内容 [近义词] [反义词] [用法] [例] 等
     * 圆括号内容 (补充说明)
     * 【】【注】等中文方括号内容
     * ①②③等带圈数字标记
     * ||双竖线标记
     * 其他特殊格式标记

## 处理规则

1. 基本规则：
   - 保留冒号前的基本内容（单词和词性）
   - 删除冒号后的例句
   - 保留所有标记（方括号、圆括号等）和意思说明

2. 格式规则：
   - 保持原有的格式
   - 如果标记在原文中是独立的一行，清理后保持换行
   - 如果标记在原文中是连续的，清理后保持连续
   - 不对原本连续的内容强制换行

## 使用示例

python
from src.cleaner import DictionaryCleaner
cleaner = DictionaryCleaner()
基本例子
text = "abandon v. 抛弃；放弃：The captain refused to abandon his ship."
result = cleaner.clean_sentence(text)
结果: "abandon v. 抛弃；放弃"
带标记的例子
text = "test v. ①测试，考查：This is a test。[近义词] examine"
result = cleaner.clean_sentence(text)
结果: "test v. ①测试，考查[近义词] examine"


## 处理示例
原文：abandon v. 抛弃；放弃：The captain refused to abandon his sinking ship. 船长拒绝弃船。
[近义词] desert, forsake
[反义词] keep, maintain
[谚语] Never abandon hope.
处理后：
abandon v. 抛弃；放弃
[近义词] desert, forsake
[反义词] keep, maintain
[谚语] Never abandon hope.

原文：
abandon v. 抛弃；放弃：
The captain refused to abandon 
his sinking ship. 
船长拒绝弃船。
[近义词] desert, forsake
【注】常用于正式场合
①多用于贬义
(书面语居多)

处理后：
abandon v. 抛弃；放弃
[近义词] desert, forsake
【注】常用于正式场合
①多用于贬义
(书面语居多)

## 主要特性
- 仅处理特定格式的例句（冒号+英文例句+中文翻译）
- 保留所有其他内容不变
- 支持跨行例句和翻译的处理
- 自动生成新文件，保留原文件以便对比
- 保持文档格式不变

## 使用要求
- Python 3.6 或更高版本
- python-docx 库
- pytest 库（用于运行测试）


## 安装依赖
# 安装所有依赖
pip install -r requirements.txt

# 或者单独安装
pip install python-docx
pip install pytest

# 执行步骤
# 1. 安装依赖
pip install python-docx pytest

# 2. 验证安装
pip list | findstr "python-docx"
pip list | findstr "pytest"

## 使用方法
1. 将需要处理的词典文档放在工具同目录下
2. 运行脚本：
python clean_dictionary.py <input_file.docx>
3. 程序将在同目录下生成处理后的文件，命名为：`原文件名_cleaned.docx`

## 注意事项
- 处理前请备份重要文档
- 确保文档未被其他程序打开
- 建议处理完成后检查结果，确保：
  1. 所有例句都被正确删除
  2. 其他内容（近反义词、谚语等）都保持原样
  3. 文档格式未被破坏

## 注意事项

1. 标记处理：
   - 支持的标记类型：[]、【】、()、（）、||...||、①②③...
   - 标记可能包含说明文本，会一并保留
   - 保持标记的原有格式和位置

2. 换行处理：
   - 尊重原文的格式
   - 不对连续内容强制换行
   - 保持原有的换行结构

## 错误处理
如果发现处理结果有误，请检查：
1. 确认原文档中的标点符号使用是否规范（中文冒号、句号）
2. 检查是否存在特殊格式的例句结构
3. 确认被误删的内容是否符合"冒号+英文例句+中文翻译"的格式

## 版本历史
- v1.0.0: 初始版本

## 许可证
Apache-2.0 license


# Dictionary Cleaner

词典清理工具，用于清理词典中的例句，保留重要信息。

## 安装

bash
pip install python-docx

## 使用方法

### 命令行使用

bash
python clean_dictionary.py <input_file.docx>

例如：

bash
python clean_dictionary.py dictionary.docx


处理后会生成一个新文件：`dictionary_cleaned.docx`

### 作为模块使用

python

from clean_dictionary import clean_word_document

处理 Word 文档
clean_word_document("dictionary.docx")


## 处理规则

1. 基本规则：
   - 保留冒号前的基本内容（单词和词性）
   - 删除冒号后的例句
   - 保留所有标记（方括号、圆括号等）和意思说明

2. 格式规则：
   - 保持原有的格式
   - 如果标记在原文中是独立的一行，清理后保持换行
   - 如果标记在原文中是连续的，清理后保持连续
   - 不对原本连续的内容强制换行

## 支持的标记类型

- 方括号标记：[近义词]、[用法说明] 等
- 圆括号标记：(说明)、（补充）等
- 方括号标记：【注】等
- 双竖线标记：||专业术语|| 等
- 带圈数字：①②③④⑤⑥⑦⑧⑨⑩

## 注意事项

1. 只支持 .docx 格式的 Word 文档
2. 会生成新的文件，不会修改原文件
3. 输出文件名会自动添加 _cleaned 后缀