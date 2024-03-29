import datetime
import json
import sys

def for_day(day, amount, member_names, stars):
    problem_dt = datetime.datetime(year=2022, month=12, day=day, hour=6)
    print(f"First {amount} users to get both stars on Day {day}:")
    for i, (dt, member) in enumerate(stars[day-1][1][:amount]):
        dt = datetime.datetime.fromtimestamp(dt)
        td = dt - problem_dt
        d = td.days
        total_s = td.total_seconds()
        h, rem = divmod(total_s, 60*60)
        m, s = divmod(rem, 60)
        print("{:3}) {}  {:02}:{:02}:{:02}  {}".format(
            i+1,
            dt.strftime("%b %d"),
            int(h%24),
            int(m),
            int(s),
            member_names[member]
        ))
    print(f"First {amount} users to get the first star on Day {day}:")
    for i, (dt, member) in enumerate(stars[day-1][0][:amount]):
        dt = datetime.datetime.fromtimestamp(dt)
        td = dt - problem_dt
        d = td.days
        total_s = td.total_seconds()
        h, rem = divmod(total_s, 60*60)
        m, s = divmod(rem, 60)
        print("{:3}) {}  {:02}:{:02}:{:02}  {}".format(
            i+1,
            dt.strftime("%b %d"),
            int(h%24),
            int(m),
            int(s),
            member_names[member]
        ))

def for_user(user, members, member_ids, stars):
    search_id = member_ids[user]
    max_score = min(100, len(members))
    print("      ----------Part 1----------   ----------Part 2----------")
    print("Day           Time   Rank  Score           Time   Rank  Score")
    for d, dstars in reversed(list(enumerate(stars))):
        if not dstars[0]:
            continue
        
        rank1 = 0
        rank2 = 0
        for solve in dstars[0]:
            if solve[1] == search_id:
                rank1 = (rank1, solve[0])
                break
            rank1 += 1
        else:
            rank1 = None

        for solve in dstars[1]:
            if solve[1] == search_id:
                rank2 = (rank2, solve[0])
                break
            rank2 += 1
        else:
            rank2 = None

        problem_dt = datetime.datetime(year=2022, month=12, day=d+1, hour=6)
        not_solved_fmt = ["-", "-", "-"]
        if rank1:
            rank1_dt = datetime.datetime.fromtimestamp(rank1[1])
            rank1_td = rank1_dt - problem_dt
            rank1_d = rank1_td.days
            rank1_total_s = rank1_td.total_seconds()
            rank1_h, rem = divmod(rank1_total_s, 60*60)
            rank1_m, rank1_s = divmod(rem, 60)
            rank1_fmt = [
                ">99d"
                if rank1_td.days > 99
                else "{:2}d {:02}:{:02}:{:02}".format(
                    int(rank1_d),
                    int(rank1_h%24),
                    int(rank1_m),
                    int(rank1_s),
                ),
                rank1[0] + 1,
                (max_score - rank1[0]) if rank1[0] < max_score else 0,
            ]
        else:
            rank1_fmt = not_solved_fmt

        if rank2:
            rank2_dt = datetime.datetime.fromtimestamp(rank2[1])
            rank2_td = rank2_dt - problem_dt
            rank2_d = rank2_td.days
            rank2_total_s = rank2_td.total_seconds()
            rank2_h, rem = divmod(rank2_total_s, 60*60)
            rank2_m, rank2_s = divmod(rem, 60)
            rank2_fmt = [
                ">99d"
                if rank2_td.days > 99
                else "{:2}d {:02}:{:02}:{:02}".format(
                    int(rank2_d),
                    int(rank2_h%24),
                    int(rank2_m),
                    int(rank2_s),
                ),
                rank2[0] + 1,
                (max_score - rank2[0]) if rank2[0] < len(members) else 0,
            ]
        else:
            rank2_fmt = not_solved_fmt

        print(" {:2}   {:>12}  {:>5}    {:>3}   {:>12}  {:>5}    {:>3}".format(
            d+1,
            *rank1_fmt,
            *rank2_fmt,
        ))


def main():
    obj = json.loads(open(sys.argv[1], "r").read())
    members = obj["members"]
    member_names = {mid: member["name"] if member["name"] else ("Anon " + str(member["id"])) for mid, member in members.items()}
    member_ids = {v: k for k, v in member_names.items()}
    if sys.argv[2] == "list":
        print("\n".join(list(sorted(member_ids, key=str.lower))))
        return

    stars = [([], []) for _ in range(25)]
    for m, member in members.items():
        for d, d_stars in member["completion_day_level"].items():
            if "1" in d_stars:
                stars[int(d)-1][0].append((d_stars["1"]["get_star_ts"], m))
            if "2" in d_stars:
                stars[int(d)-1][1].append((d_stars["2"]["get_star_ts"], m))
    for d in stars:
        d[0].sort()
        d[1].sort()

    if sys.argv[2] == "show":
        for_user(sys.argv[3], members, member_ids, stars)
    elif sys.argv[2] == "day":
        for_day(int(sys.argv[3]), int(sys.argv[4]), member_names, stars)


main()
