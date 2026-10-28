import {chromium} from '../remotion/node_modules/playwright-core/index.mjs';
import {createHash} from 'node:crypto';
import {createReadStream, existsSync, mkdirSync, readdirSync, unlinkSync, writeFileSync} from 'node:fs';
import {basename, join, resolve} from 'node:path';
import {pathToFileURL} from 'node:url';

const sourceDir=resolve('C:/Users/KK/VIDEO008_PRODUCTION/VIDEO008_SOURCE_ARCHIVE/03_ORIGINAL_DOCUMENTS');
const outputDir=resolve('C:/Users/KK/VIDEO008_PRODUCTION/VIDEO008_FINAL_VISUAL_PACK/DOCUMENTS/CROPS');
mkdirSync(outputDir,{recursive:true});
const files=readdirSync(sourceDir);
const findSource=(id)=>join(sourceDir,files.find(f=>f.startsWith(id+'_'))||'__MISSING__');
const liveUrls={
 SRC011:'https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents',
 SRC012:'https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals'
};
const tasks=[
 ['SC005','SRC001','72,388','PASS'],['SC013','SRC001','125.2','PASS'],['SC018','SRC001','8,945','PASS'],
 ['SC025','SRC001','This prospectus contains forward-looking statements','PASS'],['SC027','SRC001','Lease Arrangement','PASS'],['SC031','SRC001','non-cancelable','PASS'],
 ['SC034','SRC001','acceleration','PASS'],['SC038','SRC017','special purpose vehicle','PASS'],['SC043','SRC018','residual value support','HOLD'],
 ['SC049','SRC004','42,000,000,000','PASS'],['SC051','SRC005','30,000,000,000','PASS'],['SC053','SRC001','6.2 billion','PASS'],
 ['SC057','SRC001','72,388','PASS'],['SC062','SRC001','1,111','PASS'],['SC066','SRC001','80,748','PASS'],
 ['SC071','SRC001','50.1%','PASS'],['SC076','SRC008','Class T Directors','PASS'],['SC082','SRC011','We present an alignment assessment','PASS'],
 ['SC084','SRC011','four incidents','PASS'],['SC086','SRC001','civil investigative demand','PASS'],['SC092','SRC001','16,286','PASS'],
 ['SC100','SRC001','50.1%','PASS'],['SC102','SRC001','subject to completion','PASS'],['SC106','SRC001','125.2','PARTIAL_HOLD']
];
const hash=async(p)=>new Promise((ok,no)=>{const h=createHash('sha256');createReadStream(p).on('data',d=>h.update(d)).on('end',()=>ok(h.digest('hex').toUpperCase())).on('error',no)});
const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'});
const context=await browser.newContext({viewport:{width:1600,height:900},deviceScaleFactor:1});
const rows=[];
for(const [scene,source,keyword,planned] of tasks){
 const src=findSource(source); const out=join(outputDir,`${scene}_${source}_AUTHENTIC_CROP.png`);
 if(existsSync(out)) unlinkSync(out);
 if(planned==='HOLD'||!existsSync(src)){
  rows.push({scene_id:scene,source_id:source,keyword,source_file:existsSync(src)?basename(src):'',crop_file:'',sha256:'',width:'',height:'',status:'HOLD_SOURCE_UNAVAILABLE',notes:'Official Broadcom endpoint returned Access Denied; no substitute or reconstructed document used.'}); continue;
 }
 const page=await context.newPage();
 try{
  page.setDefaultTimeout(120000);
  const target=liveUrls[source]||pathToFileURL(src).href;
  await page.goto(target,{waitUntil:'domcontentloaded',timeout:120000});
  if(liveUrls[source]) await page.waitForTimeout(2500);
  const result=await page.evaluate(({keyword})=>{
   const needle=keyword.toLowerCase(); const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT); const matches=[];
   let node; while((node=walker.nextNode())){if((node.textContent||'').toLowerCase().includes(needle)){
    let el=node.parentElement; if(!el) continue;
    el=el.closest('tr')||el.closest('p,li,h1,h2,h3,h4')||el;
    const text=(el.innerText||el.textContent||'').trim();
    matches.push({el,text,score:(el.tagName==='TR'?5:0)+(!el.closest('a')?3:0)+(!/table of contents/i.test(text)?3:0)+(text.length>40?2:0)});
   }}
   matches.sort((a,b)=>b.score-a.score); const best=matches[0]; if(!best)return {found:false};
   best.el.scrollIntoView({block:'center',inline:'nearest'}); best.el.style.outline='5px solid #D3AD32'; best.el.style.outlineOffset='4px'; best.el.style.backgroundColor='rgba(211,173,50,0.08)';
   return {found:true,tag:best.el.tagName,text:best.text.slice(0,500)};
  },{keyword});
  if(!result.found) throw new Error(`keyword not found: ${keyword}`);
  await page.waitForTimeout(250);
  await page.screenshot({path:out,type:'png',timeout:120000});
  rows.push({scene_id:scene,source_id:source,keyword,source_file:basename(src),crop_file:`DOCUMENTS/CROPS/${basename(out)}`,sha256:await hash(out),width:1600,height:900,status:planned==='PARTIAL_HOLD'?'PARTIAL_PASS_SECOND_SOURCE_HOLD':'AUTHENTIC_SOURCE_CROP_TECH_PASS',notes:planned==='PARTIAL_HOLD'?'SEC lease crop captured; required Broadcom juxtaposition remains HOLD because official endpoint denied access.':'Local capture of downloaded primary-source pixels; yellow outline is editorial highlight only.'});
 }catch(e){rows.push({scene_id:scene,source_id:source,keyword,source_file:basename(src),crop_file:'',sha256:'',width:'',height:'',status:'HOLD_CAPTURE_FAILED',notes:String(e.message||e)});}finally{await page.close();}
}
await browser.close();
const cols=['scene_id','source_id','keyword','source_file','crop_file','sha256','width','height','status','notes'];
const q=v=>`"${String(v??'').replaceAll('"','""')}"`;
writeFileSync(join(outputDir,'DOCUMENT_CROP_MANIFEST.csv'),cols.join(',')+'\n'+rows.map(r=>cols.map(c=>q(r[c])).join(',')).join('\n')+'\n');
console.log(JSON.stringify({total:rows.length,pass:rows.filter(r=>r.status.includes('PASS')).length,hold:rows.filter(r=>r.status.includes('HOLD')).length},null,2));
