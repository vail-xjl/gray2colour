# gray2colour
在做弱半语义分割或无监督语义分割时，需要生成作为监督的掩码，而在类激活图首次生成伪掩码时是未着色（黑白）的伪掩码，为了提高可读性或视觉上的效果，我们需要将黑白伪掩码转换为彩色伪掩码，本代码提供此功能。

注：本代码只罗列了Pascal VOC2012数据集的着色板，若读者需要其他数据集的转换，只需替换着色板即可。
