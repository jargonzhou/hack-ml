import jieba
jieba.dt.tmp_dir = ".cache"

# NER模式
entity_ruler_patterns = [
    #  TEXTILE_FIBER: 纤维类型（如：羊毛、氨纶、尼龙）
    {"label": "纤维类型", "pattern": "羊毛"},
    {"label": "纤维类型", "pattern": "氨纶"},
    {"label": "纤维类型", "pattern": "尼龙"},
    {"label": "纤维类型", "pattern": "涤纶"},
    {"label": "纤维类型", "pattern": "棉花"},
    {"label": "纤维类型", "pattern": "纱线"},

    # TEXTILE_YARN: 纱线规格（如：精纺纱、40支纱）
    {"label": "纱线规格", "pattern": "精纺纱"},
    {"label": "纱线规格", "pattern": "40支纱"},

    # TEXTILE_WEAVE: 织物组织（如：平纹、缎纹、提花）
    {"label": "织物组织", "pattern": "平纹"},
    {"label": "织物组织", "pattern": "缎纹"},
    {"label": "织物组织", "pattern": "提花"},
    {"label": "织物组织", "pattern": "斜纹"},

    # TEXTILE_TECH: 生产工艺（如：丝光、起毛、预缩）
    {"label": "生产工艺", "pattern": "丝光"},
    {"label": "生产工艺", "pattern": "起毛"},
    {"label": "生产工艺", "pattern": "预缩"},
    {"label": "生产工艺", "pattern": "精梳"},

    # FABRIC_TYPE: 面料成品（如：帆布、雪纺、灯芯绒）
    {"label": "面料成品", "pattern": "帆布"},
    {"label": "面料成品", "pattern": "雪纺"},
    {"label": "面料成品", "pattern": "灯芯绒"},

    # PHYSICAL_PROP: 物理性能（如：克重、拉伸强度、色牢度）
    {"label": "物理性能", "pattern": "克重"},
    {"label": "物理性能", "pattern": "拉伸强度"},
    {"label": "物理性能", "pattern": "色牢度"},

]

# --- 模拟知识库文档 ---
knowledge_base = [
    "涤纶是一种合成纤维，具有优异的抗皱性和保形性。",
    "棉花是天然纤维，透气性好但容易皱。",
    "精梳工艺通过剔除短纤维来提升纱线的平滑度。",
    "斜纹组织织物表面有明显的斜向线条，常用于制作牛仔布。"
]

config = {
    "nlp": {
        "tokenizer": {
            "@tokenizers": "spacy.zh.ChineseTokenizer",
            # "segmenter": "jieba"
            "segmenter": "pkuseg"
        }
    }
}
