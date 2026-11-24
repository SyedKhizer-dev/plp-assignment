import requests
import pandas as pd
import os


def main():

    # Data Extraction

    try:
        posts_response = requests.get(
            "https://jsonplaceholder.typicode.com/posts", timeout=5
        )
        users_response = requests.get(
            "https://jsonplaceholder.typicode.com/users", timeout=5
        )

        posts_data = posts_response.json()
        users_data = users_response.json()

        print("Total posts:", len(posts_data))
        print("Total users:", len(users_data))

    except requests.exceptions.ConnectionError:
        print("Connection failed")
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON data")

    # Data Transformation to Dataframe

    users_df = pd.DataFrame(users_data)
    posts_df = pd.DataFrame(posts_data)
    posts_df["word_count"] = posts_df["body"].apply(lambda x: len(x.split()))

    merge_df = pd.merge(posts_df, users_df, left_on="userId", right_on="id")

    filtered_df = merge_df[merge_df["word_count"] > 30]

    def category(word_count):
        if word_count <= 30:
            return "Short"
        elif word_count <= 50:
            return "Medium"
        else:
            return "Long"

    filtered_df["category"] = filtered_df["word_count"].apply(category)

    os.makedirs("output", exist_ok=True)
    filtered_df.to_csv("output/etl_result.csv", index=False)


if __name__ == "__main__":
    main()
