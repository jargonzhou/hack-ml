# PyTorch + Transformers

import dotenv
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

load_dotenv(".env/hf.env")

# 1. 定义模型 ID
model_id = "google/gemma-4-E4B-it"

# 2. 加载分词器 (Tokenizer)
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 3. 加载 PyTorch 模型
# device_map="auto" 会自动将模型权重放置在可用的 GPU (CUDA) 上
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.bfloat16,  # 推荐使用 bfloat16 以平衡显存与精度
    device_map="cpu"
)

# 4. 创建对话输入（基于 Gemma 的 Chat Template）
messages = [
    {"role": "user", "content": "用一句话解释什么是量子计算。"}
]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# 5. 推理生成
with torch.no_grad():
  outputs = model.generate(
      **inputs,
      max_new_tokens=150,
      do_sample=True,
      temperature=0.7
  )

# 6. 解码并打印输出结果
generated_tokens = outputs[0][inputs.input_ids.shape[-1]:]
response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
print(response)
