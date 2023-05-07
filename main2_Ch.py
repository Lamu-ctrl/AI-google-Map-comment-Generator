import openai
import json
import config

# 設定您的API密鑰
openai.api_key = config.APIKEY

# 餐廳菜單
menu = """
1. 家常豆腐
2. 魚香肉絲
3. 四川辣子雞
4. 麻婆豆腐
5. 糖醋排骨
"""

# GPT-4.0模型的輸入
prompt = f"根據以下餐廳菜單，請寫一篇類似sample中風格的餐廳評論：\n{menu}\n評論："

# 調用GPT-4.0模型
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.7,
)

# 輸出生成的評論
generated_review = response.choices[0].text.strip()
print(generated_review)
