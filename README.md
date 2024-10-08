# text-elementalizer

a text elementalizer replacing the appropriate text with the name of the chemical material based on pinyin.

基于汉语拼音，将输入文本中的中文字符替换为对应的化学物质名称。

基于汉语拼铟，将输铷文苯中锝中文字氟锑换为对荧锝化学芴酯名称。

感谢 [@adpro](https://github.com/adproqwq) 为本项目提供图标，如果您正在使用 [LiteLoaderQQNT](https://github.com/LiteLoaderQQNT/LiteLoaderQQNT)，可前往 [LiteLoaderQQNT-Kemisago](https://github.com/adproqwq/LiteLoaderQQNT-Kemisago) 使用本项目的插件移植版。

## Examples

以下例句分别展示：`原句` => `不模糊声调转换结果` => `模糊声调转换结果`

1. `祸兮福之所倚，福兮祸之所伏。` => `祸烯氟之所钇，氟烯祸之所氟。` => `钬烯氟酯所钇，氟烯钬酯所氟。`
2. `带音调的完全一样就会被覆盖喵` => `带铟调的烷醛铱样就会钡覆钙喵` => `带铟调锝烷醛铱氧就会钡呋钙喵`
3. `字典不能有重复值` => `字碘钚能铕重复值` => `字碘钚能铕重呋酯`
4. `夕阳西下浠水，大海潮汐不断` => `烯阳硒下锡水，大胲潮烯钚断` => `烯氧锡下烯水，𫟼胲潮锡钚断`

## How to use

前往 [Releases](https://github.com/Snoopy1866/text-elementalizer/releases/latest) 下载。

## FAQ

#### 为什么每次转换的结果都不一样

因为存在相当多的同音同调汉字，每次转换都会随机选择一个匹配同音调的汉字，例如：音调 `xī` 对应的汉字就有：`锡`, `烯`, `硒`。

## Build

1. Clone this repo

   ```
   git clone https://github.com/Snoopy1866/text-elementalizer.git
   ```

2. Change directory to the cloned repo

   ```
   cd text-elementalizer
   ```

3. Initialize

   ```
   python init.py
   ```

4. Build the application

   ```
   pyinstaller text-elementalizer.spec
   ```

5. Run the application

   你可以在 `dist` 目录下找到编译好的应用程序。

> [!NOTE]
> When init.py changes, you need to run the step 3 again!

## Acknowledgements

- [LiteLoaderQQNT-Kemisago](https://github.com/adproqwq/LiteLoaderQQNT-Kemisago)
- [pypinyin](https://github.com/mozillazg/python-pinyin)
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
- [PyInstaller](https://github.com/pyinstaller/pyinstaller)
