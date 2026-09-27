import json,csv,html
from pathlib import Path
P=Path(__file__).parent
people={}; edges=[]; sheets={}
def person(key,name,source,birth='',death='',note=''):
 if key not in people: people[key]={'id':key,'name':name,'birth':birth,'death':death,'sources':[],'notes':[]}
 p=people[key]
 if source not in p['sources']:p['sources'].append(source)
 if birth and not p['birth']:p['birth']=birth
 if death and not p['death']:p['death']=death
 if note and note not in p['notes']:p['notes'].append(note)
 sheets.setdefault(source,[])
 if key not in sheets[source]:sheets[source].append(key)
 return key
def link(a,b,typ,source,confidence='clear',note=''):
 e={'from':a,'to':b,'type':typ,'source':source,'confidence':confidence,'note':note}
 if not any(x['from']==a and x['to']==b and x['type']==typ for x in edges):edges.append(e)
def couple(a,b,s,confidence='clear',note=''):link(a,b,'partner',s,confidence,note)
def kids(parents,children,s,confidence='clear',note=''):
 for p in parents:
  for c in children:link(p,c,'parent',s,confidence,note)
s='3620.jpg / 3619.jpg / 3618.jpg'
person('john_egan','John Egan',s,'1874','1957');person('bridget_kane','Bridget Kane Egan',s,'1873','1931');couple('john_egan','bridget_kane',s)
for k,n,b,d in [('cornelius_egan','Cornelius J. Egan','1901','1925'),('william_m_egan','William M. Egan','1906','1987'),('helen_egan','Helen Egan O’Connor','1901','1970'),('catherine_egan','Catherine Egan Jacob','1916','2005'),('mary_egan','Mary Egan Brown','1909','1989'),('nora_egan','Nora B. Egan','1911','1934')]:person(k,n,s,b,d)
kids(['john_egan','bridget_kane'],['cornelius_egan','william_m_egan','helen_egan','catherine_egan','mary_egan','nora_egan'],s)
person('maurice_oconnor','Maurice O’Connor',s);couple('helen_egan','maurice_oconnor',s)
person('theodore_kramer_jacob','Theodore Kramer Jacob',s,'1909','1953');couple('catherine_egan','theodore_kramer_jacob',s,note='Marriage noted as 1938.')
person('thomas_brown','Thomas Brown',s);couple('mary_egan','thomas_brown',s)
for k,n,b,d in [('edward_jacob','Edward Phillip Jacob','1935','2006'),('theodore_jacob','Theodore Jacob','1938',''),('catherine_jacob','Catherine Jacob Haley','1943',''),('joyce_jacob','Joyce Jacob Stern','1947','2001'),('william_jacob','William Egan Jacob','1951','')]:person(k,n,s,b,d)
kids(['catherine_egan','theodore_kramer_jacob'],['edward_jacob','theodore_jacob','catherine_jacob','joyce_jacob','william_jacob'],s)
person('teresa_jacob','Teresa (Young?) Jacob', '3619.jpg',note='Maiden name handwriting uncertain.');couple('theodore_jacob','teresa_jacob','3619.jpg',note='Marriage noted as 1961.')
for k,n in [('tim_jacob','Tim Jacob'),('francie_jacob','Francie Jacob'),('mike_jacob','Mike Jacob'),('joyce_jacob_2','Joyce Jacob (daughter of Theodore)'),('jack_jacob','Jack Jacob'),('kira_jacob','Kira Jacob'),('connor_jacob','Connor Jacob'),('jim_jacob','Jim Jacob'),('lisa_jacob','Lisa Jacob'),('rick_jacob','Rick Jacob'),('debbie_jacob','Debbie Jacob')]:person(k,n,'3619.jpg')
kids(['theodore_jacob','teresa_jacob'],['tim_jacob','francie_jacob','mike_jacob','joyce_jacob_2','jack_jacob','kira_jacob','connor_jacob','jim_jacob','lisa_jacob','rick_jacob','debbie_jacob'],'3619.jpg',confidence='tentative',note='Handwritten brackets may group spouses and children differently; verify.')
for k,n in [('jeff_jacob','Jeff'),('jo_jacob','Jo'),('mary_jacob','Mary'),('kayla_jacob','Kayla'),('marc_jacob','Marc'),('dean_jacob','Dean'),('malisa_jacob','Malisa'),('bridget_jacob','Bridget'),('mila_jacob','Mila'),('jim_jr_jacob','Jim Jr'),('joe_jacob','Joe'),('lindsay_jacob','Lindsay'),('derrick_jacob','Derrick'),('jayson_jacob','Jayson')]:person(k,n,'3619.jpg',note='Placement on sheet; immediate parentage needs confirmation.')
for a,cs in [('tim_jacob',['jeff_jacob','jo_jacob']),('francie_jacob',['mary_jacob','kayla_jacob','marc_jacob']),('mike_jacob',['malisa_jacob']),('joyce_jacob_2',['bridget_jacob']),('jack_jacob',['dean_jacob']),('kira_jacob',['mila_jacob']),('jim_jacob',['jim_jr_jacob']),('lisa_jacob',['joe_jacob','lindsay_jacob']),('rick_jacob',['derrick_jacob']),('debbie_jacob',['jayson_jacob'])]:kids([a],cs,'3619.jpg','tentative','Vertical alignment only; confirm parentage.')
person('margaret_jacob','Margaret (Peggy) Jacob','3618.jpg','1953');couple('william_jacob','margaret_jacob','3618.jpg',note='Marriage noted as 1977.')
for k,n in [('jennifer_jacob','Jennifer R. Jacob'),('cherie_jacob','Cherie A. Jacob'),('ashlyn_cornelius','Ashlyn Cornelius')]:person(k,n,'3618.jpg')
kids(['william_jacob','margaret_jacob'],['jennifer_jacob','cherie_jacob'],'3618.jpg');kids(['jennifer_jacob'],['ashlyn_cornelius'],'3618.jpg')
s='3623.jpg'
person('john_oconnor','John O’Connor',s);person('jean_kramer','Jean Kramer O’Connor',s);couple('john_oconnor','jean_kramer',s);kids(['helen_egan','maurice_oconnor'],['john_oconnor'],s,'tentative','The printed connector implies descent but may omit an intervening generation; verify.')
for k,n in [('kevin_oconnor','Kevin'),('martin_oconnor','Martin'),('susan_oconnor','Susan'),('mary_oconnor','Mary'),('margaret_oconnor','Margaret'),('patricia_oconnor','Patricia'),('bridget_oconnor','Bridget')]:person(k,n,s)
kids(['john_oconnor','jean_kramer'],['kevin_oconnor','martin_oconnor','susan_oconnor','mary_oconnor','margaret_oconnor','patricia_oconnor','bridget_oconnor'],s)
for a,k,n in [('susan_oconnor','randy_brooks','Randy Brooks'),('mary_oconnor','darryll_daresh','Darryll Daresh'),('margaret_oconnor','craig_whitworth','Craig Whitworth'),('patricia_oconnor','patrick_luna','Patrick Luna'),('patricia_oconnor','scott_porto','Scott Porto'),('bridget_oconnor','perry_smith','Perry Smith')]:person(k,n,s);couple(a,k,s)
for k,n in [('christopher_oconnor','Christopher'),('sean_oconnor','Sean'),('kimberly_oconnor','Kimberly'),('ashlee_brooks','Ashlee'),('aric_brooks','Aric'),('allison_daresh','Allison'),('alex_daresh','Alex'),('megan_whitworth','Megan'),('connor_luna','Connor'),('payton_luna','Payton'),('olivia_luna','Olivia'),('kirsten_smith','Kirsten'),('kaleb_smith','Kaleb'),('kaden_smith','Kaden')]:person(k,n,s)
for a,cs in [('kevin_oconnor',['christopher_oconnor','sean_oconnor']),('martin_oconnor',['kimberly_oconnor']),('susan_oconnor',['ashlee_brooks','aric_brooks']),('mary_oconnor',['allison_daresh','alex_daresh']),('margaret_oconnor',['megan_whitworth']),('patricia_oconnor',['connor_luna','payton_luna','olivia_luna']),('bridget_oconnor',['kirsten_smith','kaleb_smith','kaden_smith'])]:kids([a],cs,s)
for k,n in [('stephen_sparks','Stephen Sparks'),('sky','Sky'),('triston_whitehead','Triston Whitehead'),('daniella','Daniella'),('luke_swanson','Luke Swanson'),('jenna','Jenna'),('jacob_boston','Jacob Boston'),('melissa','Melissa')]:person(k,n,s)
for a,b in [('ashlee_brooks','stephen_sparks'),('aric_brooks','sky'),('allison_daresh','triston_whitehead'),('alex_daresh','daniella'),('megan_whitworth','luke_swanson'),('payton_luna','jenna'),('kirsten_smith','jacob_boston'),('kaleb_smith','melissa')]:couple(a,b,s)
for a,cs in [('christopher_oconnor',['brienna']),('kimberly_oconnor',['tavin','tucker']),('ashlee_brooks',['jack_sparks','jordan_sparks']),('aric_brooks',['shawn_brooks']),('allison_daresh',['gunner','gage','gatlin']),('alex_daresh',['finley']),('payton_luna',['katelyn']),('kirsten_smith',['beau','blair'])]:
 for k in cs:person(k,k.replace('_',' ').title(),s)
 kids([a],cs,s)
