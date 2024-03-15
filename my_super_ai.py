import superai as ai

client = ai.Client("your_api_key")

client.create_jobs(
    app_id="your_project_id",
    inputs=[{"image_url":"https://cdn.super.ai/cool-bulldog.jpg"},{"image_url":"https://cdn.super.ai/hot-dog-01.jpeg"}]
)
