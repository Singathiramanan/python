from csv import DictReader

def read_csv():
    """
    Reads the contents of the csv file into a list
    Each record of the list is a dictionary
    """
    records = [ ]
    with open("../data_files/covid-data.csv") as f:
        rows = DictReader(f)
        for row in rows:
            actual_data = {"country": row['location'], "date": row['date'], 'cases': int(row['new_cases'])}
            records.append(actual_data)
    return records

# total number of covid cases around the world
def total_cases():
    total = 0
    data = read_csv()
    for item in data:
        total = total + item['cases']
    return total

# {"India": 345874389, "USA": 938258349, "France": 3589349}
def total_cases_by_country():
    by_country = { }
    data = read_csv()
    for item in data:
        country = item['country']
        cases = item['cases']
        if country in by_country:
            by_country[country] = by_country[country] + cases
        else:
            by_country[country] = cases
    return by_country

def unique_countries():
    countries = set()
    data = read_csv()
    for item in data:
        countries.add(item['country'])
    return countries

def countries_less_10k():
    less_10k = { }
    by_country = total_cases_by_country()
    for country, cases in by_country.items():
        if cases < 10000:
            less_10k[country] = cases
    return less_10k

def top_10_most_cases():
    by_country = total_cases_by_country()
    sorted_d = sorted(by_country.items(), key=lambda item: item[-1])
    top_10 = sorted_d[-10:]
    return dict(top_10)

def least_10_most_cases():
    by_country = total_cases_by_country()
    sorted_d = sorted(by_country.items(), key=lambda item: item[-1])
    least_10 = sorted_d[:10]
    return dict(least_10)
