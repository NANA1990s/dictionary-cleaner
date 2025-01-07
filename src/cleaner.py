# Copyright 2024 [NANA1990s]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
from typing import Dict, List, Optional
...

import re
from typing import Dict, List, Optional

class DictionaryCleaner:
    def __init__(self, config=None):
        """初始化清理器"""
        self.config = config or {}
        
    def is_english_example(self, text: str) -> bool:
        """判断是否为英文例句"""
        return bool(re.match(r'^[A-Za-z].*[.?!]$', text.strip()))
        
    def clean_sentence(self, text: str) -> str:
        """清理词典中的例句"""
        if not text:
            return ""
            
        # 按行分割文本
        lines = [line for line in text.split('\n') 
                if line.strip() and not self.is_english_example(line)]
        
        if not lines:
            return ""
            
        # 处理第一行（通常包含单词和词性）
        first_line = lines[0]
        
        # 查找第一行中的冒号
        colon_index = -1
        for c in ['：', ':']:
            pos = first_line.find(c)
            if pos != -1:
                if colon_index == -1 or pos < colon_index:
                    colon_index = pos
        
        # 获取基础内容
        if colon_index != -1:
            base_content = first_line[:colon_index].strip()
        else:
            base_content = first_line.strip()
            
        # 提取所有标记
        all_text = '\n'.join(lines)
        marks = []
        
        # 匹配所有标记
        pattern = r'(\[[^\]]*\][^：:]*|\【[^】]*】[^：:]*|\([^)]*\)[^：:]*|（[^）]*）[^：:]*|\|\|[^|]*\|\|[^：:]*|[①②③④⑤⑥⑦⑧⑨⑩][^：:①②③④⑤⑥⑦⑧⑨⑩]*)'
        
        for match in re.finditer(pattern, all_text):
            mark = match.group().strip()
            if mark and mark not in base_content:
                # 检查这个标记是否是独立的一行
                is_standalone = any(line.strip() == mark for line in lines[1:])
                marks.append((mark, is_standalone))
        
        # 组合结果
        result = base_content
        
        for mark, is_standalone in marks:
            if is_standalone:
                result += '\n' + mark
            else:
                result += mark
                
        return result