import subprocess, sys
mods = ["module_KIS","module_news_data","module_flow","module_watchlist","module_paper_book",
        "module_valuation","module_business","module_business_us","module_disclosure",
        "module_disclosure_us","module_fundamentals_us","module_industry_map","module_report_tags",
        "module_inflection","module_macro_us","module_evidence","module_chart","module_epistemics",
        "module_math_check"]
scripts = ["sector_flow","us_live_shortlist","us_setup_screener","us_flow","flow_read","risk_units",
           "snapshot_estimates","exposure_rule","missed_ledger","kelly_size","catalyst_calendar",
           "report_lint","reject_ledger","drift_watch","cycle_exposure","action_bracket",
           "company_score","axis_inflection","axis_window_flow","margin_history","ic_ledger",
           "measure_ic","handoff_compact","handoff_id_audit","leak_scan"]
bad=[]; n=0
for m in mods:
    r=subprocess.run([sys.executable,"-X","utf8","-m",m,"--help"],capture_output=True,text=True,encoding="utf-8",errors="replace")
    n+=1
    print(f"{'OK ' if r.returncode==0 else 'FAIL'} -m {m}  exit={r.returncode}")
    if r.returncode: bad.append(("-m "+m, (r.stderr or r.stdout or "").strip().splitlines()[-1][:150] if (r.stderr or r.stdout) else ""))
for s in scripts:
    r=subprocess.run([sys.executable,"-X","utf8",f"scripts/{s}.py","--help"],capture_output=True,text=True,encoding="utf-8",errors="replace")
    n+=1
    print(f"{'OK ' if r.returncode==0 else 'FAIL'} scripts/{s}.py  exit={r.returncode}")
    if r.returncode: bad.append((s,(r.stderr or r.stdout or "").strip().splitlines()[-1][:150] if (r.stderr or r.stdout) else ""))
print(f"\n=== {n-len(bad)}/{n} exit 0 ===")
for b in bad: print("  FAIL:", b[0], "|", b[1])
