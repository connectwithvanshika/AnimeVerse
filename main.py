import requests
import pandas as pd
import time

url = "https://graphql.anilist.co"

query = """
query ($page:Int, $perPage:Int) {
  Page(page:$page, perPage:$perPage) {
    pageInfo {
      hasNextPage
    }

    media(type: ANIME) {
      id

      title {
        romaji
        english
        native
      }

      season
      seasonYear

      type
      format
      status

      episodes
      duration

      averageScore
      popularity
      favourites

      genres
      countryOfOrigin

      source

      studios(isMain:true){
        nodes{
          name
        }
      }

      rankings{
        rank
        type
      }

      startDate{
        year
        month
        day
      }
    }
  }
}
"""

all_anime = []

page = 1
per_page = 50

while True:

    variables = {
        "page": page,
        "perPage": per_page
    }

    response = requests.post(
        url,
        json={
            "query": query,
            "variables": variables
        }
    )

    data = response.json()

    if data.get("data") is None:
        print("API Error:")
        print(data)
        break

    anime_list = data["data"]["Page"]["media"]

    for anime in anime_list:

        studio = None

        if anime["studios"]["nodes"]:
            studio = anime["studios"]["nodes"][0]["name"]

        all_anime.append({
            "anime_id": anime["id"],
            "title_romaji": anime["title"]["romaji"],
            "title_english": anime["title"]["english"],
            "title_native": anime["title"]["native"],

            "season": anime["season"],
            "season_year": anime["seasonYear"],

            "type": anime["type"],
            "format": anime["format"],
            "status": anime["status"],

            "episodes": anime["episodes"],
            "duration": anime["duration"],

            "average_score": anime["averageScore"],
            "popularity": anime["popularity"],
            "favorites": anime["favourites"],

            "genres": ", ".join(anime["genres"])
                if anime["genres"] else None,

            "country": anime["countryOfOrigin"],

            "source_material": anime["source"],

            "studio": studio,

            "start_year": anime["startDate"]["year"],
            "start_month": anime["startDate"]["month"],
            "start_day": anime["startDate"]["day"]
        })

    print(f"Collected Page {page}")

    has_next = data["data"]["Page"]["pageInfo"]["hasNextPage"]

    if not has_next:
        break

    page += 1

    time.sleep(0.5)

df = pd.DataFrame(all_anime)

df.to_csv(
    "anilist_anime_dataset.csv",
    index=False
)

print("Saved:", len(df), "anime")