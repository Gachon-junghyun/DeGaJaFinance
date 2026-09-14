import sys, re, urllib.request, html
rcp=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 4000
hdr={'User-Agent':'Mozilla/5.0','Referer':f'https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcp}'}
main=urllib.request.urlopen(urllib.request.Request(f'https://dart.fss.or.kr/dsaf001/main.do?rcpNo={rcp}',headers=hdr),timeout=30).read().decode('utf-8','ignore')
pairs=re.findall(r'viewDoc\("(\d+)",\s*"(\d+)"',main)
out=[f'rcpNo={rcp} viewDoc pairs: {pairs[:5]}']
if pairs:
    dcm=pairs[0][1]
    raw=urllib.request.urlopen(urllib.request.Request(f'https://dart.fss.or.kr/report/viewer.do?rcpNo={rcp}&dcmNo={dcm}&eleId=0&offset=0&length=0&dtd=HTML',headers=hdr),timeout=30).read()
    best=None
    for enc in ('cp949','utf-8'):
        t=raw.decode(enc,errors='replace'); h=sum(1 for c in t if '가'<=c<='힣'); q=t.count('�')
        if best is None or (h-q)>(best[0]): best=(h-q,enc,t)
    _,enc,txt=best; out.append(f'enc={enc}')
    txt=re.sub(r'<script.*?</script>','',txt,flags=re.S); txt=re.sub(r'<style.*?</style>','',txt,flags=re.S)
    txt=re.sub(r'<[^>]+>',' ',txt); txt=html.unescape(txt); txt=re.sub(r'[ \t\r\xa0]+',' ',txt); txt=re.sub(r'\n\s*\n+','\n',txt)
    out.append(txt[:n])
open(sys.argv[3],'w',encoding='utf-8').write('\n'.join(out))
