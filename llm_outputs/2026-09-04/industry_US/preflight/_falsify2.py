import sys, time, json
sys.path.insert(0, r"C:/Users/fivep/DeGaJaFinance")

from module_flow._news_velocity import news_velocity, news_query
# (a) what query does the sweep actually build for the two zero names?
for tk,nm in [("SLB","SLB"),("MSTR","MicroStrategy")]:
    print(f"[query] {tk} -> {news_query(tk, nm)!r}", file=sys.stderr)
# (b) probe alternate surface forms
for q in ["Schlumberger","SLB","MicroStrategy","Strategy bitcoin","MSTR"]:
    r = news_velocity(q,7,30,kr=False)
    print(f"  {q!r:22} recent={r.get('recent')} base={r.get('base')} vel={r.get('velocity')} note={r.get('note','')}", file=sys.stderr)
    time.sleep(2)
# (c) burst test: 40 rapid queries, watch for a cutoff
uni = ["ORLY","MAR","CMI","PWR","AME","ROST","HES","VRSK","IDXX","OTIS","EA","YUM","NDAQ","MSCI",
       "IQV","GLW","KMB","EXC","CTSH","MCHP","VLTO","AVB","EBAY","FANG","DD","XYL","BKR","TSCO",
       "WAB","EFX","HIG","ANSS","HAL","DOV","MTD","STE","BR","PPG","CDW","ZBH"]
ok=0; first_none=None
for i,t in enumerate(uni):
    r = news_velocity(t,7,30,kr=False)
    v=r.get("velocity"); n=r.get("recent")
    if v is not None: ok+=1
    elif first_none is None: first_none=(i,t,r.get("note"))
    print(f"  burst#{i+1:02} {t:6} recent={n} vel={v}", file=sys.stderr, flush=True)
print(f"\n[burst] measured {ok}/{len(uni)} at ~0s spacing · first None at {first_none}", file=sys.stderr)
