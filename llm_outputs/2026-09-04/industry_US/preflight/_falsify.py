"""G1 falsification: names the sweep scored velocity=None — are they silent, or refused?
Change ONE variable (request spacing) on a FIXED name set."""
import sys, json, time, csv
sys.path.insert(0, r"C:/Users/fivep/DeGaJaFinance")
from module_flow._news_velocity import news_velocity
NAMES = {"SLB":"SLB Schlumberger","CRM":"Salesforce","MDT":"Medtronic","DE":"Deere",
         "CTVA":"Corteva","HPE":"Hewlett Packard Enterprise","NEM":"Newmont",
         "MSTR":"MicroStrategy Strategy","TER":"Teradyne","JCI":"Johnson Controls"}
def probe(gap, tag):
    out={}
    for i,(t,q) in enumerate(NAMES.items()):
        if i: time.sleep(gap)
        try: r = news_velocity(q, 7, 30, kr=False)
        except Exception as e: r = {"velocity":None,"note":f"EXC {e}"}
        out[t]=r
        print(f"  [{tag}] {t:6} vel={r.get('velocity')}  recent={r.get('recent')} base={r.get('base')} src={r.get('source')} note={r.get('note','')}", file=sys.stderr, flush=True)
    return out
print("=== pass 1: 1.5s spacing ===", file=sys.stderr)
a = probe(1.5, "1.5s")
print("\n… 90s cooldown …", file=sys.stderr); time.sleep(90)
print("=== pass 2: 9s spacing, SAME names ===", file=sys.stderr)
b = probe(9.0, "9s")
n1=sum(1 for v in a.values() if v.get("velocity") is not None)
n2=sum(1 for v in b.values() if v.get("velocity") is not None)
flip=[t for t in NAMES if a[t].get("velocity") is None and b[t].get("velocity") is not None]
print(f"\n[result] measured at 1.5s: {n1}/10 · at 9s: {n2}/10 · None->number on cadence alone: {len(flip)} {flip}", file=sys.stderr)
json.dump({"fast":a,"slow":b,"flipped":flip}, sys.stdout, ensure_ascii=False, indent=1)
