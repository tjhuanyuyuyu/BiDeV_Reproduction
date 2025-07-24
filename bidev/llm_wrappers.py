# # llm_wrappers.py
# from typing import List
# import openai
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# class GPTClient:
#     def __init__(self, model="gpt-3.5-turbo", temperature=0):
#         self.model = model
#         self.temperature = temperature

#     def chat(self, system: str, user: str) -> str:
#         resp = openai.ChatCompletion.create(
#             model=self.model,
#             temperature=self.temperature,
#             messages=[{"role": "system", "content": system},
#                       {"role": "user",   "content": user}]
#         )
#         return resp.choices[0].message.content.strip()

# class FlanT5Client:
#     def __init__(self, model_name="google/flan-t5-xl"):
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.model     = AutoModelForSeq2SeqLM.from_pretrained(
#             model_name, device_map="auto", torch_dtype="auto"
#         )

#     @torch.inference_mode()
#     def generate(self, prompt: str, max_new_tokens=128) -> str:
#         input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.model.device)
#         output_ids = self.model.generate(input_ids, max_new_tokens=max_new_tokens)
#         return self.tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()

# llm_wrappers.py
import os
import requests
from dotenv import load_dotenv

# 自动读取 .env 文件中的 API_KEY
load_dotenv()

class DashScopeClient:
    def __init__(self, api_key: str = None, model: str = "qwen-plus"):
        self.api_key = api_key or os.getenv("DASHSCOPE_API_KEY")
        self.model = model
        if not self.api_key:
            raise ValueError("Missing DashScope API Key. Set DASHSCOPE_API_KEY in .env or pass it explicitly.")

    def chat(self, system: str, user: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": self.model,
            "input": {
                "messages": [
                    {"role": "system", "content": system or "You are a helpful assistant."},
                    {"role": "user", "content": user}
                ]
            },
            "parameters": {
                "temperature": 0.3,
                "top_p": 0.95,
                "max_tokens": 1024
            }
        }

        try:
            resp = requests.post(
                "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation",
                headers=headers, json=data
            )
            resp.raise_for_status()
            return resp.json()["output"]["text"].strip()
        except Exception as e:
            return f"[ERROR] {e}"
