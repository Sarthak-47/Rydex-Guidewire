import urllib.request
urls = {
    'worker_dashboard.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2YzZmY0ZGViZGZlZTQ5OWFhYmVkNjlmNzJhMzdhM2EzEgsSBxCXz5e95xkYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDYzMjcxMjE0MTc5NTI3MzM0NQ&filename=&opi=89354086',
    'admin_dashboard.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2Y2OTJlMjEzOWRkNzQzNTQ5Nzk2YzZmYTU2ZGJjZDEyEgsSBxCXz5e95xkYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDYzMjcxMjE0MTc5NTI3MzM0NQ&filename=&opi=89354086',
    'register.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzFmNmE0NDBjMzA1MDQxODVhNGI0ZjkyNjhlZWZjMzZhEgsSBxCXz5e95xkYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDYzMjcxMjE0MTc5NTI3MzM0NQ&filename=&opi=89354086',
    'claim_detail.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzc1OGUxYmIwNDExNzQ3NDM4NmEyMWE5ODkzZDRiMzdiEgsSBxCXz5e95xkYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDYzMjcxMjE0MTc5NTI3MzM0NQ&filename=&opi=89354086',
    'login.html': 'https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzdlZDY5MDdmNWQwMzRlYTJhOTQwODE5YzA5NTQ2MTNjEgsSBxCXz5e95xkYAZIBJAoKcHJvamVjdF9pZBIWQhQxNDYzMjcxMjE0MTc5NTI3MzM0NQ&filename=&opi=89354086'
}
for name, url in urls.items():
    print(f"Downloading {name}...")
    urllib.request.urlretrieve(url, name)
print("Done")
