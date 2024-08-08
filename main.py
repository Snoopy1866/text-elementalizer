from pypinyin import pinyin, lazy_pinyin, Style
import element

def elementalizer(source):
    # 将源字符串转为列表
    source_list = list(source)

    # 生成源字符串的拼音列表
    source_pinyin_tone   = lazy_pinyin(source_list, style = Style.TONE)
    source_pinyin_normal = lazy_pinyin(source_list, style = Style.NORMAL)

    # 生成翻译字典
    translate_map = dict()
    for i in range(len(source_pinyin_tone)):
        if source_pinyin_tone[i] in element.element_pinyin_tone:
            translate_map[source_list[i]] = element.element_pinyin_tone_dict[source_pinyin_tone[i]]
        else:
            if source_pinyin_normal[i] in element.element_pinyin_normal:
                translate_map[source_list[i]] = element.element_pinyin_normal_dict[source_pinyin_normal[i]]

    translation = str.maketrans(translate_map)

    # 翻译源字符串
    source_translated = source.translate(translation)
    return(source_translated)

# 简单交互
try:
    while True:
        source = input('请输入要翻译的字符串：')
        print('翻译结果：' + elementalizer(source))
except KeyboardInterrupt:
    pass
