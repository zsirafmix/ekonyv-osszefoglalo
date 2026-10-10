import base64
s=open('/workspace/ekonyv/src.html').read()
for k,f in [('HERO','hero'),('LOGO','logo'),('UPLOAD','upload'),('SPOILER','spoiler')]:
    b=base64.b64encode(open(f'/workspace/ekonyv/assets/{f}.webp','rb').read()).decode()
    s=s.replace('{{'+k+'}}','data:image/webp;base64,'+b)
assert '{{' not in s
open('/workspace/ekonyv/ekonyv-osszefoglalo.html','w').write(s); open('/workspace/ekonyv/index.html','w').write(s)
print(len(s.encode()))
