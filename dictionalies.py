month_conv = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    1:"Jan"
    }
print(month_conv[1])
print(month_conv["Feb"])
print(month_conv.get("Jan"))
print(month_conv.get("No"))
print(month_conv.get("none", "will print this instead"))
