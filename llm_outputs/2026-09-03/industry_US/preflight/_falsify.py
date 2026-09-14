import sys, time, json
sys.path.insert(0, r"C:/Users/fivep/DeGaJaFinance")
sys.path.insert(0, r"C:/Users/fivep/DeGaJaFinance/scripts")
sys.stdout.reconfigure(encoding="utf-8")
import flow_read
NAMES = {"CRM":"Salesforce","SLB":"SLB","A":"Agilent Technologies","MDT":"Medtronic",
         "CTVA":"Corteva","BKR":"Baker Hughes","USB":"U.S. Bancorp","PCG":"PG&E",
         "SHOP":"Shopify","CI":"Cigna"}
out = {}
for i, (t, nm) in enumerate(NAMES.items()):
    q = flow_read._news_query(t, nm)
    try:
        r = flow_read.news_velocity(q, 7, 30, kr=False)
    except Exception as e:
        r = {"error": repr(e)}
    out[t] = {"query": q, **(r if isinstance(r, dict) else {"val": r})}
    print(f"{t:6s} q={q!r:38s} {r}", flush=True)
    if i < len(NAMES) - 1:
        time.sleep(9)
json.dump(out, open(r"C:/Users/fivep/DeGaJaFinance/llm_outputs/2026-09-03/industry_US/preflight/_falsify.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
