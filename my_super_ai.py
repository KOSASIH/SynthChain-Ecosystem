import superai as ai

client = ai.Client("2nodwtr18uvrqcskehvbqnu9geb85wgb4n8wuwc5uch9r532vkqqs577ak0stozn") 

client.create_jobs(
    app_id="63f4e18afd5a1b78762767ea",
    inputs=[{"image_url":"https://cdn.super.ai/cool-bulldog.jpg"},{"image_url":"https://cdn.super.ai/hot-dog-01.jpeg"}]
)
