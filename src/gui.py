import maliang

from elementalizer import elementalizer as ele


def update_result():
    if chk_ignore_tone.state == "normal-on":
        txt_result.texts[0].text = ele(ibx_source.texts[0].text, ignore_tone=True)
    else:
        txt_result.texts[0].text = ele(ibx_source.texts[0].text, ignore_tone=False)


root = maliang.Tk(title="文本-化学名称-转换器")
root.center()

cv = maliang.Canvas(auto_zoom=True, keep_ratio="min", free_anchor=True)
cv.place(width=1280, height=720, x=640, y=360, anchor="center")

maliang.Text(cv, (20, 50), text="请输入需要转换的文本：", fontsize=24, anchor="w")
ibx_source = maliang.InputBox(cv, (300, 50), size=(600, 40), fontsize=24, anchor="w")
chk_ignore_tone = maliang.CheckBox(cv, (920, 50), anchor="w", default=True)
maliang.Text(cv, (960, 50), text="忽略音调", fontsize=24, anchor="w")

maliang.Text(cv, (20, 100), text="转换结果：", fontsize=24, anchor="w")
txt_result = maliang.Text(cv, (300, 100), fontsize=24, anchor="w")
btn_copy = maliang.Button(cv, (920, 100), text="复制", fontsize=24, anchor="w", command=update_result)
maliang.Text(cv, (1000, 100), text="已复制到剪贴板", fontsize=24, anchor="w")


root.mainloop()
