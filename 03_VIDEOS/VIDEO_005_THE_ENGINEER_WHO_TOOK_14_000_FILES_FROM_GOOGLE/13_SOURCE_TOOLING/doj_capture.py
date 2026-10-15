#!/usr/bin/env python3
"""Capture final publisher-rendered DOJ originals after meta-refresh instead of archiving DOJ interstitial HTML."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import hashlib,datetime,json,re
B=Path(__file__).resolve().parents[1]/'13_SOURCE_DOJ_ORIGINALS'
B.mkdir(exist_ok=True,parents=True)
urls={
'S010':'https://www.justice.gov/usao-ndca/pr/former-uber-self-driving-car-executive-signs-agreement-plead-guilty-theft-trade-secrets',
'S011':'https://www.justice.gov/usao-ndca/pr/former-uber-executive-sentenced-18-months-jail-trade-secret-theft-google'}
targets={'S010':['December 11, 2015','weekly','33'], 'S011':['one count','33 counts','pleaded guilty','18 months']}
results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1700,'height':1000},device_scale_factor=1)
 for sid,url in urls.items():
  try:
   page.goto(url,wait_until='domcontentloaded',timeout=40000)
   for i in range(10):
    page.wait_for_timeout(1500)
    body=page.locator('body').inner_text(timeout=5000)
    if 'Levandowski' in body and len(body)>1700:break
   html=page.content()
   file=B/(sid+'_ACTUAL_RENDERED_DOM.html')
   file.write_text(html,encoding='utf8')
   accepted=('Levandowski' in body and len(body)>1700 and '<title>&nbsp;</title>' not in html)
   item={'id':sid,'url':url,'resolved_url':page.url,'title':page.title(),
        'rendered_dom_path':file.name,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),
        'body_chars':len(body),'verified_rendered_original':accepted,
        'capture_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'anchors':[]}
   for j,a in enumerate(targets[sid]):
    match=page.locator('p').filter(has_text=re.compile(re.escape(a),re.I))
    if not match.count():
      item['anchors'].append({'phrase':a,'status':'HOLD_NOT_FOUND'})
      continue
    el=match.first
    filename=sid+'_source_paragraph_'+str(j)+'.png'
    try:
      el.scroll_into_view_if_needed(timeout=8000)
      bbox=el.bounding_box()
      scroll=page.evaluate('({x:window.scrollX,y:window.scrollY})')
      el.screenshot(path=str(B/filename),timeout=15000)
      raw=(B/filename).read_bytes()
      item['anchors'].append({'phrase':a,'status':'CAPTURED_ORIGINAL_DOM_PIXEL','file':filename,'sha256':hashlib.sha256(raw).hexdigest(),
                             'source_dom_crop_rect_css_px':[round(bbox['x']+scroll['x'],1),round(bbox['y']+scroll['y'],1),round(bbox['width'],1),round(bbox['height'],1)],
                             'viewport_px':[1700,1000]})
    except Exception as e:item['anchors'].append({'phrase':a,'status':'HOLD_SCREENSHOT','error':str(e)[:200]})
   results.append(item)
  except Exception as e:results.append({'id':sid,'status':'HOLD_BROWSER_ACCESS','error':str(e)[:350]})
 browser.close()
(B/'DOJ_RENDERED_ORIGINALS_QC.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2)[:7000])
