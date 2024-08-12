from pypinyin import pinyin, lazy_pinyin, load_single_dict, Style

# 元素名称列表
element_list = [
    '氢', '氦', '锂', '铍', '硼', '碳', '氮', '氧', '氟', '氖', 
    '钠', '镁', '铝', '硅', '磷', '硫', '氯', '氩', '钾', '钙', 
    '钪', '钛', '钒', '铬', '锰', '铁', '钴', '镍', '铜', '锌', 
    '镓', '锗', '砷', '硒', '溴', '氪', '铷', '锶', '钇', '锆', 
    '铌', '钼', '锝', '钌', '铑', '钯', '银', '镉', '铟', '锡', 
    '锑', '碲', '碘', '氙', '铯', '钡', '镧', '铈', '镨', '钕', 
    '钷', '钐', '铕', '钆', '铽', '镝', '钬', '铒', '铥', '镱', 
    '镥', '铪', '钽', '钨', '铼', '锇', '铱', '铂', '金', '汞', 
    '铊', '铅', '铋', '钋', '砹', '氡', '钫', '镭', '锕', '钍', 
    '镤', '铀', '镎', '钚', '镅', '锔', '锫', '锎', '锿', '镄',
    '钔', '锘', '铹', '𬬻', '𬭊', '𬭳', '𬭛', '𬭶', '鿏', '𫟼',
    '𬬭', '鿔', '鿭', '𫓧', '镆', '𫟷', '鿬', '鿫'
]

# 有机物名称列表
organic_list = [
    '烷', '烯', '炔', '烃',
    '醇', '醛', '酮', '醚', '酯', '酸', '酐', '酚', '酰', '醋',
    '醌', '酞',
    '苯', '蒽', '苄', '茚', '薁', '苊', '菲', '芴', '蒽', '荧',
    '芘', '蒄', '芥', '莰', '萘', '苷', '萜',
    '胺', '腈', '胩', '腙', '胍', '膦', '肼', '脲', '胲', '肟',
    '脒', '胱',
    '哌', '吡', '碇', '噻', '吩', '嘧', '呋', '喃', '𫫇', '咯',
    '吲', '哚', '嗪', '吖', '𫫇', '咪', '唑', '卟', '啉', '哆',
    '噌', '哒', '喹', '嘌', '呤', '啡'
]

# 其他名称列表
other_list = [
    '铵',
    '氨', '氰',
    '硝', '磺', '砜', '碱',
    '卤', '甾', '汀'
]

# 合并列表
name_list = element_list + organic_list + other_list

# 排除列表
exclude_list = [
    'a', 'ā', 'á', 'ǎ', 'à',
    'b', 'c', 'd',
    'e', 'ē', 'é', 'ě', 'è',
    'f', 'g', 'h',
    'i', 'ī', 'í', 'ǐ', 'ì',
    'j', 'k', 'l', 'm', 'n',
    'o', 'ō', 'ó', 'ǒ', 'ò',
    'p', 'q', 'r', 's', 't',
    'u', 'ū', 'ú', 'ǔ', 'ù',
    'v', 'w', 'x', 'y', 'z',
    'ǖ', 'ǘ', 'ǚ', 'ǜ',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z',
]

# 修正拼音
load_single_dict({ord('薁'): 'ào'})

# 拼音列表（含音调）
name_pinyin_tone = lazy_pinyin(name_list, style=Style.TONE)

# 拼音列表（不含音调）
name_pinyin_normal = lazy_pinyin(name_list, style=Style.NORMAL)

# 拼音名称映射（含音调）
name_pinyin_tone_dict = dict()
for i in range(len(name_list)):
    if name_pinyin_tone_dict.get(name_pinyin_tone[i]) == None:
        name_pinyin_tone_dict[name_pinyin_tone[i]] = [name_list[i]]
    else:
        same_pinyin_list = name_pinyin_tone_dict[name_pinyin_tone[i]]
        same_pinyin_list.append(name_list[i])
        name_pinyin_tone_dict[name_pinyin_tone[i]] = same_pinyin_list

# 拼音名称映射（不含音调）
name_pinyin_normal_dict = dict()
for i in range(len(name_list)):
    if name_pinyin_normal_dict.get(name_pinyin_normal[i]) == None:
        name_pinyin_normal_dict[name_pinyin_normal[i]] = [name_list[i]]
    else:
        same_pinyin_list = name_pinyin_normal_dict[name_pinyin_normal[i]]
        same_pinyin_list.append(name_list[i])
        name_pinyin_normal_dict[name_pinyin_normal[i]] = same_pinyin_list
