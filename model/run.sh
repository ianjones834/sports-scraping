files=("mlb" "nba" "college-football" "nfl" "nhl")

rm './data/data.json'

for str in ${files[@]}; do
  rm "./tmp/${str}.jsonl"
  python3 -m scrapy runspider "./spiders/${str}_spider.py" -o "./tmp/${str}.jsonl"
done

python3 "./helpers/json-combiner.py"