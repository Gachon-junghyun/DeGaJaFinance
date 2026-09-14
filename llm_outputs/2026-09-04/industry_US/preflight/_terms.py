import subprocess, sys, re
TERMS = ["inflation","data center","tariff","Federal Reserve","rate hike","Strait of Hormuz",
         "crude oil","Treasury yield","payrolls","refinery","AI capex","credit spread",
         "bond selloff","Bessent","diesel"]
def run(args):
    r = subprocess.run([sys.executable,"-X","utf8","-m","module_news_data","fts","search",*args,
                        "--days","7","--count","--scope","foreign"],
                       capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=180)
    m = re.search(r"(\d+)", (r.stdout or "").strip())
    return int(m.group(1)) if m else None
print(f"{'term':22}{'phrase':>9}{'argvAND':>10}")
for t in TERMS:
    ph = run([t])
    av = run(t.split()) if " " in t else ph
    print(f"{t:22}{str(ph):>9}{str(av):>10}", flush=True)
