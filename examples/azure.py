from wizkid import AzureWizkid

# may change in the future
# https://learn.microsoft.com/en-us/azure/ai-services/wizkid/reference#rest-api-versioning
api_version = "2023-07-01-preview"

# gets the API Key from environment variable AZURE_WIZKID_API_KEY
client = AzureWizkid(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/wizkid/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.wizkid.azure.com",
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


deployment_client = AzureWizkid(
    api_version=api_version,
    # https://learn.microsoft.com/en-us/azure/cognitive-services/wizkid/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-resource.azure.wizkid.com/",
    # Navigate to the Azure Wizkid Studio to deploy a model.
    azure_deployment="deployment-name",  # e.g. gpt-35-instant
)

completion = deployment_client.chat.completions.create(
    model="<ignored>",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.model_dump_json(indent=2))
