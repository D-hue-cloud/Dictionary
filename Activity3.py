countrycode={"India":"0091",
             "Australia":"0025",
             "Sri Lanka":"0094",
             "England":"0044",
             "Nepal":"009777"}

#search dictionary for country code for India
print("Country calling-code for India: ")
print(countrycode.get("India", "Not Found..."))

#search dictionary for code for UK
print("Country calling-code for England: ")
print(countrycode.get("England", "Not Found..."))

#searching dictionary for code for Nigeria
print("Country calling-code for Nigeria: ")
print(countrycode.get("Nigeria", "Not Found..."))