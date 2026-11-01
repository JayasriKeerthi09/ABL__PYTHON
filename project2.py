plans = [
    {
        "name": "Basic Saver",
        "base": 199,
        "m_lim": 200,
        "d_lim": 5,
        "s_lim": 100,
    },
    {
        "name": "Value Pack",
        "base": 399,
        "m_lim": 500,
        "d_lim": 15,
        "s_lim": 300,
    },
    {
        "name": "Unlimited Max",
        "base": 599,
        "m_lim": 1000,
        "d_lim": 50,
        "s_lim": 500,
    },
]
mins, data, sms, budget = 450, 15, 100, 600
print(
    f"User Usage: {mins} Mins, {data} GB, {sms} SMS | Budget: Rs. {budget}"
)
print(
    f"{'Plan Name': <16}{'Base Cost': <12}{'Overages': <12}{'Total Cost': <12}{'Eligible?'}"
)
print("-" * 65)
best_plan, min_cost = None, float("inf")
for p in plans:
    e_m = max(0, mins - p["m_lim"])
    e_d = max(0, data - p["d_lim"])
    e_s = max(0, sms - p["s_lim"])
    overage = e_m * 1.0 + e_d * 20.0 + e_s * 1.0
    total = p["base"] + overage
    elig = "Yes" if total <= budget else "No"
    print(
        f"{p['name']: <16}Rs.{p['base']: <9}Rs.{overage:<9.2f}Rs.{total:<9.2f}{elig}"
    )
    if elig == "Yes" and total < min_cost:
        min_cost = total
        best_plan = p["name"]
print("-" * 65)
print(
    f"Recommended Optimal Plan: {best_plan} (Total Cost: Rs.{min_cost:.2f})"
)