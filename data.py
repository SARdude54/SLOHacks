import csv

def get_data(file="static/Mapping_Police_Violence.csv") -> list[dict]:
    lst = []
    with open(file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            news_list = row[17].split("\n\n")
            data = {
                "name": row[0] if len(row[0]) != 0 else "NA",
                "age": row[1] if len(row[1]) != 0 else "NA",
                "gender": row[2] if len(row[2]) != 0 else "NA",
                "race": row[3] if len(row[3]) != 0 else "NA",
                "date": row[5] if len(row[5]) != 0 else "NA",
                "city": row[7] if len(row[7]) != 0 else "NA",
                "state": row[8] if len(row[8]) != 0 else "NA",
                "county": row[10] if len(row[10]) != 0 else "NA",
                "cause_of_death": row[13] if len(row[13]) != 0 else "NA",
                "circumstance": row[14] if len(row[14]) != 0 else "NA",
                "news_link": news_list,
                "case_status": row[15] if len(row[15]) != 0 else "NA",
                "officer_charged": row[16] if len(row[16]) != 0 else "NA"

            }
            lst.append(data)

    return lst


def get_result_list(data: list[dict], desired_city) -> str:
    result = []
    for incident in data:
        if incident["city"] == desired_city:
            result.append(incident)
        else:
            continue

    return result


