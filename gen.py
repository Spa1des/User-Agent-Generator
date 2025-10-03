import random
import string

def gen_user_agent():
    os_win = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 10.0; WOW64",
        "Windows NT 11.0; Win64; x64",
        "Windows NT 11.0; WOW64",
    ]
    os_mac = [
        f"Macintosh; Intel Mac OS X 10_{random.randint(10,15)}_{random.randint(0,9)}",
        f"Macintosh; Intel Mac OS X 11_{random.randint(0,9)}_{random.randint(0,9)}",
    ]
    os_lin = [
        "X11; Linux x86_64",
        "X11; Linux i686",
        "X11; U; Linux x86_64",
        "X11; U; Linux i686",
    ]
    os_mobile = [
        f"Android {random.randint(6,14)}; Mobile",
        f"Android {random.randint(6,14)}; Tablet",
        f"iPhone; CPU iPhone OS {random.randint(10,17)}_{random.randint(0,9)} like Mac OS X",
        f"iPad; CPU OS {random.randint(10,17)}_{random.randint(0,9)} like Mac OS X",
    ]

    chrome_ver = f"{random.randint(90, 125)}.0.{random.randint(1000, 6000)}.{random.randint(10,150)}"
    firefox_ver = f"{random.randint(90, 115)}.0"
    safari_ver = f"{random.randint(600, 650)}.{random.randint(1,50)}.{random.randint(1,20)}"
    edge_ver = f"{random.randint(90, 125)}.0.{random.randint(1000, 6000)}.{random.randint(10,150)}"
    opera_ver = f"{random.randint(80, 110)}.0.{random.randint(1000, 6000)}.{random.randint(10,150)}"

    os_choice = random.choice(os_win + os_mac + os_lin + os_mobile)
    engine = random.choice([
        f"AppleWebKit/537.36 (KHTML, like Gecko)",
        f"Gecko/20100101"
    ])

    browser = random.choice([
        f"Chrome/{chrome_ver} Safari/{safari_ver}",
        f"Firefox/{firefox_ver}",
        f"Chrome/{chrome_ver} Safari/{safari_ver} Edg/{edge_ver}",
        f"Chrome/{chrome_ver} Safari/{safari_ver} OPR/{opera_ver}",
        f"Version/{random.randint(13,17)}.0 Safari/{safari_ver}"
    ])

    return f"Mozilla/5.0 ({os_choice}) {engine} {browser}"


if __name__ == "__main__":
    try:
        amount = int(input("How many user agents do you want to generate? "))
    except ValueError:
        print("Please enter a valid number!")
        exit()

    user_agents = [gen_user_agent() for _ in range(amount)]

    print("\nGenerated User Agents:\n")
    for ua in user_agents:
        print(ua)
    
    save = input("\nSave to file? (y/n): ").lower()
    if save == "y":
        with open("user_agents.txt", "w") as f:
            for ua in user_agents:
                f.write(f'"{ua}",\n')
        print("✅ Saved to user_agents.txt")
