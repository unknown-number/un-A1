#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: UTF-8 -*-
import sys, re
from handlers import HTMLRenderer
from util import blocks
from rules import rule_list


class Parser:
    """
    解析器父类
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []     # 判断文本块规则的实例列表
        self.filters = []   # 过滤方法列表

    def addRule(self, rule):
        """
        向 self.rules 列表中添加规则类的实例
        """
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        """
        向 self.filters 列表中添加过滤函数
        """
        # 该过滤器函数接收两个参数：文本块和 HTMLRenderer 类的实例
        def filter(block, handler):
            # re.sub 接收三个参数 a b c ，将字符串 c 中的 a 字段替换成 b
            # b 的值可以是字符串或函数
            # 在下一行代码中 b 参数的值为 handler 的 sub 方法的返回值
            # sub 方法的参数 name 的值为字符串，它和 'sub_' 组成一个大字符串
            # 大字符串就是 handler 的一个方法名
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        """
        核心方法，解析文本，打印符合要求的标签，写入新的文件中
        """
        # 调用 handler 实例的 start 方法，参数为 handler 实例的某个方法名的一部分
        # 结果就是调用 handler 的 start_document 方法，打印文档的 head 标签
        self.handler.start('document')
        # blocks 是从 urti.py 文件引入的生成器函数
        # blocks(file) 就是一个生成器
        # 使用 for 循环生成器
        for block in blocks(file):
            # 调用过滤器，对每个文本块进行处理
            for filter in self.filters:
                block = filter(block, self.handler)
            # 循环规则类的实例
            for rule in self.rules:
                # 如果符合规则，调用实例的 action 方法打印标签
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    # 如果 action 方法的返回值为 True
                    # 表示该文本块处理完毕，结束循环
                    if last:
                        break
        # 同 self.handler.start
        # 调用 handler 的 end_document 方法打印 '</body></html>'
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    纯文本解析器
    """

    def __init__(self, handler):
        # 运行父类 Parser 的同名方法
        super().__init__(handler)
        # 增加规则类的实例到 self.urls 列表
        for rule in rule_list:
            self.addRule(rule)
        # 增加三个过滤函数，分别处理斜体字段、链接和邮箱
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


def main():
    '''
    主函数，控制整个程序的运行
    '''
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    # 将文件内容作为标准输入，sys.stdin 获取标准输入的内容，生成 IOWrapper 迭代器对象
    parser.parse(sys.stdin)


if __name__ == '__main__':
    main()

