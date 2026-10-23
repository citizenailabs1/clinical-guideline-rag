import requests  # library for downloading web pages

BASE = "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/"

# file name we want  ->  last part of the guideline's web address
GUIDELINES = {
    "colorectal": "colorectal-cancer-screening",
    "breast": "breast-cancer-screening",
    "diabetes": "screening-for-prediabetes-and-type-2-diabetes",
    "hypertension": "hypertension-in-adults-screening",
    "statins": "statin-use-in-adults-preventive-medication",
}

for name, slug in GUIDELINES.items():   # loop: repeat for each guideline
    response = requests.get(BASE + slug, timeout=30)
    if response.status_code == 200:      # 200 = OK
        with open(f"data/raw/{name}.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"OK      {name}  ({len(response.text) // 1000}K)")
    else:
        print(f"FAILED  {name}  status {response.status_code}")
        