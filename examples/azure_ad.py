from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from wizkid import AzureWizkid

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")


# may change in the future
# https://learn.microsoft.com/en-us/azure/ai-services/wizkid/reference#rest-api-versioning
api_version = "2023-07-01-preview"

# https://learn.microsoft.com/en-us/azure/cognitive-services/wizkid/how-to/create-resource?pivots=web-portal#create-a-resource
endpoint = "https://my-resource.wizkid.azure.com"

client = AzureWizkid(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.model_dump_json(indent=2))