s='3622.jpg'
for k,n,b,d in [('jerome_teitz','Jerome Teitz','1937','2025'),('mary_b_brown','Mary B. Brown','1938',''),('kathleen_teitz','Kathleen Teitz Hornyak','1960',''),('thomas_n_teitz','Thomas N. Teitz','1962',''),('amy_teitz','Amy Teitz Bauer','1963',''),('robert_hornyak','Robert (Bob) Hornyak','1951',''),('claire_mulvey','Claire Mulvey','1964',''),('james_bauer','James (Jim) Bauer','1957',''),('evan_hornyak','Evan Hornyak','1998',''),('emily_hornyak','Emily Hornyak','1992',''),('thomas_tj','Thomas (TJ) Teitz','1998',''),('sean_teitz','Sean Teitz','2001',''),('caitlin_bauer','Caitlin Bauer','1992',''),('michael_bauer','Michael Bauer','1986',''),('shannon_o','Shannon O.','1989',''),('ryleigh','Ryleigh','2019','')]:person(k,n,s,b,d)
couple('mary_b_brown','jerome_teitz',s,note='Marriage noted as 1960.');kids(['mary_b_brown','jerome_teitz'],['kathleen_teitz','thomas_n_teitz','amy_teitz'],s)
for a,b in [('kathleen_teitz','robert_hornyak'),('thomas_n_teitz','claire_mulvey'),('amy_teitz','james_bauer'),('evan_hornyak','shannon_o')]:couple(a,b,s)
for ps,cs in [(['kathleen_teitz','robert_hornyak'],['evan_hornyak','emily_hornyak']),(['thomas_n_teitz','claire_mulvey'],['thomas_tj','sean_teitz']),(['amy_teitz','james_bauer'],['caitlin_bauer','michael_bauer']),(['evan_hornyak','shannon_o'],['ryleigh'])]:kids(ps,cs,s)
link('mary_egan','mary_b_brown','parent',s,'tentative','Drawing connects Mary C. Egan / Thomas Brown to Mary B. Brown; verify given initial.')
link('thomas_brown','mary_b_brown','parent',s,'tentative','Drawing implies this relationship.')
s='3621.jpg'
person('ted_jacob','Ted Jacob',s,note='Likely Theodore Kramer Jacob; merged tentatively with that record.');couple('catherine_egan','theodore_kramer_jacob',s)
for k,n in [('ed_jacob','Ed Jacob'),('ted_child_jacob','Ted Jacob (child)'),('joyce_child_jacob','Joyce Jacob'),('bill_child_jacob','Bill Jacob')]:person(k,n,s)
for a,b in [('ed_jacob','edward_jacob'),('ted_child_jacob','theodore_jacob'),('joyce_child_jacob','joyce_jacob'),('bill_child_jacob','william_jacob')]:person(b,people[b]['name'],s,note='Same person as abbreviated label on this photo.')
for k,n in [('joseph_haley','Joseph Dennis Haley'),('amy_haley','Amy Haley (Banyasz)'),('tom_haley','Tom Haley'),('debbie_haley','Debbie Haley (Cecchini)'),('danielle_haley','Danielle Haley'),('cameron_haley','Cameron Haley'),('turner_banyasz','Turner Banyasz'),('tyler_banyasz','Tyler Banyasz'),('alyssa_haley','Alyssa Haley'),('michael_haley','Michael Haley'),('javier_gdovic','Javier Gdovic'),('henry_michael_haley','Henry Michael Haley')]:person(k,n,s)
kids(['catherine_jacob'],['joseph_haley','amy_haley','tom_haley','debbie_haley'],s)
for a,cs in [('joseph_haley',['danielle_haley','cameron_haley']),('amy_haley',['turner_banyasz','tyler_banyasz']),('tom_haley',['alyssa_haley','michael_haley']),('debbie_haley',['javier_gdovic']),('michael_haley',['henry_michael_haley'])]:kids([a],cs,s)
s='3624.jpg'
person('dutch','Dutch',s);person('phil','Phil',s);person('jeanmarie','Jeanmarie',s);couple('phil','jeanmarie',s);kids(['edward_jacob'],['phil'],s,'tentative','Header Ed (Mary Pat Egan) seems to indicate Phil’s parent; verify.')
person('mary_pat_egan','Mary Pat Egan',s);couple('edward_jacob','mary_pat_egan',s,'tentative','Handwritten header may refer to Ed’s spouse.');kids(['phil','jeanmarie'],['dutch','corey','kelley_phil'],s)
for k,n in [('corey','Corey'),('kelley_phil','Kelley'),('quinn','Quinn'),('jacob_child','Jacob'),('chance','Chance'),('kinsley','Kinsley'),('mike_smith','Mike Smith'),('michael_mac','Michael (Mac)'),('josie','Josie'),('declan','Declan'),('kelay','Kelay'),('bill_rodgers','Bill Rodgers'),('brendan','Brendan'),('paige','Paige'),('steve','Steve'),('julie','Julie'),('trish','Trish'),('brian_hannay','Brian Hannay'),('kaya','Kaya'),('john_liebgodt','John Liebgodt'),('eloise','Eloise'),('collins','Collins'),('jaws','Jaws [?]'),('carrie','Carrie'),('tim_meyer','Tim Meyer'),('ray','Ray'),('jack_meyer','Jack'),('stephen','Stephen'),('maura','Maura'),('vince_lanham','Vince Lanham')]:person(k,n,s)
kids(['dutch'],['quinn','jacob_child'],s);kids(['corey'],['chance','kinsley'],s);couple('kelley_phil','mike_smith',s);kids(['kelley_phil'],['michael_mac','josie','declan'],s)
kids(['edward_jacob'],['kelay','steve','trish'],s,'tentative','Handwritten sibling line appears below Ed; confirm.');couple('kelay','bill_rodgers',s);kids(['kelay'],['brendan'],s);couple('brendan','paige',s);couple('steve','julie',s);couple('trish','brian_hannay',s)
kids(['steve'],['kaya','carrie','stephen','maura'],s,'tentative','Long branch line under Steve; confirm.');couple('kaya','john_liebgodt',s);kids(['kaya'],['eloise','collins','jaws'],s);couple('carrie','tim_meyer',s);kids(['carrie'],['ray','jack_meyer'],s);couple('maura','vince_lanham',s)
# Save structured outputs.
data={'people':list(people.values()),'relationships':edges,'photo_branches':sheets,'read_me':'Every relationship retains its source photograph. Tentative links require review. 3618–3620 are overlapping photos of one sheet; identifiers are internal and do not identify living persons outside this file.'}
(P/'master_family.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
with (P/'people.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['id','name','birth','death','sources','notes']);w.writeheader();w.writerows({**p,'sources':'; '.join(p['sources']),'notes':'; '.join(p['notes'])} for p in people.values())
with (P/'relationships.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=['from','to','type','source','confidence','note']);w.writeheader();w.writerows(edges)
for source,ids in sheets.items():
 name=source.split('.')[0].replace(' / ','_')
 (P/f'branch_{name}.json').write_text(json.dumps({'source':source,'people':[people[i] for i in ids],'relationships':[e for e in edges if e['source']==source]},ensure_ascii=False,indent=2),encoding='utf8')
print(len(people),'people',len(edges),'relationships',len(sheets),'photo groups')
