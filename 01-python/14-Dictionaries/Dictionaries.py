convert_month = {
    "jan"  : "january",    # keys or values maybe anything not just str
    "feb"  : "february",
    "mar"  : "march"
}
# first way to print :
print(convert_month["mar"])

# second way to print :
print(convert_month.get("omar", "the value does not exist")) # output --> the value does not exist