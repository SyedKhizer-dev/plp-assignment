import requests
import json

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)

    posts = response.json()
    print(len(posts))
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.JSONDecodeError:
    print("Invalid JSON response")


# (b)
required_ids = [1, 25, 50, 100]

for post in posts:
    if post["id"] in required_ids:
        print("Title:", post["title"])
        print("Body:", post["body"])

# (c)
large_posts = []

for post in posts:
    post_body = post["body"].split()
    print(len(post_body))

    if len(post_body) > 5:
        large_posts.append(post["id"])

print("Large posts id:\n", large_posts)
print("Number of large posts: ", len(large_posts))

# (d)
posts_by_user = {}
for post in posts:
    if post["userId"] in posts_by_user:
        posts_by_user[post["userId"]].append(post["title"])
    else:
        posts_by_user[post["userId"]] = [post["title"]]

with open("posts_by_user.json", "w+") as f:
    json.dump(posts_by_user, f, indent=2)
