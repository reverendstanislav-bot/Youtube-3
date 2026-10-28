import React from 'react';
import {AbsoluteFill} from 'remotion';
import type {Graphic} from './data';

const C={bg:'#0B0B0B',panel:'#1F1F1F',text:'#EDEDED',muted:'#A8A8A8',red:'#D32222',gold:'#B69B68'};
export const GraphicFrame: React.FC<Graphic> = ({scene,eyebrow,title,note,kind,items}) => {
  const horizontal=kind==='flow'||kind==='timeline'||kind==='columns'||kind==='split'||kind==='matrix';
  const barMax=Math.max(...items.map(i=>Number(i.value.replace(/[^0-9.]/g,''))||1));
  return <AbsoluteFill style={{backgroundColor:C.bg,color:C.text,fontFamily:'Arial, Helvetica, sans-serif',padding:'74px 92px 220px',boxSizing:'border-box'}}>
    <div style={{fontSize:25,letterSpacing:4,color:C.gold,fontWeight:700}}>{eyebrow}</div>
    <div style={{fontSize:72,lineHeight:1.02,fontWeight:900,letterSpacing:-2,maxWidth:1600,marginTop:22}}>{title}</div>
    <div style={{height:5,width:150,background:C.red,marginTop:30}} />
    {kind==='bars' ? <div style={{display:'flex',gap:46,alignItems:'flex-end',height:470,marginTop:38}}>{items.map((it,i)=>{
      const n=Number(it.value.replace(/[^0-9.]/g,''))||1; return <div key={it.label} style={{flex:1,display:'flex',flexDirection:'column',justifyContent:'flex-end',height:'100%'}}><div style={{fontSize:44,fontWeight:900,marginBottom:16}}>{it.value}</div><div style={{height:Math.max(48,(n/barMax)*340),background:it.accent?C.red:C.gold}}/><div style={{fontSize:25,letterSpacing:2,marginTop:16,color:C.muted}}>{it.label}</div></div>})}</div>
    : <div style={{display:'flex',flexDirection:horizontal?'row':'column',gap:22,marginTop:48,alignItems:'stretch'}}>{items.map((it,i)=><React.Fragment key={it.label}><div style={{flex:1,minHeight:horizontal?260:104,background:C.panel,borderTop:`6px solid ${it.accent?C.red:C.gold}`,padding:'30px 32px',display:'flex',flexDirection:'column',justifyContent:'center'}}><div style={{fontSize:21,letterSpacing:2.5,color:C.muted,fontWeight:700}}>{it.label}</div><div style={{fontSize:horizontal?39:48,lineHeight:1.08,fontWeight:900,marginTop:14}}>{it.value}</div></div>{(kind==='flow'||kind==='timeline')&&i<items.length-1?<div style={{fontSize:52,color:C.red,alignSelf:'center'}}>→</div>:null}</React.Fragment>)}</div>}
    <div style={{position:'absolute',left:92,right:92,bottom:118,display:'flex',justifyContent:'space-between',alignItems:'flex-end',borderTop:'1px solid #444',paddingTop:24}}><div style={{fontSize:27,color:C.muted,maxWidth:1450}}>{note}</div><div style={{fontSize:24,letterSpacing:3,color:'#666'}}>{scene}</div></div>
  </AbsoluteFill>;
};
