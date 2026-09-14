import subprocess, sys, datetime
Q = [("S109 FRO corp action","Frontline",10),("S109 FRO corp action","Frontline Ltd",10),
     ("S109 OPEC supply","OPEC output",10),("S109 tanker rates","tanker rates",10),
     ("S114 Section 232","Section 232",12),("S114 steel tariff","steel tariff",12),
     ("S105 MRVL M&A","Marvell acquisition",16),("S105 AVGO M&A","Broadcom acquisition",16),
     ("S106 MSFT","Microsoft antitrust",16),("S106 MSFT","Microsoft acquisition",16),
     ("S107 T/VZ","spectrum auction",16),("S107 T/VZ","Verizon dividend",16),
     ("S141 export ctrl","export controls",4),("S141 export ctrl","semiconductor export",4),
     ("S132/138 AVGO","Broadcom guidance",4),("print corroboration","Broadcom earnings",4),
     ("print corroboration","HPE earnings",4),("print corroboration","Dell earnings",6),
     ("macro","jobs report",2),("macro","nonfarm payrolls",2),("macro","unemployment rate",2)]
for tag,q,days in Q:
    r = subprocess.run([sys.executable,"-X","utf8","-m","module_news_data","fts","search",q,
                        "--days",str(days),"--scope","foreign","--count"],
                       capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=180)
    print(f"{tag:22} {q!r:26} d{days:<3} -> {(r.stdout or '').strip()[:80]}", flush=True)
