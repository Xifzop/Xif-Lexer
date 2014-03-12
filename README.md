Xif-Lexer
=========

自制的一个词法解析器，由Python实现。实现的基本程序结构是根据有限状态机来实现的，具体的请看version.1/state.machine.lex/下的有限状态机图。


Lexer根据给定的Pattern从一个源文件的字符流中，切分出一个个语素，格式为(<Type>, <Content>).
详细使用方法见version.x下的test.py, 其中需要的预定义类型以及pattern须在patterns.json下进行定义。

由于只是初等的词法解析器，可以满足一般情况下的词法解析，但是对于字符串类型中的一些常见问题还没能有很好的处理（字符串的转义，字符串的替换等等，这些都是要在后面的版本中继续完善的）。


Lexer进行初始化之后，需要导入或者手动添加相应的Pattern，如test.py中的导入patterns.json的示例。紧接着，制定源文件的名字，即可进行解析。由于Xif-Lexer的analyse方法是一个Python生成器，所以一般的使用方式为：

> for term in lexer.analyse(<source-file-name>):
> 		< use term code >


从而进行更近一步的语法解析。语法解析的版本会在后续推出。

