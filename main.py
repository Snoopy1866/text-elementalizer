import PySimpleGUI as psg
from elementalizer import elementalizer
import icon

# 事件-更新转换结果
def txt_result_update(source, ignore_tone = True):
    if ignore_tone:
        result = elementalizer(source, ignore_tone = True)
    else:
        result = elementalizer(source, ignore_tone = False)

    window['txt_result'].update(result)


# 界面布局
layout = [
    [psg.Text('请输入需要转换的文本：'),
     psg.Input(key = 'txt_source', expand_x = True, enable_events = True)],

    [psg.Checkbox('模糊音调', key = 'chk_ignore_tone', default = False, enable_events = True)],

    [psg.Text('转换结果：'),
     psg.Text(key = 'txt_result'),
     psg.Button('重新生成', key = 'btn_regenerate'),
     psg.Button('复制结果', key = 'btn_copy'),
     psg.Text(key = 'txt_copy_hint', visible = False)]
]

window = psg.Window('化学名称文本转换器', layout, icon = icon.icon)
last_source = ''
while True:
    event, values = window.read()

    print(event, values)
    if event == psg.WIN_CLOSED:
        break

    # 复制结果
    if event == 'btn_copy':
        psg.clipboard_set(window['txt_result'].get())
        window['txt_copy_hint'].update('已复制到剪贴板', visible = True)

    # 转换文本
    if event in ['txt_source']:
        current_source = values['txt_source']
        if current_source != last_source:
            txt_result_update(current_source, ignore_tone = values['chk_ignore_tone'])
            last_source = current_source
    elif event in ['chk_ignore_tone', 'btn_regenerate']:
        txt_result_update(current_source, ignore_tone = values['chk_ignore_tone'])

window.close()
