from pypinyin import pinyin, lazy_pinyin, Style
import name
import random

def elementalizer(source, ignore_tone = True):
    """
    基于汉语拼音，将字符串中的汉字转换为对应的化学词汇

    参数:
    - source: 待转换的字符串
    - ignore_tone: 是否模糊音调，默认为 True

    返回值:
    转换后的字符串
    """

    # 将源字符串转为列表
    source_list = list(source)

    # 生成源字符串的拼音列表
    source_pinyin_tone   = lazy_pinyin(source_list, style = Style.TONE)
    source_pinyin_normal = lazy_pinyin(source_list, style = Style.NORMAL)

    # 生成翻译字典
    translate_map = dict()
    if ignore_tone:
        for i in range(len(source_pinyin_tone)):
            source_char = source_list[i]
            pinyin_tone   = source_pinyin_tone[i]
            pinyin_normal = source_pinyin_normal[i]

            if source_char in name.exclude_list:
                continue
            elif pinyin_tone in name.name_pinyin_tone:
                candidate_list = name.name_pinyin_tone_dict[pinyin_tone]
                translate_map[source_char] = random.choice(candidate_list)
            elif pinyin_normal in name.name_pinyin_normal:
                candidate_list = name.name_pinyin_normal_dict[pinyin_normal]
                translate_map[source_char] = random.choice(candidate_list)
    else:
        for i in range(len(source_pinyin_tone)):
            source_char = source_list[i]
            pinyin_tone   = source_pinyin_tone[i]
            pinyin_normal = source_pinyin_normal[i]

            if source_char in name.exclude_list:
                continue
            elif pinyin_tone in name.name_pinyin_tone:
                candidate_list = name.name_pinyin_tone_dict[pinyin_tone]
                translate_map[source_char] = random.choice(candidate_list)

    translation = str.maketrans(translate_map)

    # 翻译源字符串
    source_translated = source.translate(translation)
    return(source_translated)
