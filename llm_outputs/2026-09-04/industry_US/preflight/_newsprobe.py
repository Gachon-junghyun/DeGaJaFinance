import subprocess, sys, time, json, datetime
terms = sys.argv[1:] or ["Federal Reserve","Nvidia","tariff","jobs report","oil prices","data center"]
out=[]
for i,t in enumerate(terms):
    if i: time.sleep(9)
    r = subprocess.run([sys.executable,"-X","utf8","-m","module_news_data","fts","search",t,
                        "--days","7","--count","--scope","foreign"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    line=(r.stdout or "").strip().replace("\n"," | ")
    print(f"{datetime.datetime.now():%H:%M:%S}  {t!r:28} rc={r.returncode}  {line[:200]}  ERR={(r.stderr or '').strip()[:120]}", flush=True)
