## 许可证
本项目采用 [Apache License 2.0](LICENSE)。

Copyright 2024 [NANA1990s]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# Dictionary Cleaner

一个智能的词典清理工具，可以自动删除例句同时保留重要标记信息。

## 项目简介
这个工具可以帮助您快速清理词典文件中的例句，同时智能保留词性、用法说明、近义词等重要标记信息。它特别适合处理需要精简的词典文档。

## 功能特性
- 智能清理中英文例句
- 保留重要标记信息：
  - 词性标记
  - 用法说明 [用法]
  - 近义词标记 [近义词]
  - 补充说明 (说明)
  - 注释标记 【注】
  - 多重释义 ①②③
- 保持原有格式和换行
- 文件处理安全机制

## 快速开始

### 安装
1. 克隆项目：
```bash
git clone https://github.com/你的用户名/dictionary-cleaner.git
cd dictionary-cleaner
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

### 使用方法
基本用法：
```bash
python run.py data/your_dictionary.docx
```

### 使用示例
输入文本：
```text
abandon v. 抛弃；放弃：The captain refused to abandon his ship. 船长拒绝弃船。
phrase v. 措辞：Choose your words carefully. 请谨慎用词。[用法说明] 常用于书面语【注】正式场合
```

输出文本：
```text
abandon v. 抛弃；放弃
phrase v. 措辞[用法说明] 常用于书面语【注】正式场合
```

## 技术细节

### 支持的文件格式
- Microsoft Word (.docx)

### 标记处理规则
- 保留所有方括号标记 [用法] [近义词]
- 保留所有圆括号标记 (补充说明)
- 保留所有书名号标记 《》
- 保留所有注释标记 【注】
- 保留多重释义编号 ①②③

## 开发计划
- [ ] 批量处理多个文件
- [ ] 配置文件支持
- [ ] 更多文件格式支持
- [ ] 进度显示功能
- [ ] 日志记录系统
- [ ] 扩展单元测试

## 贡献
欢迎提交 Issue 和 Pull Request 来帮助改进项目。