import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';
import crypto from 'node:crypto';
const root='C:/Users/KK/VIDEO009_VISUAL_PRODUCTION/DOCUMENTS';
const rows=JSON.parse(fs.readFileSync(path.join(root,'SOURCE_DOWNLOADS.json'),'utf8')).filter(x=>['DOJ_PLEA','DOJ_VIP','DOJ_SENTENCE'].includes(x.source_id));
rows.push({source_id:'DOJ_INITIAL_CHARGES',url:'https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-individual-defrauding-investors-digital'});
const browser=spawn('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',['--headless','--disable-gpu','--no-first-run','--remote-debugging-port=9239','--user-data-dir='+path.join(root,'CDP_PROFILE'),'about:blank'],{stdio:'ignore',windowsHide:true});
const delay=t=>new Promise(r=>setTimeout(r,t));
let targets;
for(let i=0;i<60;i++){try{targets=await(await fetch('http://127.0.0.1:9239/json')).json();break;}catch{await delay(200);}}
if(!targets)throw Error('Browser debugging endpoint unavailable');
const ws=new WebSocket(targets.find(x=>x.type==='page').webSocketDebuggerUrl);await new Promise((r,j)=>{ws.onopen=r;ws.onerror=j;});
let id=0;const pending=new Map();
ws.onmessage=e=>{const x=JSON.parse(e.data);if(x.id&&pending.has(x.id)){const {resolve,reject}=pending.get(x.id);pending.delete(x.id);x.error?reject(Error(JSON.stringify(x.error))):resolve(x.result);}};
const send=(method,params={})=>new Promise((resolve,reject)=>{const n=++id;pending.set(n,{resolve,reject});ws.send(JSON.stringify({id:n,method,params}));setTimeout(()=>{if(pending.has(n)){pending.delete(n);reject(Error('CDP timeout '+method));}},45000).unref();});
await send('Page.enable');await send('Runtime.enable');
const outputs=[];
for(const row of rows){
  try{
    await send('Page.navigate',{url:row.url});await delay(7000);
    const value=await send('Runtime.evaluate',{expression:"fetch(location.href).then(async r=>({status:r.status,url:r.url,body:await r.text()}))",awaitPromise:true,returnByValue:true});
    const data=value.result.value;if(!data)throw Error('No browser response');
    const file=path.join(root,'ORIGINALS',row.source_id+'_BROWSER_RESPONSE.html');fs.writeFileSync(file,data.body,'utf8');
    const valid=data.status===200&&data.body.includes('McFarland')&&data.body.length>10000&&!data.body.includes('triggerInterstitialChallenge');
    if(valid){const pdf=await send('Page.printToPDF',{printBackground:true,displayHeaderFooter:true,preferCSSPageSize:true});fs.writeFileSync(path.join(root,'RENDERED_PAGES',row.source_id+'_BROWSER_PRINT.pdf'),Buffer.from(pdf.data,'base64'));}
    const entry={source_id:row.source_id,url:row.url,status:data.status,final_url:data.url,file,bytes:Buffer.byteLength(data.body),sha256:crypto.createHash('sha256').update(data.body).digest('hex'),valid_official_content:valid,provenance:'Exact decoded response body retrieved by the ordinary browser fetch API after native page navigation; no text reconstruction',retrieved_utc:new Date().toISOString()};
    outputs.push(entry);console.log(JSON.stringify(entry));
  }catch(e){outputs.push({...row,error:String(e),valid_official_content:false});console.log(JSON.stringify(outputs.at(-1)));}
}
fs.writeFileSync(path.join(root,'BROWSER_ORIGINAL_RESPONSES.json'),JSON.stringify(outputs,null,2));
try{await send('Browser.close');}catch{}ws.close();browser.unref();
