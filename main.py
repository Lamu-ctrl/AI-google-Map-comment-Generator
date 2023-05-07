import openai
import random
import config
# 設定API key
openai.api_key = config.APIKEY

# 設定GPT-4.0模型ID
model_engine = "text-davinci-002"

# 設定餐廳評論樣本
restaurant_reviews = [
    "The food was amazing and the service was excellent. Highly recommend this restaurant!",
    "The atmosphere was cozy and the food was delicious. Will definitely come back again.",
    "The staff was friendly and attentive, and the food was top-notch. A must-visit for foodies!",
    "The menu had a great variety of options and the dishes we ordered were all fantastic. Can't wait to try more!",
    "The presentation of the dishes was beautiful and the flavors were even better. A truly memorable dining experience."
]

# 隨機選擇一個餐廳評論樣本
review = random.choice(restaurant_reviews)

# 設定生成文本的長度
length = 100

# 設定生成文本的起始句子
prompt = f"I recently visited a restaurant and here's my review: {review} "

# 設定生成文本的條件
temperature = 0.7
max_tokens = length
top_p = 1
frequency_penalty = 0
presence_penalty = 0

# 使用GPT-4.0模型生成文本
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    frequency_penalty=frequency_penalty,
    presence_penalty=presence_penalty
)

# 取得生成的文本
generated_text = response.choices[0].text.strip()

# 輸出生成的文本
print(generated_text)
