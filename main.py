import PySimpleGUI as psg
import elementalizer as ele

layout = [
    [psg.Text('请输入需要转换的文本：'),
     psg.Input(key = 'txt_source', expand_x = True, enable_events = True)],

    [psg.Checkbox('忽略音调', key = 'chk_ignore_tone', default = False, enable_events = True)],

    [psg.Text('转换结果：'),
     psg.Text(key = 'txt_result'),
     psg.Button('重新生成', key = 'btn_regenerate'),
     psg.Button('复制结果', key = 'btn_copy'),
     psg.Text(key = 'txt_copy_hint', visible = False)]
]

window = psg.Window('化学名称文本转换器', layout)
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
    if event in ['txt_source', 'chk_ignore_tone', 'btn_regenerate']:
        if values['chk_ignore_tone']:
            result = ele.elementalizer(values['txt_source'], ignore_tone = True)
        else:
            result = ele.elementalizer(values['txt_source'], ignore_tone = False)

    # 更新结果
    window['txt_result'].update(result)

window.close()