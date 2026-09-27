import json,csv
from pathlib import Path
p=Path(__file__).parent
d=json.loads((p/'master_family.json').read_text()); people={x['id']:x for x in d['people']}
aliases={'theodore_kramer_jacob':['Ted Jacob'],'edward_jacob':['Ed Jacob','Ed'],'theodore_jacob':['Ted Jacob (child)','Ted'],'joyce_jacob':['Joyce Jacob'],'william_jacob':['Bill Jacob','Bill'],'catherine_jacob':['Catherine Jacob']}
remove={'ted_jacob','ed_jacob','ted_child_jacob','joyce_child_jacob','bill_child_jacob'}
for k,v in aliases.items():people[k]['aliases']=v
for k in remove:people.pop(k,None)
d['people']=list(people.values())
for s,ids in d['photo_branches'].items():d['photo_branches'][s]=[i for i in ids if i in people]
(p/'master_family.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
with (p/'people.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['id','name','aliases','birth','death','sources','notes']);w.writeheader()
 for x in d['people']:w.writerow({**x,'aliases':'; '.join(x.get('aliases',[])),'sources':'; '.join(x['sources']),'notes':'; '.join(x['notes'])})
for source,ids in d['photo_branches'].items():
 filename='branch_'+source.split('.')[0].replace(' / ','_')+'.json'
 (p/filename).write_text(json.dumps({'source':source,'people':[people[i] for i in ids],'relationships':[e for e in d['relationships'] if e['source']==source]},ensure_ascii=False,indent=2),encoding='utf8')
review=[
('R01','Ed Jacob on 3621/3624','Edward Phillip Jacob on 3618–3620','likely same','Abbreviated name and matching position as Catherine and Theodore’s child. Confirm spouse Mary Pat Egan.'),
('R02','Ted Jacob (parent) on 3621/3624','Theodore Kramer Jacob on 3618–3620','likely same','Husband of Catherine Mary Egan Jacob; distinguish son Theodore (1938).'),
('R03','Ted Jacob (child) on 3621/3624','Theodore Jacob (1938) on 3618–3620','likely same','Both appear among Catherine and Theodore’s children.'),
('R04','Bill Jacob on 3621/3624','William Egan Jacob (1951) on 3618–3620','likely same','Both appear among Catherine and Theodore’s children.'),
('R05','Cathy on 3624','Catherine Jacob Haley (1943) on 3618–3621','possible','Surname and sibling position suggest match; handwritten Cathy is unconnected on 3624.'),
('R06','Kelay on 3624','Kelley on 3624','distinct unless corrected','Both appear under Ed on the sheet, but the handwriting may be Kelley and Kelay; clarify.'),
('R07','John O’Connor on 3623','Helen Egan O’Connor and Maurice O’Connor on 3623','generation unclear','Printed chart links the two couples directly but could omit a generation.'),
('R08','Mary B. Brown on 3622','Mary Egan Brown (1909) and Thomas Brown','parentage tentative','Drawing suggests Mary B. Brown is their child; confirm against family records.'),
('R09','Jeanmarie, Phil, Dutch on 3624','full legal names and surnames','needs input','Photo provides given names only; avoid filling them by assumption.'),
('R10','Theodore Jacob descendants on 3619','spouses versus children','needs input','Handwritten horizontal braces do not reliably show which names are spouses and which are children.'),
]
with (p/'REVIEW_QUEUE.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['id','name_or_relationship_a','name_or_relationship_b','status','question']);w.writerows(review)
(p/'REVIEW.md').write_text('# Review queue\n\nThe CSV lists identity candidates and unclear links. Do not merge a possible match solely because two people share a nickname. Record the decision and evidence in a commit.\n\n'+'\n'.join(f'- **{id} — {a} / {b}:** {q} ({status})' for id,a,b,status,q in review)+'\n',encoding='utf8')
print(len(people),len(d['relationships']))
