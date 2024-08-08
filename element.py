from pypinyin import pinyin, lazy_pinyin, Style

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
    '𬬭', '鿔', '鿭', '𫓧', '镆', '𫟷', '鿬', '鿫']

# 元素拼音列表（含音调）
element_pinyin_tone = lazy_pinyin(element_list, style=Style.TONE)

# 元素拼音列表（不含音调）
element_pinyin_normal = lazy_pinyin(element_list, style=Style.NORMAL)

# 元素拼音名称映射（含音调）
element_pinyin_tone_dict = dict()
for i in range(len(element_list)):
    element_pinyin_tone_dict[element_pinyin_tone[i]] = element_list[i]

# 元素拼音名称映射（不含音调）
element_pinyin_normal_dict = dict()
for i in range(len(element_list)):
    element_pinyin_normal_dict[element_pinyin_normal[i]] = element_list[i]
    