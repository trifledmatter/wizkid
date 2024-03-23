import wizkid

# will default to `os.environ['WIZKID_API_KEY']` if not explicitly set
wizkid.api_key = "..."

# all client options can be configured just like the `Wizkid` instantiation counterpart
wizkid.base_url = "https://..."
wizkid.default_headers = {"x-foo": "true"}

# all API calls work in the exact same fashion as well
stream = wizkid.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)

print()
