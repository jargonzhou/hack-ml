import pandas as pd
from typing import List
from llama_index.core.program import LLMTextCompletionProgram
from llama_index.core.bridge.pydantic import BaseModel, Field

from app.constants.models import llm


# 1. 用 Pydantic 定义单行记录的 Schema 格式


class DataRow(BaseModel):
  section: str = Field(
      description="The section title extracted from the text.")
  topics: str = Field(
      description="The matching topics extracted as a single string, separated by ','.")

# 2. 定义承载多行记录的复数容器


class DataFrameOutput(BaseModel):
  rows: List[DataRow] = Field(description="List of all extracted data rows.")


# 3. 编写文本转 DataFrame 的提示词模板
df_parser_template_str = """Extract rows of data from the text and format them into the requested structure.
Text input to analyze: {input_str}"""

# 4. 初始化结构化提取程序 (支持任何 LLM 实例)
program = LLMTextCompletionProgram.from_defaults(
    output_cls=DataFrameOutput,
    llm=llm,  # 传入你的 llm 实例
    prompt_template_str=df_parser_template_str,
)

# 5. 执行提取并直接生成 Pandas DataFrame
# 这里的 response 换成你从其他 Index/Query 处拿到的非结构化字符串
raw_response_text = """<MATHEMATICAL FOUNDATIONS, Linear Algebra Review, Complex Numbers, Hilbert Space, Dirac Notation, Unitary Operators, Tensor Products>
<QUANTUM GATES AND CIRCUITS, Single Qubit Gates, Pauli Gates, Hadamard Gate, Phase Shift Gates, Multi-Qubit Gates, CNOT Gate, Quantum Circuit Diagrams>
<QUANTUM ALGORITHMS I: FUNDAMENTALS, Quantum Parallelism, Deutsch-Jozsa Algorithm, Bernstein-Vazirani Algorithm, Simon's Algorithm, Quantum Teleportation, Superdense Coding>
<QUANTUM ALGORITHMS II: ADVANCED, Quantum Fourier Transform, Shor's Factoring Algorithm, Grover's Search Algorithm, Quantum Phase Estimation, Amplitude Amplification>
<QUANTUM ERROR CORRECTION, Decoherence and Noise, Quantum Bit Flip and Phase Flip, Shor Code, Steane Code, Surface Codes, Fault-Tolerant Quantum Computing>
<QUANTUM HARDWARE AND IMPLEMENTATIONS, Superconducting Qubits, Trapped Ions, Topological Qubits, Photonic Quantum Computing, NV Centers, Cryogenics and Control Electronics>
<ADVANCED TOPICS AND APPLICATIONS, Quantum Chemistry Simulation, Quantum Machine Learning, Quantum Cryptography, BB84 Protocol, Quantum Key Distribution, NISQ Era Challenges>
"""
extracted_data = program(input_str=raw_response_text)

# 6. 一行代码完成转换，彻底告别 to_df() 和旧版 append 的报错崩溃
df = pd.DataFrame([row.model_dump() for row in extracted_data.rows])
print(df)
